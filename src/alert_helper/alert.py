import traceback
from typing import Callable, Any

from .config import APP, ON
from .app import call_slack


class alert:
    def __init__(
        self,
        text: str,
        on: ON = ON.ALWAYS,
        app: APP = APP.SLACK,
        verbose: bool = False,
    ):
        self.text = text
        self.on = on
        self.app = app
        self.verbose = verbose

    # Context manager
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        if self.app is APP.SLACK:
            call_fn = call_slack
        else:
            raise NotImplementedError(
                f"Notice for {self.app.value} has not been implemented."
            )

        # replace text with traceback if exception is occurred
        if exc:
            self.text = "".join(traceback.format_exception(exc_type, exc, tb))

        if (
            self.on == ON.ALWAYS
            or (self.on == ON.SUCCESS and exc is None)
            or (self.on == ON.ERROR and exc)
        ):
            try:
                call_fn(self.text)
                if self.verbose:
                    print(f"Call {self.app.value} notification successed.")
            except Exception as e:
                if self.verbose:
                    print(f"Call {self.app.value} notification failed: {e}")
        return False

    # Decorator
    def __call__(self, func: Callable[..., Any]) -> Callable[..., Any]:
        def wrapper(*args, **kwargs):
            with self:  # context manager를 내부에서 재사용
                return func(*args, **kwargs)

        return wrapper
