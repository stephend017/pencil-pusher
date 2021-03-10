import subprocess
import logging

logger = logging.getLogger("documenter")
logger.addHandler(logging.FileHandler("documenter.log"))
logger.setLevel(logging.INFO)


class Documenter:
    @staticmethod
    def install():
        """
        installs the correct pydoc-markdown package
        to the python version being used to execute
        the commands
        """
        subprocess.Popen(
            ["python3", "-m", "pip", "install", "pydoc-markdown"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

    @staticmethod
    def generate(module: str, title: str = "", output_dir: str = "./"):
        """
        Generates markdown documentation for a given
        module (.py file) and creates a file with the
        name title as the documentation output
        """
        options = "{renderer: {type: markdown,descriptive_class_title: false,render_toc: true}}"

        if not output_dir.endswith("/"):
            output_dir += "/"

        fp = open(f"{output_dir}{title}.md", "w")
        subprocess.Popen(
            ["pydoc-markdown", "-m", f"{module}", options],
            stdout=fp,
            stderr=subprocess.PIPE,
        )
        fp.close()
