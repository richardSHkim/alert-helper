import traceback
from typing import Callable, Any

from .config import AT, ON, APP
from .app import Slack


class alert:
    def __init__(
        self,
        text: str,
        at: AT = AT.BOTH,
        on: ON = ON.ALWAYS,
        app: APP = APP.SLACK,
        verbose: bool = False,
    ):
        self.text = text
        self.at = at
        self.on = on
        self.app = app
        self.verbose = verbose

        if self.app is APP.SLACK:
            self.caller = Slack(verbose=self.verbose)
        else:
            raise NotImplementedError(
                f"Notice for {self.app.value} has not been implemented."
            )

    # Context manager
    def __enter__(self):
        if self.at in (AT.BOTH, AT.START):
            text_start = "START: " + self.text
            self.caller(text_start)
        return self

    def __exit__(self, exc_type, exc, tb):
        if self.at in (AT.BOTH, AT.END):
            # replace text with traceback if exception is occurred
            if exc:
                text_end = "".join(traceback.format_exception(exc_type, exc, tb))
            else:
                text_end = "END: " + self.text

            if (
                self.on == ON.ALWAYS
                or (self.on == ON.SUCCESS and exc is None)
                or (self.on == ON.ERROR and exc)
            ):
                self.caller(text_end)
        return False

    # Decorator
    def __call__(self, func: Callable[..., Any]) -> Callable[..., Any]:
        def wrapper(*args, **kwargs):
            with self:  # context manager를 내부에서 재사용
                return func(*args, **kwargs)

        return wrapper
