from github import Github 
import re
import os


gh = Github(g_github_token)
repo = gh.get_repo("stephend017/pencil-pusher")

dockerfile_meta = repo.get_contents("Dockerfile")
dockerfile = str(dockerfile_meta.decoded_content, 'utf-8')
dockerfile_sha = dockerfile_meta.sha

setup_file = str(repo.get_contents("setup.py").decoded_content, 'utf-8')


old_version = re.search(r"\d+\.\d+\.\d+", dockerfile).group()
new_version = re.search(r'\d+\.\d+\.\d+', setup_file).group()

dockerfile = dockerfile.replace(old_version, new_version)
repo.update_file("Dockerfile", "Updated version", dockerfile, dockerfile_sha)
