import pytest
from alert_helper import alert


def test_noticeme_decorator_success():
    @alert("test-job")
    def dummy():
        x = 1
        x += 1

    dummy()


def test_noticeme_decorator_error():
    @alert("test-job")
    def dummy():
        with pytest.raises(ValueError):
            raise ValueError("boom")

    dummy()
