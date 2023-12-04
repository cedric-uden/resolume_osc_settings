from __future__ import annotations

import typing as t


def duration_seconds_to_float(seconds: float):
    if seconds < 0.0 or seconds > 10.0:
        raise ValueError("Duration has to be within 0 to 10 seconds")
    return seconds / 10.0
