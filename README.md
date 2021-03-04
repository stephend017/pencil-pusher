# ghapd
ghapd (Github Automated Python Documenter): A Github Action that creates and publishes source documentation to the repository's wiki.

# Tech Stack
- :whale: docker
- python
- [pydoc-markdown](https://pydoc-markdown.readthedocs.io/en/latest/)

# Inputs

| Input Name            | Type     | Required | Default                 | Description                                                                                                                                                             |
|-----------------------|----------|----------|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| owner_name            | `string` | `true`   | `None`                  | The username of the repository owner                                                                                                                                    |
| repository_name       | `string` | `true`   | `None`                  | The name of the repository being accessed                                                                                                                               |
| personal_access_token | `string` | `true`   | `None`                  | A [github personal access token](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token) with full repository permissions checked. |
| config_file           | `string` | `false`  | `"./ghapd.config.json"` | This is the location of the config file. The config file is where you define which source files should be documented and how they should map to individual wiki pages.  |

# Config File
This action requires that the calling repository define a file called `ghapd.config.json` where the auto doc generator can process which source files to document and how to map those source files to wiki pages. 

Here is the format
```json
{
  "sources": [
    "mypackage/mymodule1/myfile1.py",
    "mypackage/mymodule2/"
  ],
  "title_prefix": "MyPackage",
  "title_suffix": "API",
  "titles": [
    {
      "source_file": "mypackage/mymodule1/myfile1.py",
      "title": "Utilities",
      "use_prefix": true,
      "use_suffix": false
    }
  ]
}

```

Notes:
- only files defined in the `sources` array will be processed
- `sources` can be both files or directories
- all items in `sources` should be valid paths relative to the root path of the repo
- `title_prefix` is appended to the beginning of every md file generated (same for appending `title_suffix` to end)
- only files with different title names should be defined in the `titles` array.
