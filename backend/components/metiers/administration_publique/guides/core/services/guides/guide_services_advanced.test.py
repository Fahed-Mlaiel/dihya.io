"""
Test unitaire pour guide_services_advanced.md (Python)
"""
def test_guide_services_advanced_existe():
    with open('guide_services_advanced.md', encoding='utf-8') as f:
        content = f.read()
    assert 'Guide avancé' in content
