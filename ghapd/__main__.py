from ghapd.documenter import Documenter
from ghapd.input import InputManager
from ghapd.github_api import GithubAPI
from ghapd.repo_manager import RepoManager


def main():
    im = InputManager()
    im.define()
    response = im.validate()

    if not response[0]:
        raise ValueError(response[1])

    Documenter.install()

    gh = GithubAPI(im.get("personal_access_token"))

    rm = RepoManager(im.get("owner_name"), im.get("repository_name"), gh)
    rm.setup()
    rm.install()
    # only support default for now (repo_name = package_name)
    rm.document()
    rm.publish()
    rm.cleanup()


if __name__ == "__main__":
    main()
