from __future__ import annotations

import typing as t

from pythonosc.udp_client import SimpleUDPClient

from roset.structs.config_item import ConfigItem
from roset.structs.config_master import ConfigMasterAbc


class GroupConfiguration(ConfigMasterAbc):
    def __init__(
        self,
        client: SimpleUDPClient,
        group_id: int,
        opacity: float = 1.0,
        speed: float = 0.25,
        solo: bool = False,
        black: bool = False,
    ):
        super().__init__(client, f"/composition/groups/{group_id}")
        self.opacity = opacity
        self.speed = speed
        self.solo = solo
        self.black = black

    def config_items(self) -> t.List[ConfigItem]:
        return [
            ConfigItem("master", self.opacity, float),
            ConfigItem("speed", self.speed, float),
            ConfigItem("solo", self.solo, int),
            ConfigItem("bypassed", self.black, int),
        ]
