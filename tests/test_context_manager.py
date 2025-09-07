import pytest
from alert_helper import alert
from alert_helper.types import AT, ON


def test_noticeme_context_success():
    for on in ON:
        for at in AT:
            with alert(f"test success on {on.value}, at {at.value}", on=on, at=at):
                pass


def test_noticeme_context_error():
    for on in ON:
        for at in AT:
            with alert(f"test error on {on.value}, at {at.value}", on=on, at=at):
                with pytest.raises(ValueError):
                    with alert("test-job", verbose=True):
                        raise ValueError("boom")
