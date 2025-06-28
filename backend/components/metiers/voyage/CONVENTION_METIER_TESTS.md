# Convention de nommage et de structuration des fichiers métier et tests Voyage

"""
1. Chaque fichier métier doit avoir un fichier de test associé dans tests_centralises, avec une logique métier réelle testée (pas de test vide ou factice).
2. Les fichiers de test doivent contenir au moins une assertion réelle (assert, expect, etc.) et cibler explicitement le fichier métier associé.
3. Les fichiers vides ou de structure (.keep) sont autorisés uniquement pour garantir la présence de dossiers nécessaires à l’architecture.
4. Toute création de nouveau fichier métier ou test doit être justifiée par un besoin métier réel et documentée dans le code.
5. Les conventions de nommage doivent être respectées : test_<nom_module>.py, <module>.test.js, etc.
6. Les fichiers inutilisés, vides (hors .keep), ou sans logique métier/test réelle doivent être supprimés ou complétés immédiatement.
7. Toute modification de la structure doit être validée par revue de code et testée automatiquement en CI.

Cette convention garantit une base de code propre, professionnelle, sans doublon ni parasite, et une couverture de test maximale.
"""
