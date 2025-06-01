"""
Routes principales publiques pour l'application Dihya Coding.
Inclut : accueil, healthcheck, informations API, endpoints utilitaires et sécurité de base.
"""

from flask import jsonify, request
from . import main

@main.route("/", methods=["GET"])
def home():
    """
    Page d'accueil de l'API Dihya Coding.
    ---
    responses:
      200:
        description: Message de bienvenue.
    """
    return jsonify({
        "message": "Bienvenue sur l'API Dihya Coding.",
        "version": "1.0.0",
        "documentation": "/api/docs"
    }), 200

@main.route("/api/health", methods=["GET"])
def health():
    """
    Endpoint de healthcheck pour vérifier que l'API fonctionne.
    ---
    responses:
      200:
        description: Statut OK.
    """
    return jsonify({
        "status": "ok",
        "message": "Dihya API opérationnelle"
    }), 200

@main.route("/api/info", methods=["GET"])
def api_info():
    """
    Informations générales sur l'API (version, auteur, etc.).
    ---
    responses:
      200:
        description: Infos API.
    """
    return jsonify({
        "project": "Dihya Coding",
        "version": "1.0.0",
        "author": "Dihya Coding Team",
        "features": [
            "No-Code/Low-Code",
            "Génération multistack",
            "Multilingue",
            "Sécurité avancée"
        ]
    }), 200

@main.route("/api/echo", methods=["POST"])
def echo():
    """
    Endpoint utilitaire pour tester la réception de données (debug).
    ---
    parameters:
      - in: body
        name: data
        required: true
        description: Données à renvoyer.
    responses:
      200:
        description: Données reçues.
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "Aucune donnée reçue"}), 400
    return jsonify({"received": data}), 200

@main.route("/api/ping", methods=["GET"])
def ping():
    """
    Endpoint simple pour monitoring externe (anti-censure, uptime robot, etc.).
    ---
    responses:
      200:
        description: Pong.
    """
    return jsonify({"pong": True}), 200

# Route robots.txt pour SEO
@main.route("/robots.txt", methods=["GET"])
def robots_txt():
    """
    Sert le fichier robots.txt pour le SEO.
    """
    content = "User-agent: *\nDisallow:"
    return content, 200, {"Content-Type": "text/plain"}

# Route sitemap.xml pour SEO
@main.route("/sitemap.xml", methods=["GET"])
def sitemap_xml():
    """
    Sert le sitemap.xml pour le SEO.
    """
    base_url = request.host_url.rstrip("/")
    urls = [
        f"{base_url}/",
        f"{base_url}/api/info",
        f"{base_url}/api/health"
    ]
    xml = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for url in urls:
        xml.append(f"  <url><loc>{url}</loc></url>")
    xml.append('</urlset>')
    return "\n".join(xml), 200, {"Content-Type": "application/xml"}