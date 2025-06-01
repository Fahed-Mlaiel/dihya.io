"""
Templates ultra avancés pour VR/AR (Django routes)
Exemples de templates métiers, extensibles, multilingues, RGPD-ready.
"""
VR_AR_SCENE_TEMPLATE = {
    'fr': {
        'title': 'Exemple de scène VR/AR',
        'description': 'Ceci est un template de scène immersive en français.'
    },
    'en': {
        'title': 'Sample VR/AR Scene',
        'description': 'This is a sample immersive scene template in English.'
    },
    'ar': {
        'title': 'مثال على مشهد VR/AR',
        'description': 'هذا قالب لمشهد غامر باللغة العربية.'
    },
    'ber': {
        'title': 'ⴰⵙⴽⴰⵏⴰ VR/AR',
        'description': 'ⴰⴷⵔⴰⵙ ⵏ ⴰⵙⴽⴰⵏⴰ ⴷ ⵜⴰⵎⴰⵣⵉⵖⵜ.'
    }
}

VR_AR_ASSET_TEMPLATE = {
    'fr': {
        'type': '3D',
        'file': 'exemple_asset_3d.glb'
    },
    'en': {
        'type': '3D',
        'file': 'sample_asset_3d.glb'
    }
}
