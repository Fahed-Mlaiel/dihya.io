"""
Dihya Frontend – Main Script (Python)
Automatisation, génération, tests, i18n, accessibilité, multilingue, souverain, documenté, prêt à l'emploi.
"""
import subprocess

def generate_i18n():
    print('Génération des fichiers i18n...')
    subprocess.run(['python', 'generate_i18n.py'], check=True)

def run_accessibility_audit():
    print('Audit accessibilité en cours...')
    subprocess.run(['npx', 'axe', 'build'], check=True)

def run_e2e_tests():
    print('Lancement des tests E2E...')
    subprocess.run(['npm', 'run', 'e2e'], check=True)

def build_frontend():
    print('Build du frontend...')
    subprocess.run(['npm', 'run', 'build'], check=True)

def main():
    generate_i18n()
    run_accessibility_audit()
    run_e2e_tests()
    build_frontend()

if __name__ == '__main__':
    main()
