# python-package-template
A template repository for python packages

# Inputs

### `owner_name`

**type: `string`**

**required: `true`**

This is the username of the repository owner

### `repository_name`

**type: `string`**

**required: `true`**

This is the name of the repository being accessed

### `personal_access_token`

**type: `string`**

**required: `true`**

This should be an environment variable which points to a [github personal access token](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token) with full repository permissions checked.

### `config_file`

**type: `string`**

**required: `true`**

This is the location of the config file. The config file is where you define which source files should be documented and how they should map to individual wiki pages.
