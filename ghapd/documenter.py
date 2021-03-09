import subprocess
import logging

logger = logging.getLogger("documenter")
logger.addHandler(logging.FileHandler("documenter.log"))
logger.setLevel(logging.INFO)


class Documenter:
    @staticmethod
    def generate(module: str, title: str = "", output_dir: str = "./"):
        """
        Generates markdown documentation for a given
        module (.py file) and creates a file with the
        name title as the documentation output
        """
        options = "{renderer: {type: markdown,descriptive_class_title: false,render_toc: true}}"
        fp = open(f"{output_dir}{title}.md", "w")
        subprocess.Popen(
            ["pydoc-markdown", "-m", f"{module}", options],
            stdout=fp,
            stderr=subprocess.PIPE,
        )
        fp.close()
