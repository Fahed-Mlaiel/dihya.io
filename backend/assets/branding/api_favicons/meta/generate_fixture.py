# Dihya API Favicon – Générateur de fixtures de test

import json
import pytest
from meta_favicon_api import meta_favicon_api

def generate_fixture():
    with open('meta_favicon_api_fixture.json', 'w', encoding='utf-8') as f:
        json.dump(meta_favicon_api, f, ensure_ascii=False, indent=2)
    print("Fixture générée: meta_favicon_api_fixture.json")

@pytest.fixture
def meta_favicon_api_fixture():
    with open('meta_favicon_api_fixture.json', encoding='utf-8') as f:
        return json.load(f)

if __name__ == "__main__":
    generate_fixture()
