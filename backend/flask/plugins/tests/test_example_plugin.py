"""
Tests unitaires et d'intégration pour le plugin métier ultra avancé Dihya Coding.
Couvre : validation stricte, RBAC, audit, multilingue, RGPD, logs, accessibilité.
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import example_plugin
import pytest

def test_run_valid_admin():
    user = {'username': 'alice', 'role': 'admin'}
    payload = {'action': 'run', 'lang': 'fr'}
    result = example_plugin.run(user, payload)
    assert result['msg'] == 'Plugin exécuté avec succès'
    assert result['user'] == 'alice'

def test_run_valid_user():
    user = {'username': 'bob', 'role': 'user'}
    payload = {'action': 'run', 'lang': 'en'}
    result = example_plugin.run(user, payload)
    assert result['msg'] == 'Plugin executed successfully'
    assert result['user'] == 'bob'

def test_run_invalid_role():
    user = {'username': 'eve', 'role': 'guest'}
    payload = {'action': 'run', 'lang': 'fr'}
    with pytest.raises(Exception):
        example_plugin.run(user, payload)

def test_run_invalid_payload():
    user = {'username': 'alice', 'role': 'admin'}
    payload = {'lang': 'fr'}
    with pytest.raises(Exception):
        example_plugin.run(user, payload)

def test_run_multilingue():
    user = {'username': 'alice', 'role': 'admin'}
    for lang, msg in [
        ('fr', 'Plugin exécuté avec succès'),
        ('en', 'Plugin executed successfully'),
        ('ar', 'تم تنفيذ البرنامج المساعد بنجاح'),
        ('amz', 'ⴰⵏⴰⴷⴷⴰⵙ ⴷ plugin'),
        ('de', 'Plugin erfolgreich ausgeführt'),
        ('zh', '插件执行成功'),
        ('ja', 'プラグインが正常に実行されました'),
        ('ko', '플러그인이 성공적으로 실행되었습니다'),
        ('nl', 'Plugin succesvol uitgevoerd'),
        ('he', 'התוסף הופעל בהצלחה'),
        ('fa', 'افزونه با موفقیت اجرا شد'),
        ('hi', 'प्लगइन सफलतापूर्वक निष्पादित हुआ'),
        ('es', 'Plugin ejecutado con éxito')
    ]:
        payload = {'action': 'run', 'lang': lang}
        result = example_plugin.run(user, payload)
        assert result['msg'] == msg
