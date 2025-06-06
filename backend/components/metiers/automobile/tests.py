# Entrée unique pour les tests automobile ultra avancés
from .tests.test_automobile import test_automobile_creation

def run_all():
    test_automobile_creation()
    print('Tous les tests automobile sont passés.')

if __name__ == '__main__':
    run_all()
