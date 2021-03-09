from ghapd.documenter import Documenter


def test_gen_local():
    """
    Tests generating a doc with a
    local file
    """
    Documenter.generate("ghapd.documenter", "test")
