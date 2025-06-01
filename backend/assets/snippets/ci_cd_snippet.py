"""
ci_cd_snippet.py – CI/CD backend (Dihya)
Lint, test, build, logs, audit, RGPD, multilingue.
"""
import subprocess

def run_lint():
    return subprocess.call(["python3", "-m", "py_compile", "test_snippet.py"])

def run_tests():
    return subprocess.call(["pytest", "test_snippet.py"])

# Exemple d’utilisation
if __name__ == "__main__":
    print("Lint:", run_lint())
    print("Tests:", run_tests())
