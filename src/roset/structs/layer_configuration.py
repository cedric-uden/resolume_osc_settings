from __future__ import annotations

import typing as t

from pythonosc.osc_bundle_builder import IMMEDIATELY
from pythonosc.osc_bundle_builder import OscBundleBuilder
from pythonosc.osc_message_builder import OscMessageBuilder
from pythonosc.udp_client import SimpleUDPClient

from src.roset.consts.resolume import PlayDirection
from src.roset.consts.resolume import Transition
from src.roset.util.convert import duration_seconds_to_float


class LayerConfiguration:
    def __init__(
        self,
        client: SimpleUDPClient,
        layer_id: int,
        video_opacity: float = 1.0,
        audio_level: float = 1.0,
        master_fader: float = 1.0,
        transition_duration: float = 0.0,
        transition_type: Transition = Transition.ALPHA,
        transport_playdirection: PlayDirection = PlayDirection.PLAY,
    ):
        self._client = client
        self.layer_id = layer_id
        self.video_opacity = video_opacity
        self.audio_level = audio_level
        self.master_fader = master_fader
        self.transition_duration = transition_duration
        self.transition_type = transition_type
        self.transport_playdirection = transport_playdirection
        self._bundle = OscBundleBuilder(IMMEDIATELY)

    def patch(self):
        self._bundle.add_content(self._command_video_opacity())
        self._bundle.add_content(self._command_audio_level())
        self._bundle.add_content(self._command_master_fader())
        self._bundle.add_content(self._command_transition_type())
        self._bundle.add_content(self._command_transition_duration())
        self._bundle.add_content(self._command_set_to_play())

        self._client.send(self._bundle.build())

    def _command_video_opacity(self):
        osc_msg = OscMessageBuilder(address=f"/composition/layers/{self.layer_id}/video/opacity")
        osc_msg.add_arg(float(self.video_opacity))
        return osc_msg.build()

    def _command_master_fader(self):
        osc_msg = OscMessageBuilder(address=f"/composition/layers/{self.layer_id}/master")
        osc_msg.add_arg(float(self.master_fader))
        return osc_msg.build()

    def _command_audio_level(self):
        osc_msg = OscMessageBuilder(address=f"/composition/layers/{self.layer_id}/audio/volume")
        osc_msg.add_arg(float(self.audio_level))
        return osc_msg.build()

    def _command_transition_duration(self):
        osc_msg = OscMessageBuilder(
            address=f"/composition/layers/{self.layer_id}/transition/duration"
        )
        osc_msg.add_arg(duration_seconds_to_float(self.transition_duration))
        return osc_msg.build()

    def _command_transition_type(self):
        osc_msg = OscMessageBuilder(
            address=f"/composition/layers/{self.layer_id}/video/transition/mixer/blendmode"
        )
        osc_msg.add_arg(self.transition_type.value)
        return osc_msg.build()

    def _command_set_to_play(self):
        osc_msg = OscMessageBuilder(
            address=(
                f"/composition/layers/{self.layer_id}"
                f"/clips/*/transport/position/behaviour/playdirection"
            )
        )
        osc_msg.add_arg(self.transport_playdirection.value)
        return osc_msg.build()
