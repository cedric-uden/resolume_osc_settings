from __future__ import annotations

import typing as t
from dataclasses import dataclass


@dataclass
class ConfigItem:
    path: str
    value: t.Any
    convert: t.Callable = lambda x: x
