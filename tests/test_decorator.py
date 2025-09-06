import pytest
from notice_me import notice


def test_noticeme_decorator_success():
    @notice("test-job")
    def dummy():
        x = 1
        x += 1

    dummy()


def test_noticeme_decorator_error():
    @notice("test-job")
    def dummy():
        with pytest.raises(ValueError):
            raise ValueError("boom")

    dummy()
