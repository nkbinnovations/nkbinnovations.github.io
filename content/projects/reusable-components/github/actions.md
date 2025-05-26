+++
date = '2025-05-12T00:28:13Z'
+++


[![pre-commit-checks](https://github.com/nkbinnovations/reusable-actions/actions/workflows/pre-commit-checks.yaml/badge.svg)](https://github.com/nkbinnovations/reusable-actions/actions/workflows/pre-commit-checks.yaml)
[![ansible-lint](https://github.com/nkbinnovations/reusable-actions/actions/workflows/ansible-lint.yaml/badge.svg)](https://github.com/nkbinnovations/reusable-actions/actions/workflows/ansible-lint.yaml)
[![Pull Request Labeler](https://github.com/nkbinnovations/reusable-actions/actions/workflows/labeler.yaml/badge.svg)](https://github.com/nkbinnovations/reusable-actions/actions/workflows/labeler.yaml)
[![yaml-lint](https://github.com/nkbinnovations/reusable-actions/actions/workflows/yaml-lint.yaml/badge.svg)](https://github.com/nkbinnovations/reusable-actions/actions/workflows/yaml-lint.yaml)
## GitHub Actions

This repository contains several GitHub Actions workflows for linting and other automated checks. Below is a brief description of each workflow:


### ansible-lint
  * Runs the Lint on the ansible configurations to verify the syntax in the user repository

  **INPUTS**

  - **python_version:** *(optional)*

    Default Python version to use. `default('3.13.0')`

  - **ansible_requirements_file:** *(optional)*

    Relative file path of the 'requirements.yml' file in the user repository. `default('`[requirements.yml](https://github.com/nkbinnovations/reusable-actions/blob/main/.github/actions/ansible-lint/requirements.yml)'`)`

  - **ansible_directory:** *(optional)*

    Relative ansible folder path of the ansible configuration folders in the user repository. `default('${{ github.workspace }}')`

  - **ansible_lint_config:** *(optional)*

    Relative file path of the '.ansible-lint.yaml' file in the user repository. `default('`[.ansible-lint.yaml](https://github.com/nkbinnovations/reusable-actions/blob/main/.github/actions/ansible-lint/.ansible-lint.yaml)'`)`

  - **ansible_extra_args:** *(optional)*

    Extra Args to pass for the ansible-lint command line. `default('')`


  example
  ```YAML
  ansible-lint:
    name: ansible-lint
    uses: nkbinnovations/reusable-actions/.github/actions/ansible-lint.yaml@v2 # best to use the SHA instead of tags for immutable code.
    with:
      ansible_lint_config: '.ansible-lint.yaml'
  ```

### yaml-lint
  * Runs the Lint on the YAML files to verify the syntax in the user repository

  **INPUTS**

  - **python_version:** *(optional)*

    Default Python version to use. `default('3.13.0')`

  - **yamllint_config:** *(optional)*

    The YAML lint rules file for validating the configurations in the user repository. `default('`[.yamllint](https://github.com/nkbinnovations/reusable-actions/blob/main/.github/actions/yaml-lint/.yamllint)'`)`

  example
  ```YAML
  yaml-lint:
    name: python-lint
    uses: nkbinnovations/reusable-actions/.github/actions/yaml-lint.yaml@v2 # best to use the SHA instead of tags for immutable code.
    with:
      yamllint_config: '.yamllint.yml'
  ```

### pull-request-labeler
  * Creates the Labels for all the pull-request raised on the user repository

  **INPUTS**

  - **github_token:** *(optional)*

    The GitHub Token used for creating labels. `default('${{ secrets.GITHUB_TOKEN }}')`

  - **labeler_config:** *(optional)*

    The Pull Request Label rules config file for creating relevant labels for the PR in the user repository. `default('`[labeler.yaml](https://github.com/nkbinnovations/reusable-actions/blob/main/.github/actions/labeler/labeler.yaml)'`)`

  example
  ```YAML
  labeler:
    name: github-labeler
    uses: nkbinnovations/reusable-actions/.github/actions/labeler.yaml@v2 # best to use the SHA instead of tags for immutable code.
    with:
      github_token: ${{ secrets.GITHUB_TOKEN }}
      labeler_config: '.github/actions/labeler/labeler.yaml'
  ```

### pre-commit-checks
  * Runs a set of lints for the various configuration files like (Terraform, Packer, Ansible) etc. to ensure the formatting of the code committed to the user repository.
  This job enables the Pull Request reviewers to verify the code committed to the repository always follows standards.

  **INPUTS**

  - **python_version:** *(optional)*

    The Python version to use for validating the configurations in the user repository with pre-commit hooks. `default('3.13.0')`

  - **action_lint_config:** *(optional)*

    The GitHub action lint configuration file in the user repository with pre-commit hooks. `default('`[.actionlint.yaml](https://github.com/nkbinnovations/reusable-actions/blob/main/.github/actions/pre-commit/.actionlint.yaml)'`)`

  - **yamlfmt_config:** *(optional)*

    The YAML format configuration file in the user repository with pre-commit hooks. `default('`[.yamlfmt](https://github.com/nkbinnovations/reusable-actions/blob/main/.github/actions/pre-commit/.yamlfmt)'`)`

  - **yamllint_config:** *(optional)*

    The YAML Lint configuration file in the user repository with pre-commit hooks. `default('`[.yamllint](https://github.com/nkbinnovations/reusable-actions/blob/main/.github/actions/pre-commit/.yamllint)'`)`

  - **pre_commit_config:** *(optional)*

    The Pre-Commit configuration file in the user repository with pre-commit hooks. `default('`[.pre-commit-config.yaml](https://github.com/nkbinnovations/reusable-actions/blob/main/.github/actions/pre-commit/.pre-commit-config.yaml)'`)`

  example
  ```YAML
  pre-commit-checks:
    name: github-pre-commit-checks
    uses: nkbinnovations/reusable-actions/.github/actions/pre-commit-checks.yaml@v2 # best to use the SHA instead of tags for immutable code.
    with:
      python_version: '3.13.0'
  ```
