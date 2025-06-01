"""
Routes SEO : robots.txt, sitemap.xml, logs structurés, plugins, RGPD, audit, IA.
"""
from fastapi import APIRouter, Depends, Request, Response
from typing import Any
from backend.utils.security import audit_log, waf_protect
from backend.utils.i18n import get_locale
from backend.utils.plugins import plugin_hook
from backend.utils.seo import generate_robots, generate_sitemap
from backend.utils.multitenancy import get_tenant
from backend.utils.graphql import graphql_router

router = APIRouter(prefix="/seo", tags=["SEO"])

@router.get("/robots.txt", summary="robots.txt dynamique")
@waf_protect
@audit_log
async def robots_txt(request: Request, tenant=Depends(get_tenant), locale=Depends(get_locale)):
    """
    Génère un robots.txt dynamique (multilingue, plugins, RGPD).
    """
    robots = plugin_hook("seo_robots", tenant=tenant, locale=locale) or generate_robots(tenant, locale)
    return Response(content=robots, media_type="text/plain")

@router.get("/sitemap.xml", summary="sitemap.xml dynamique")
@waf_protect
@audit_log
async def sitemap_xml(request: Request, tenant=Depends(get_tenant), locale=Depends(get_locale)):
    """
    Génère un sitemap.xml dynamique (multilingue, plugins, RGPD).
    """
    sitemap = plugin_hook("seo_sitemap", tenant=tenant, locale=locale) or generate_sitemap(tenant, locale)
    return Response(content=sitemap, media_type="application/xml")

# Intégration GraphQL
router.include_router(graphql_router, prefix="/graphql")
