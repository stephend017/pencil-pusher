from ghapd.configs.base import ConfigParamBase
from ghapd.configs.manager import ConfigManager
from sd_utils.plugins.plugin_collector import collect_plugins


config_manager = ConfigManager()

__all__ = collect_plugins(
    __file__, __name__, ConfigParamBase, ["base", "manager"]
)
