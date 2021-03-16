from ghapd.configs.manager import ConfigManager
from typing import Any
from ghapd.configs.base import ConfigParamBase
from ghapd.configs import config_manager


@config_manager.register("sources")
class SourcesConfigParam(ConfigParamBase):
    """
    Processes the sources config parameter

    Note: validation only validates config name
        and config type (string array)
    """

    def on_iterate(self, data: Any):
        """
        This is the validate function
        """
        if data["type"] == ConfigManager.VALIDATE:
            self._validate(data["contents"])
            self.set_defined()

    def _validate(self, contents: dict) -> bool:
        """
        Validates the parameter is included in the
        config file since it is a required field
        """
        if "sources" not in contents:
            raise ValueError("sources config parameter was not defined")

        if not isinstance(contents["sources"], list):
            raise ValueError("source config parameter is not of type list")

        for source in contents["sources"]:
            if not isinstance(source, str):
                raise ValueError("sources path must be of type string")

        return True
