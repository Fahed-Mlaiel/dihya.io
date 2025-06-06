# Point d'entrée principal pour le module Arts
from .arts import get_expositions, get_oeuvres, get_artistes

if __name__ == "__main__":
    print("Expositions:", get_expositions())
    print("Œuvres:", get_oeuvres())
    print("Artistes:", get_artistes())
