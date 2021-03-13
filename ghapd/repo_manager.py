"""
This module contains functions for managing a repository

This includes
- cloning a repo
- cloning a repo's wiki
- installing a repo's python project

"""
from ghapd.process_util import ProcessUtil
from ghapd.file_util import FileUtil
import shutil
from ghapd.documenter import Documenter
from ghapd.github_api import GithubAPI
import logging

logger = logging.getLogger("rm")
logger.addHandler(logging.FileHandler("rm.log"))
logger.setLevel(logging.INFO)


class RepoManager:
    def __init__(self, owner: str, repo: str, github_api: GithubAPI):
        """
        """
        self._owner = owner
        self._repo = repo
        self._gh = github_api

    def setup(self):
        """
        clones both this repo and its wiki into their
        own directories
        """
        self._gh.clone_repo(self._owner, self._repo, self._repo_path)
        self._gh.clone_repo(self._owner, f"{self._repo}.wiki", self._wiki_path)

    def install(self):
        """
        installs the python project in the source repo
        using the command pip install . (from source repo)
        """
        ProcessUtil.execute(
            ["python3", "-m", "pip", "install", "."], cwd=self._repo_path
        )

    def document(self, module: str = ""):
        """
        documents all given modules in the source
        repo (using config definition) then outputs
        them to the wiki repo and commits them
        """
        if module == "":
            # use default module name (same as repo name)
            module = self._repo

        source_files = FileUtil.query_directory(
            "../" + self._repo + "/" + module, [".py"]
        )
        for sf in source_files:
            # get a relative path of the module (remove containing
            # directory and .py extension)
            module_path = sf[
                sf.index(module) + len(module) + 1
                if module == self._repo
                else 0 : -3
            ]
            # replace slashes with dots to conform
            # to python module import syntax
            module_path = module_path.replace("/", ".")
            Documenter.generate(module_path, module_path, self._wiki_path)

    def publish(self):
        """
        Publishes the generated documentation to the
        wiki repo
        """
        self._gh.full_update(
            self._owner, f"{self._repo}.wiki", self._wiki_path
        )

    def cleanup(self):
        """
        removes all files created by this object
        """
        shutil.rmtree(self._repo_path)
        shutil.rmtree(self._wiki_path)

    @property
    def _repo_path(self) -> str:
        """
        Returns the relative path of the source repo
        """
        return f"../{self._repo}"

    @property
    def _wiki_path(self) -> str:
        """
        Returns the relative path of the wiki repo
        """
        return f"../{self._repo}-wiki"
