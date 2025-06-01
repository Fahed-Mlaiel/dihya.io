"""
metiers_config.py - Configuration métiers backend Dihya Coding
Sécurité, i18n, audit, extensibilité, documentation intégrée.
"""
from typing import Dict, List

METIERS: List[Dict] = [
    {
        "key": "voyage",
        "label": {
            "fr": "Voyage", "en": "Travel", "ar": "السفر", "de": "Reise", "zh": "旅行", "ja": "旅行", "ko": "여행", "nl": "Reis", "he": "טיול", "fa": "سفر", "hi": "यात्रा", "es": "Viaje", "amazigh": "ⴰⵙⴳⴰⵙ"
        },
        "roles": ["admin", "user"],
        "enabled": True,
        "plugin": False
    },
    {
        "key": "vr_ar",
        "label": {
            "fr": "VR/AR", "en": "VR/AR", "ar": "الواقع الافتراضي/المعزز", "de": "VR/AR", "zh": "虚拟现实/增强现实", "ja": "VR/AR", "ko": "VR/AR", "nl": "VR/AR", "he": "VR/AR", "fa": "واقعیت مجازی/افزوده", "hi": "वीआर/एआर", "es": "VR/AR", "amazigh": "VR/AR"
        },
        "roles": ["admin", "user"],
        "enabled": True,
        "plugin": True
    },
    # ...autres métiers extensibles
]
