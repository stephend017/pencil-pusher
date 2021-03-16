import pytest
from ghapd.configs import config_manager


def test_valid():
    """
    Tests that a valid config file does not throw
    any errors when validated
    """
    config_manager.load_config_file(
        "./tests/test_configs/test_sources/sources01.config.json"
    )
    config_manager.validate()


def test_invalid_type():
    """
    tests that a config file with an invalid type
    for sources throws an error
    """
    config_manager.load_config_file(
        "./tests/test_configs/test_sources/sources02.config.json"
    )
    with pytest.raises(ValueError):
        config_manager.validate()


def test_invalid_element_type():
    """
    tests that a complex type with an invalid
    element type throws an error
    """
    config_manager.load_config_file(
        "./tests/test_configs/test_sources/sources03.config.json"
    )
    with pytest.raises(ValueError):
        config_manager.validate()


def test_invalid_name():
    """
    tests that a missing config parameter that is required
    throws an error
    """
    config_manager.load_config_file(
        "./tests/test_configs/test_sources/sources04.config.json"
    )
    with pytest.raises(ValueError):
        config_manager.validate()


def test_get_values():
    """
    tests that config values are loaded properly
    """
    expected = [
        "path1/*",
        "path1/anotherpath/*",
        "path1/anotherpath2/",
        "path1/anotherpath2/file1.py",
    ]

    config_manager.load_config_file(
        "./tests/test_configs/test_sources/sources01.config.json"
    )
    config_manager.validate()
    response = config_manager.get("sources")
    assert len(expected) == len(response)
    for path in expected:
        assert path in response
