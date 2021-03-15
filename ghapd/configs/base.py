from typing import Any
from sd_utils.plugins.plugin_base import PluginBase


class ConfigParamBase(PluginBase):
    def on_find(self, data: Any) -> Any:
        # return super().on_find(data=data)
        return data["contents"][data["name"]]
