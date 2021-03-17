from ghapd.configs.manager import ConfigManager
from typing import Any
from ghapd.configs.base import ConfigParamBase
from ghapd.configs import config_manager


@config_manager.register("title_suffix")
class TitleSuffixConfigParam(ConfigParamBase):
    """
    Processes the title_suffix config parameter

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
        if "title_suffix" not in contents:
            raise ValueError("title_suffix config parameter was not defined")

        if not isinstance(contents["title_suffix"], str):
            raise ValueError(
                "title_suffix config parameter is not of type str"
            )

        return True