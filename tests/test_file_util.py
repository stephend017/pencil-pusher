from ghapd.file_util import FileUtil


def test_query_directory():
    """
    Tests that source files are queried properly
    """
    result = FileUtil.query_directory("ghapd", [".py"])

    count = 0
    for r in result:
        if "ghapd/__init__.py" in r:
            count += 1
        if "ghapd/__main__.py" in r:
            count += 1

    assert count == 2
