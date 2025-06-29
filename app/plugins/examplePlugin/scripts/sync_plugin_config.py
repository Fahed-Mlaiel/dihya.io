"""Script Python pour synchroniser la config du plugin avec l’application principale"""

import json

def sync_config():
    with open('../plugin.config.js', 'r') as f:
        config = f.read()
    print('Config du plugin synchronisée (exemple).')

if __name__ == "__main__":
    sync_config()
