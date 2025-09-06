import pytest
from noticeme import noticeme


def test_noticeme_context_success():
    with noticeme("test-job", verbose=True):
        x = 1
        x += 1


def test_noticeme_context_error():
    with pytest.raises(ValueError):
        with noticeme("test-job", verbose=True):
            raise ValueError("boom")
