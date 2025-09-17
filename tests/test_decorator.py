import pytest
from alert_helper import alert
from alert_helper.types import AT, ON


DISABLE = True


def test_noticeme_decorator_success():
    for on in ON:
        for at in AT:
            @alert(f"test success on {on.value}, at {at.value}", on=on, at=at, disable=DISABLE)
            def dummy():
                pass
            dummy()


def test_noticeme_decorator_error():
    for on in ON:
        for at in AT:
            @alert(f"test error on {on.value}, at {at.value}", on=on, at=at, disable=DISABLE)
            def dummy():
                with pytest.raises(ValueError):
                    raise ValueError("boom")
            dummy()
