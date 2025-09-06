import pytest
from alert_helper import alert


def test_noticeme_context_success():
    with alert("test-job", verbose=True):
        x = 1
        x += 1


def test_noticeme_context_error():
    with pytest.raises(ValueError):
        with alert("test-job", verbose=True):
            raise ValueError("boom")
