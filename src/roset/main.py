from __future__ import annotations

import os
import time
import typing as t

from pythonosc.udp_client import SimpleUDPClient

from roset.consts.resolume import PlayDirection
from roset.consts.resolume import Transition
from roset.structs.group_configuration import GroupConfiguration
from roset.structs.layer_configuration import LayerConfiguration

if __name__ == "__main__":
    host = os.environ.get("RSLM_HOSTNAME", "127.0.0.1")
    port = int(os.environ.get("RSLM_OSC_INPUT_PORT", 7000))

    client = SimpleUDPClient(host, port)

    TOTAL_LAYERS = 3
    layers: t.Dict[int, LayerConfiguration] = {
        k + 1: LayerConfiguration(client=client, layer_id=k + 1)
        for (k, v) in enumerate(range(TOTAL_LAYERS))
    }

    layers[1].transition_type = Transition.LUMA_IS_ALPHA
    layers[2].transition_duration = 5
    layers[2].transition_type = Transition.PIP
    layers[2].transport_playdirection = PlayDirection.REVERSE

    for layer in layers.values():
        layer.patch()
        time.sleep(0.01)

    TOTAL_GROUPS = 1
    groups: t.Dict[int, GroupConfiguration] = {
        k + 1: GroupConfiguration(client=client, group_id=k + 1)
        for (k, v) in enumerate(range(TOTAL_LAYERS))
    }

    groups[1].opacity = 0.99
    groups[1].black = True

    for group in groups.values():
        group.patch()
        time.sleep(0.01)
