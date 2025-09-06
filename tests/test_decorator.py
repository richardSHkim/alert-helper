import pytest
from noticeme import noticeme


def test_noticeme_decorator_success():
    @noticeme("test-job")
    def dummy():
        x = 1
        x += 1

    dummy()


def test_noticeme_decorator_error():
    @noticeme("test-job")
    def dummy():
        with pytest.raises(ValueError):
            raise ValueError("boom")

    dummy()
