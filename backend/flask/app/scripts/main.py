#!/usr/bin/env python3
"""
Script CLI/API avancé pour la gestion de projets IA/VR/AR, plugins, audit, multilingue, sécurité, génération automatique.
Compatible Linux, Codespaces, CI, production.
"""
import argparse
from .services import generate_project, list_projects, audit_log, i18n, plugins

def main():
    parser = argparse.ArgumentParser(description='Gestion avancée de projets IA/VR/AR (CLI/API)')
    subparsers = parser.add_subparsers(dest='command')

    gen_parser = subparsers.add_parser('generate', help='Génère un projet (web, mobile, IA, etc.)')
    gen_parser.add_argument('type', choices=['web', 'mobile', 'ia', 'vr', 'ar'])
    gen_parser.add_argument('--lang', default='fr', help='Langue (fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es, amazigh)')

    subparsers.add_parser('list', help='Liste les projets existants')

    plugin_parser = subparsers.add_parser('plugin', help='Gère les plugins dynamiquement')
    plugin_parser.add_argument('action', choices=['add', 'remove', 'list'])
    plugin_parser.add_argument('--lang', default='fr')

    args = parser.parse_args()

    if args.command == 'generate':
        generate_project(args.type, args.lang)
        audit_log('generate', {'type': args.type, 'lang': args.lang})
    elif args.command == 'list':
        list_projects(args.lang if hasattr(args, 'lang') else 'fr')
    elif args.command == 'plugin':
        plugins(args.action, args.lang)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
