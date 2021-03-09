"""
File for processing and validating inputs
"""
from os import environ
from typing import Any, Dict, Tuple
import yaml


class InputDefinition:
    def __init__(self, name: str, description: str, required: bool = False):
        """"""
        self._name = name
        self._description = description
        self._required = required

    @property
    def name(self) -> str:
        return self._name

    @property
    def description(self) -> str:
        return self._description

    @property
    def required(self) -> bool:
        return self._required


class InputManager:
    def __init__(self):
        """"""
        self._input_definition: Dict[str, InputDefinition] = {}

    def define(self):
        """"""
        with open("./action.yml", "r") as fp:
            definition = yaml.safe_load(fp)
            for input_name, input_definition in definition["inputs"].items():
                self._input_definition[input_name] = InputDefinition(
                    input_name,
                    input_definition["description"],
                    input_definition["required"],
                )

    def validate(self) -> Tuple[bool, str]:
        """"""
        for key, value in self._input_definition.items():
            environ_key: str = InputManager._environ_key(key)
            if environ_key not in environ:
                return False, f"Undefined input [{key}] provided"
            if value.required and (
                environ[environ_key] is not None or environ[environ_key] != ""
            ):
                return (
                    False,
                    f"Required Input [{key}] has illegal value [{environ[environ_key]}]",
                )

        return True, "Successfully validated all inputs"

    def get(self, name: str) -> Any:
        """"""
        environ_key: str = InputManager._environ_key(name)
        if environ_key not in environ:
            raise ValueError(f"Input [{name}] does not exist")

        return environ[environ_key]

    @staticmethod
    def _environ_key(name: str) -> str:
        return f"INPUT_{name.upper()}"
