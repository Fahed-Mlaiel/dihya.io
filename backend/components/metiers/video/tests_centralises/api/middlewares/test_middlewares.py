from video.api.middlewares.middlewares import (
    audit_request,
    rgpd_middleware,
    accessibility_middleware,
)


def test_audit_request_decorator():
    @audit_request
    def dummy():
        return True

    assert dummy() is True


def test_rgpd_middleware_decorator():
    @rgpd_middleware
    def dummy():
        return True

    assert dummy() is True


def test_accessibility_middleware_decorator():
    @accessibility_middleware
    def dummy():
        return True

    assert dummy() is True
