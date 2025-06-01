"""
Audit log avancé pour la traçabilité RGPD et la sécurité des projets VR/AR.
"""
from django.utils import timezone
from django.conf import settings
from django.db import models

def audit_log_action(user, action, instance):
    """
    Loggue une action d'audit sur un projet VR/AR.
    """
    from core.models import AuditLog
    AuditLog.objects.create(
        user=user,
        action=action,
        content_object=instance,
        timestamp=timezone.now(),
        tenant=getattr(instance, 'tenant', None)
    )
