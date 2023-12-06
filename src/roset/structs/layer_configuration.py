from __future__ import annotations

import typing as t

from pythonosc.udp_client import SimpleUDPClient

from roset.consts.resolume import PlayDirection
from roset.consts.resolume import Transition
from roset.structs.config_item import ConfigItem
from roset.structs.config_master import ConfigMasterAbc
from roset.util.convert import duration_seconds_to_float


class LayerConfiguration(ConfigMasterAbc):
    def __init__(
        self,
        client: SimpleUDPClient,
        layer_id: int,
        video_opacity: float = 1.0,
        audio_level: float = 1.0,
        master_fader: float = 1.0,
        speed: float = 0.25,
        black: bool = False,
        solo: bool = False,
        transition_duration: float = 0.0,
        transition_type: Transition = Transition.ALPHA,
        transport_playdirection: PlayDirection = PlayDirection.PLAY,
    ):
        super().__init__(client=client, osc_path_root=f"/composition/layers/{layer_id}")
        self.video_opacity = video_opacity
        self.audio_level = audio_level
        self.master_fader = master_fader
        self.speed = speed
        self.black = black
        self.solo = solo
        self.transition_duration = transition_duration
        self.transition_type = transition_type
        self.transport_playdir = transport_playdirection

    def config_items(self) -> t.List[ConfigItem]:
        return [
            ConfigItem("video/opacity", self.video_opacity, float),
            ConfigItem("audio/volume", self.audio_level, float),
            ConfigItem("master", self.master_fader, float),
            ConfigItem("speed", self.speed, float),
            ConfigItem("bypassed", self.black, int),
            ConfigItem("solo", self.solo, int),
            ConfigItem("clips/*/transport/position/behaviour/speed", self.speed, float),
            ConfigItem("transition/duration", self.transition_duration, duration_seconds_to_float),
            ConfigItem("video/transition/mixer/blendmode", self.transition_type.value),
            ConfigItem(
                "clips/*/transport/position/behaviour/playdirection", self.transport_playdir.value
            ),
        ]
