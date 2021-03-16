import pytest
from ghapd.configs import config_manager


def test_valid():
    """
    """
    config_manager.load_config_file(
        "./tests/test_configs/test_sources/sources01.config.json"
    )
    config_manager.validate()


def test_invalid_type():
    """
    """
    config_manager.load_config_file(
        "./tests/test_configs/test_sources/sources02.config.json"
    )
    with pytest.raises(ValueError):
        config_manager.validate()


def test_invalid_element_type():
    """
    """
    config_manager.load_config_file(
        "./tests/test_configs/test_sources/sources03.config.json"
    )
    with pytest.raises(ValueError):
        config_manager.validate()


def test_invalid_name():
    """
    """
    config_manager.load_config_file(
        "./tests/test_configs/test_sources/sources04.config.json"
    )
    with pytest.raises(ValueError):
        config_manager.validate()
