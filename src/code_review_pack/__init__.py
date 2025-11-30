"""Code Review Pack - AI-tool-agnostic code review frameworks."""

from code_review_pack.reviewer import (
    GitError,
    review_code,
    get_staged_diff,
    get_working_diff,
    load_overlay,
    load_checklists,
)

__version__ = "0.0.1"

__all__ = [
    "__version__",
    "GitError",
    "review_code",
    "get_staged_diff",
    "get_working_diff",
    "load_overlay",
    "load_checklists",
]
