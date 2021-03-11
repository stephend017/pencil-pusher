# Table of Contents

* [ghapd.documenter](#ghapd.documenter)
  * [Documenter](#ghapd.documenter.Documenter)
    * [install](#ghapd.documenter.Documenter.install)
    * [generate](#ghapd.documenter.Documenter.generate)

<a name="ghapd.documenter"></a>
# ghapd.documenter

<a name="ghapd.documenter.Documenter"></a>
## Documenter

```python
class Documenter()
```

<a name="ghapd.documenter.Documenter.install"></a>
#### install

```python
 | @staticmethod
 | install()
```

installs the correct pydoc-markdown package
to the python version being used to execute
the commands

<a name="ghapd.documenter.Documenter.generate"></a>
#### generate

```python
 | @staticmethod
 | generate(module: str, title: str = "", output_dir: str = "./")
```

Generates markdown documentation for a given
module (.py file) and creates a file with the
name title as the documentation output
