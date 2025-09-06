import pytest
from notice_me import notice


def test_noticeme_context_success():
    with notice("test-job", verbose=True):
        x = 1
        x += 1


def test_noticeme_context_error():
    with pytest.raises(ValueError):
        with notice("test-job", verbose=True):
            raise ValueError("boom")
