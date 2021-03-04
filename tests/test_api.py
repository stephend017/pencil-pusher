import pytest
from ghapd.api import mymethod


def test_mymethod(capsys):
    """
    Tests that mymethod prints the correct string
    """
    mymethod()
    captured = capsys.readouterr()
    assert captured.out == "hello world\n"
