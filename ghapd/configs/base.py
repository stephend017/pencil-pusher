from typing import Any, final
from sd_utils.plugins.plugin_base import PluginBase


class ConfigParamBase(PluginBase):
    def __init__(self):
        self._is_defined = False

    @final
    def on_find(self, data: Any) -> Any:
        # return super().on_find(data=data)
        if not self._is_defined:
            return None
        return data["contents"][data["name"]]

    def set_defined(self):
        """
        Sets this config parameter to having
        been defined.

        It is assumed that a config errors and
        is marked not valid if it is required
        but not defined
        """
        self._is_defined = True
