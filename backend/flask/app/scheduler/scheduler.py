"""
Module Scheduler pour Dihya Coding.

Ce module gère la planification et l’exécution de tâches asynchrones ou périodiques côté backend.
Exemples : nettoyage, notifications programmées, génération différée, synchronisation, etc.

Bonnes pratiques :
- Validation stricte des tâches à planifier
- Sécurité : seules les tâches autorisées peuvent être planifiées
- Logging horodaté de chaque exécution
- API sécurisée pour ajouter/lister/supprimer des tâches (JWT requis)
- Extensible pour supporter différents types de tâches

Ce module utilise une file en mémoire pour le mode démo (remplaçable par Celery, RQ, etc. en prod).
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime, timedelta
import threading
import time

bp = Blueprint("scheduler", __name__, url_prefix="/api/scheduler")

# Tâches autorisées (à étendre selon les besoins)
ALLOWED_TASKS = {"cleanup", "send_notification", "generate_report"}

# File de tâches en mémoire (démo)
TASK_QUEUE = []
TASK_LOCK = threading.Lock()

class ScheduledTask:
    def __init__(self, user_id, task_type, params=None, run_at=None):
        if task_type not in ALLOWED_TASKS:
            raise ValueError("Type de tâche non autorisé")
        self.user_id = user_id
        self.task_type = task_type
        self.params = params or {}
        self.run_at = run_at or datetime.utcnow()
        self.created_at = datetime.utcnow()
        self.status = "pending"

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "task_type": self.task_type,
            "params": self.params,
            "run_at": self.run_at.isoformat(),
            "created_at": self.created_at.isoformat(),
            "status": self.status
        }

def log_task_action(user_id, action, task_type):
    print(f"[{datetime.utcnow().isoformat()}] [SCHEDULER] user={user_id} action={action} type={task_type}")

def add_task(task: ScheduledTask):
    with TASK_LOCK:
        TASK_QUEUE.append(task)
    log_task_action(task.user_id, "add", task.task_type)

def list_tasks(user_id):
    with TASK_LOCK:
        return [t for t in TASK_QUEUE if t.user_id == user_id]

def remove_task(user_id, idx):
    with TASK_LOCK:
        user_tasks = [t for t in TASK_QUEUE if t.user_id == user_id]
        if idx < 0 or idx >= len(user_tasks):
            raise IndexError("Tâche introuvable")
        task = user_tasks[idx]
        TASK_QUEUE.remove(task)
    log_task_action(user_id, "remove", task.task_type)

def run_due_tasks():
    """Exécute les tâches arrivées à échéance (mode démo, synchrone)."""
    now = datetime.utcnow()
    with TASK_LOCK:
        for task in TASK_QUEUE:
            if task.status == "pending" and task.run_at <= now:
                # Exécution fictive
                print(f"[{now.isoformat()}] [SCHEDULER] Exécution de la tâche {task.task_type} pour {task.user_id}")
                task.status = "done"

# Thread de fond pour exécuter les tâches périodiquement (démo)
def scheduler_thread():
    while True:
        run_due_tasks()
        time.sleep(5)

# Lancer le thread au démarrage (en mode démo uniquement)
threading.Thread(target=scheduler_thread, daemon=True).start()

def schedule_task(task, context=None):
    """
    Plant une tâche (Demo-Stub).
    Args:
        task (ScheduledTask ou dict)
        context (optionnel)
    Returns:
        str: Statut
    """
    with TASK_LOCK:
        if isinstance(task, dict):
            t = ScheduledTask(task.get("user_id", "demo"), task.get("task_type", "cleanup"))
        else:
            t = task
        TASK_QUEUE.append(t)
    return "scheduled"

def run_scheduled_tasks():
    """
    Exécute toutes les tâches planifiées (Demo-Stub).
    """
    with TASK_LOCK:
        for t in TASK_QUEUE:
            t.status = "done"
    return "toutes les tâches exécutées"

def disable_task(task_id):
    """
    Désactive une tâche planifiée (Demo-Stub).
    """
    # Dans la démo, il ne se passe rien
    return f"tâche {task_id} désactivée"

# --- ROUTES API SECURISEES ---

@bp.route("/", methods=["GET"])
@jwt_required()
def api_list_tasks():
    """Liste les tâches planifiées de l'utilisateur courant."""
    user_id = get_jwt_identity()
    tasks = list_tasks(user_id)
    return jsonify([t.to_dict() for t in tasks]), 200

@bp.route("/", methods=["POST"])
@jwt_required()
def api_add_task():
    """
    Planifie une nouvelle tâche.
    Entrée : { "task_type": "...", "params": {...}, "run_at": "ISO8601" (optionnel) }
    """
    user_id = get_jwt_identity()
    data = request.get_json(force=True)
    try:
        task_type = data.get("task_type")
        params = data.get("params", {})
        run_at = datetime.fromisoformat(data["run_at"]) if "run_at" in data else None
        task = ScheduledTask(user_id, task_type, params, run_at)
        add_task(task)
        return jsonify(task.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@bp.route("/<int:idx>", methods=["DELETE"])
@jwt_required()
def api_remove_task(idx):
    """Supprime une tâche planifiée (par index dans la liste utilisateur)."""
    user_id = get_jwt_identity()
    try:
        remove_task(user_id, idx)
        return jsonify({"message": "Tâche supprimée"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404

# À intégrer dans votre app Flask principale :
# from backend.flask.app.scheduler.scheduler import bp as scheduler_bp
# app.register_blueprint(scheduler_bp)
