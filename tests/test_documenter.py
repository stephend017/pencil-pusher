from ghapd.documenter import Documenter
import os


def test_gen_local():
    """
    Tests generating a doc with a
    local file
    """
    Documenter.generate("ghapd.documenter", "test")
    assert os.path.isfile("./test.md")
    os.remove("./test.md")
