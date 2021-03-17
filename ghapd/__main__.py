from ghapd.documenter import Documenter
from ghapd.input import InputManager
from ghapd.github_api import GithubAPI
from ghapd.repo_manager import RepoManager
from ghapd.configs import config_manager


def main():
    im = InputManager()
    im.define()
    response = im.validate()

    if not response[0]:
        raise ValueError(response[1])

    Documenter.install()

    gh = GithubAPI(im.get("personal_access_token"))

    owner_name = im.get("owner_name")
    repository_name = im.get("repository_name")

    rm = RepoManager(owner_name, repository_name, gh)
    rm.setup()
    rm.install()

    # load configs for the given file
    config_manager.load_config_file(f'{rm._repo_path}/{im.get("config_file")}')
    config_manager.validate()

    # transform titles config into usable dict
    titles = {}
    for element in config_manager.get("titles"):
        if element["source"].endswith(".py"):
            titles[element["source"][:-3]] = element["title"]
        else:
            titles[element["source"]] = element["title"]

    # only support default for now (repo_name = package_name)
    rm.document(
        sources=config_manager.get("sources"),
        title_prefix=config_manager.get("title_prefix"),
        title_suffix=config_manager.get("title_suffix"),
        titles=titles,
    )

    rm.publish()
    rm.cleanup()


if __name__ == "__main__":
    main()
