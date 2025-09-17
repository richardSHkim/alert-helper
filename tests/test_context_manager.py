import pytest
from alert_helper import alert
from alert_helper.types import AT, ON


DISABLE=True


def test_noticeme_context_success():
    for on in ON:
        for at in AT:
            with alert(f"test success on {on.value}, at {at.value}", on=on, at=at, disable=DISABLE):
                pass


def test_noticeme_context_error():
    for on in ON:
        for at in AT:
            with alert(f"test error on {on.value}, at {at.value}", on=on, at=at, disable=DISABLE):
                with pytest.raises(ValueError):
                    with alert("test-job", verbose=True, disable=DISABLE):
                        raise ValueError("boom")
