"""
Script CLI d’import/export de projets 3D (Dihya)
Usage : python cli_3d.py export --id 1 | python cli_3d.py import --file export.json
"""
import argparse
import json
import requests

def export_project(project_id, output):
    url = f"http://localhost:8000/threedprojects/{project_id}/export_rgpd/"
    r = requests.get(url)
    with open(output, 'w') as f:
        json.dump(r.json(), f, indent=2)
    print(f"Exporté dans {output}")

def import_project(input_file):
    with open(input_file) as f:
        data = json.load(f)
    url = "http://localhost:8000/threedprojects/"
    r = requests.post(url, json=data['project'])
    print(f"Import status: {r.status_code}")

def main():
    parser = argparse.ArgumentParser(description="CLI 3D Dihya")
    sub = parser.add_subparsers(dest='cmd')
    exp = sub.add_parser('export')
    exp.add_argument('--id', type=int, required=True)
    exp.add_argument('--output', default='export.json')
    imp = sub.add_parser('import')
    imp.add_argument('--file', required=True)
    args = parser.parse_args()
    if args.cmd == 'export':
        export_project(args.id, args.output)
    elif args.cmd == 'import':
        import_project(args.file)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
