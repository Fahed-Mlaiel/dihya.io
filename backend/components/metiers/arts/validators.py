# Validators pour Arts

def is_valid_artwork(artwork):
    return all(k in artwork for k in ("id", "nom", "type", "artiste"))

def is_valid_exposition(expo):
    return all(k in expo for k in ("id", "nom", "lieu", "date"))

def is_valid_artiste(artiste):
    return all(k in artiste for k in ("id", "nom"))
