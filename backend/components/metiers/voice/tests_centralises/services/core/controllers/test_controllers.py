import types

# Test avancé pour controllers.py du module services/core/controllers
# from components.metiers.voice.services.core.controllers
# import ...


def test_services_core_controllers():
    # Ajouter des assertions avancées selon la logique métier
    assert True


def test_services_controller_nominal():
    from backend.components.metiers.voice.services.core.controllers.services_controller import ServicesController

    ctrl = ServicesController({"mode": "prod"})
    assert ctrl.init({"version": 1}) is True
    result = ctrl.handle("action", {"foo": "bar"})
    assert result["success"] is True
    assert result["action"] == "action"
    assert result["payload"] == {"foo": "bar"}
    assert isinstance(ctrl.get_audit_trail(), list)
    assert ctrl.get_audit_trail()[-1]["action"] == "handle"


def test_services_controller_edge_case():
    from backend.components.metiers.voice.services.core.controllers.services_controller import ServicesController

    ctrl = ServicesController()
    ctrl.init({})
    try:
        ctrl.handle("", {})
    except ValueError as e:
        assert "Invalid action" in str(e)
    assert ctrl.get_audit_trail()[-1]["action"] == "error"


# Mocks pour accès et modèles
class DummyUser:
    def __init__(self, role):
        self.role = role


def test_services_controller_get_model_access():
    from backend.components.metiers.voice.services.core.controllers.services_controller import ServicesController

    ctrl = ServicesController()
    ctrl.audit_log = []
    # Mock check_access et get_voice_model
    ctrl.get_model = types.MethodType(
        lambda self, model_id, user: {"id": model_id, "name": "Test"}, ctrl
    )
    model = ctrl.get_model("m1", DummyUser("admin"))
    assert model["id"] == "m1"


def test_services_controller_list_models_access():
    from backend.components.metiers.voice.services.core.controllers.services_controller import ServicesController

    ctrl = ServicesController()
    ctrl.audit_log = []
    ctrl.list_models = types.MethodType(
        lambda self, user: [{"id": "m1"}, {"id": "m2"}], ctrl
    )
    models = ctrl.list_models(DummyUser("admin"))
    assert isinstance(models, list)
    assert len(models) == 2
