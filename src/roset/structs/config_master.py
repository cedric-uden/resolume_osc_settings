from __future__ import annotations

import abc
import typing as t

from pythonosc.osc_bundle_builder import IMMEDIATELY
from pythonosc.osc_bundle_builder import OscBundleBuilder
from pythonosc.osc_message_builder import OscMessageBuilder
from pythonosc.udp_client import SimpleUDPClient

from roset.structs.config_item import ConfigItem


class ConfigMasterAbc(abc.ABC):
    def __init__(
        self,
        client: SimpleUDPClient,
        osc_path_root: str,
    ):
        self._client = client
        self._bundle = OscBundleBuilder(IMMEDIATELY)
        self._osc_path_root = osc_path_root

    @abc.abstractmethod
    def config_items(self) -> t.List[ConfigItem]:
        raise NotImplemented

    def patch(self):
        for item in self.config_items():
            osc_msg = OscMessageBuilder(address=f"{self._osc_path_root }/{item.path}")
            osc_msg.add_arg(item.convert(item.value))
            self._bundle.add_content(osc_msg.build())

        self._client.send(self._bundle.build())
