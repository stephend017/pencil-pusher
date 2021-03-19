from setuptools import setup, find_packages


with open("README.md", "r") as file:
    readme = file.read()


setup(
    name="pencil_pusher",
    version="0.0.2",
    description="A python package that compiles source documentation and publishes it to the repo wiki",
    long_description=readme,
    author="Stephen Davis",
    author_email="stephenedavis17@gmail.com",
    packages=find_packages(),
)
