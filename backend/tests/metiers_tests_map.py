"""
Map exhaustive des modules métiers Dihya vers leurs fichiers de tests d'intégration et unitaires.
Utilisé pour automatiser la cohérence, la couverture et la génération de documentation/tests.
"""
METIERS_TESTS_MAP = {
    "restauration": ["integration/restauration/test_restauration_backend.py"],
    "sante": ["integration/sante/test_sante_backend.py"],
    "science": ["integration/science/test_science_backend.py"],
    "securite": ["integration/securite/test_securite_backend.py"],
    "seo": ["integration/seo/test_seo_backend.py"],
    "services_personne": ["integration/services_personne/test_services_personne_backend.py"],
    "social": ["integration/social/test_social_backend.py"],
    "sport": ["integration/sport/test_sport_backend.py"],
    "tourisme": ["integration/tourisme/test_tourisme_backend.py"],
    "transport": ["integration/transport/test_transport_backend.py"],
    "utils": ["integration/utils/test_utils_backend.py"],
    "validators": ["integration/validators/test_validators_backend.py"],
    "voice": ["integration/voice/test_voice_backend.py"],
    "voyage": ["integration/voyage/test_voyage_backend.py"],
    "vr_ar": ["integration/vr_ar/test_vr_ar_backend.py"],
    "3d": ["unit/3d_unit.py"],
    "administration_publique": ["unit/administration_publique_unit.py"],
    "agriculture": ["unit/agriculture_unit.py"],
}
