from ghapd.github_api import GithubAPI
import os
import time
import shutil

REPO = "ghapd"
OWNER = "stephend017"
ROOT_DIR = os.path.dirname(os.path.abspath("./setup.py"))


def test_get_public_file():
    """
    Tests that a public file can be successfully queried from
    a public repository
    """
    file_path = "action.yml"

    contents = GithubAPI.get_public_file(OWNER, REPO, file_path)

    assert 'name: "ghapd"' in contents


def test_clone_repo():
    """
    Tests that a repo can be cloned successfully to a
    local location
    """
    ghapi = GithubAPI()
    ghapi.clone_repo(OWNER, REPO, "example-repo")
    path = os.path.join(ROOT_DIR, "example-repo")

    # python is slow and will not recognize the new directory right away
    time.sleep(1)

    print(path)
    assert os.path.exists(path)
    shutil.rmtree(path)
    time.sleep(1)


def test_clone_repo_external():
    """
    Tests that a repo can be cloned successfully to a
    local location that is outside of the executing directory

    This is needed so the wiki repo and the source repo can be
    used in tandem without having to deal with git potentially
    interacting with both of them
    """
    ghapi = GithubAPI()
    ghapi.clone_repo(OWNER, REPO, "../example-repo")
    path = os.path.join(ROOT_DIR, "../example-repo")

    # python is slow and will not recognize the new directory right away
    time.sleep(1)

    assert os.path.exists(path)
    shutil.rmtree(path)
    time.sleep(1)


def test_full_send():
    """
    Tests that a repo can be automatically staged, committed and
    pushed
    """
    ghapi = GithubAPI(os.environ["GH_PAT"])
    ghapi.clone_repo(OWNER, "ghapd.wiki", "../example-repo")
    path = os.path.join(ROOT_DIR, "../example-repo")

    # python is slow and will not recognize the new directory right away
    time.sleep(1)

    # do a change
    with open(os.path.join(path, "Home.md"), "a+") as fp:
        fp.write("* testing string \n\n")

    ghapi.full_update(OWNER, "ghapd.wiki", path)

    time.sleep(1)
    shutil.rmtree(path)
    time.sleep(1)
