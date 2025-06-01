"""
Routes Compliance (REST/GraphQL, sécurité, multilingue, RGPD, plugins, audit, multitenant)
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ComplianceReportViewSet

router = DefaultRouter()
router.register(r'reports', ComplianceReportViewSet, basename='compliance-report')

urlpatterns = [
    path('', include(router.urls)),
]
