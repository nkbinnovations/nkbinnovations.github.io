+++
date = '2025-05-12T00:15:40Z'
+++


[![github-pre-commit-checks](https://github.com/nkbinnovations/reusable-workflows/actions/workflows/github-pre-commit-checks.yaml/badge.svg)](https://github.com/nkbinnovations/reusable-workflows/actions/workflows/github-pre-commit-checks.yaml)
[![github-action-lint](https://github.com/nkbinnovations/reusable-workflows/actions/workflows/github-action-lint.yaml/badge.svg)](https://github.com/nkbinnovations/reusable-workflows/actions/workflows/github-action-lint.yaml)
[![github-ansible-lint](https://github.com/nkbinnovations/reusable-workflows/actions/workflows/github-ansible-lint.yaml/badge.svg)](https://github.com/nkbinnovations/reusable-workflows/actions/workflows/github-ansible-lint.yaml)
[![github-packer-lint](https://github.com/nkbinnovations/reusable-workflows/actions/workflows/github-packer-lint.yaml/badge.svg)](https://github.com/nkbinnovations/reusable-workflows/actions/workflows/github-packer-lint.yaml)
[![github-packer-lint](https://github.com/nkbinnovations/reusable-workflows/actions/workflows/github-packer-lint.yaml/badge.svg)](https://github.com/nkbinnovations/reusable-workflows/actions/workflows/github-packer-lint.yaml)
[![github-terraform-lint](https://github.com/nkbinnovations/reusable-workflows/actions/workflows/github-terraform-lint.yaml/badge.svg)](https://github.com/nkbinnovations/reusable-workflows/actions/workflows/github-terraform-lint.yaml)
[![github-labeler](https://github.com/nkbinnovations/reusable-workflows/actions/workflows/github-labeler.yaml/badge.svg)](https://github.com/nkbinnovations/reusable-workflows/actions/workflows/github-labeler.yaml)
[![github-yaml-lint](https://github.com/nkbinnovations/reusable-workflows/actions/workflows/github-yaml-lint.yaml/badge.svg)](https://github.com/nkbinnovations/reusable-workflows/actions/workflows/github-yaml-lint.yaml)
[![github-terraform-deploy](https://github.com/nkbinnovations/reusable-workflows/actions/workflows/github-terraform-deploy.yaml/badge.svg)](https://github.com/nkbinnovations/reusable-workflows/actions/workflows/github-terraform-deploy.yaml)
[![github-packer-deploy](https://github.com/nkbinnovations/reusable-workflows/actions/workflows/github-packer-deploy.yaml/badge.svg)](https://github.com/nkbinnovations/reusable-workflows/actions/workflows/github-packer-deploy.yaml)
[![github-ansible-deploy](https://github.com/nkbinnovations/reusable-workflows/actions/workflows/github-ansible-deploy.yaml/badge.svg)](https://github.com/nkbinnovations/reusable-workflows/actions/workflows/github-ansible-deploy.yaml)

## Workflows

This repository contains several GitHub Actions workflows for linting and other automated checks. Below is a brief description of each workflow:

### github-packer-lint
  * Runs the Lint on the packer configurations to verify the syntax in the user repository

  **INPUTS**

  - **packer_version:** *(optional)*

    The Packer version to use for validating the configurations in the user repository. `default('latest')`

  - **packer_directory:** *(optional)*

    Relative packer folder path of the ansible configuration folders in the user repository. `default('packer')`

  example
  ```YAML
  github-packer-lint:
    name: packer-lint
    uses: nkbinnovations/reusable-workflows/.github/workflows/github-packer-lint.yaml@v2 # best to use the SHA instead of tags for immutable code.
  ```

### github-terraform-lint
  * Runs the Lint on the terraform configurations to verify the syntax in the user repository

  **INPUTS**

  - **terraform_version:** *(optional)*

    The Terraform version to use for validating the configurations in the user repository. `default('latest')`

  - **terraform_directory:** *(optional)*

    Relative Terraform folder path of the configuration files in the user repository. `default('terraform')`

  example
  ```YAML
  github-terraform-lint:
    name: terraform-lint
    uses: nkbinnovations/reusable-workflows/.github/workflows/github-terraform-lint.yaml@v2 # best to use the SHA instead of tags for immutable code.
    with:
      terraform_version: '1.10.3'
  ```

### github-python-lint
  * Runs the Lint on the packer configurations to verify the syntax in the user repository

  **INPUTS**

  - **python_version:** *(optional)*

    The Python version to use for validating the configurations in the user repository. `default('3.13.0')`

  example
  ```YAML
  github-python-lint:
    name: python-lint
    uses: nkbinnovations/reusable-workflows/.github/workflows/github-python-lint.yaml@v2 # best to use the SHA instead of tags for immutable code.
    with:
      python_version: '3.13.0'
  ```

### github-terraform-deploy
  * Deploys the terraform configurations to verify the syntax in the user repository

  **INPUTS**

  - **terraform_environment:** *(optional)*

    The Terraform Environment to apply/plan the configurations in the user repository.

    **Note:**
      - The Variables should be either created directly or under "tfvars" directory of the Terraform directory Variable.

    **Ex:**
      - dev.tfvars
      - tfvars/dev.tfvars

  - **terraform_version:** *(optional)*

    The Terraform version to use for validating the configurations in the user repository. `default('latest')`

  - **terraform_directory:** *(optional)*

    Relative Terraform folder path of the configuration folders in the user repository. `default('terraform')`

  - **terraform_action:** *(optional)*

    The Terraform action to apply on the terraform configuration files in the user repository. `default('plan')`

  example
  ```YAML
  github-terraform-deploy:
    name: terraform-deploy
    uses: nkbinnovations/reusable-workflows/.github/workflows/github-terraform-deploy.yaml@v2 # best to use the SHA instead of tags for immutable code.
    with:
      terraform_version: '1.10.3'
      terraform_environment: 'dev'
  ```

### github-packer-deploy
  * Deploys the packer configurations to verify the syntax in the user repository

   **Note:**
     - This workflow works only for HCL2 Packer templates.

  **INPUTS**

  - **packer_environment:** *(optional)*

    The Packer Environment to inspect/build the configurations in the user repository.

    **Note:**
      - The Variables should be either created directly or under "pkrvars" directory of the Packer directory Variable.

    **Ex:**
      - dev.pkrvars.hcl
      - tfvars/dev.pkrvars.hcl

  - **packer_version:** *(optional)*

    The Packer version to use for validating the configurations in the user repository. `default('latest')`

  - **packer_directory:** *(optional)*

    Relative Packer folder path of the configuration folders in the user repository. `default('packer')`

  - **packer_action:** *(optional)*

    The Packer action to apply on the packer configuration files in the user repository. `default('inspect')`

  example
  ```YAML
  github-packer-deploy:
    name: packer-deploy
    uses: nkbinnovations/reusable-workflows/.github/workflows/github-packer-deploy.yaml@v2 # best to use the SHA instead of tags for immutable code.
    with:
      packer_version: '1.8.3'
      packer_action: 'inspect'
  ```

### github-ansible-deploy
  * Deploys the ansible configurations to verify the syntax in the user repository

  **INPUTS**

  - **ansible_version:** *(optional)*

    The Ansible version to use for validating the configurations in the user repository. `default('2.18.0')`

  - **ansible_directory:** *(optional)*

    The Relative Directory path for the ansible configurations in the user repository. `default('ansible')`

  - **ansible_requirements_file:** *(optional)*

    Relative path of the ansible-galaxy dependencies configuration file in the user repository. `default('ansible/requirements.yml')`

  - **ansible_inventory_file:** *(optional)*

    Relative path of the ansible inventory file in the user repository. `default('ansible/inventory.yml')`

  - **ansible_playbook_file:** *(optional)*

    Relative path of the ansible playbook file in the user repository. `default('ansible/sample-playbook.yml')`

  **SECRETS**

  - **ansible_user:** *(required)*

    The User for running the Ansible Configurations in the user repository.

  - **ansible_private_key_path:** *(required)*

    The User private key to connect to target servers for running the Ansible Configurations in the user repository.

  example
  ```YAML
  github-ansible-deploy:
    name: ansible-deploy
    uses: nkbinnovations/reusable-workflows/.github/workflows/github-ansible-deploy.yaml@v2 # best to use the SHA instead of tags for immutable code.
    secrets:
      ansible_version: "${USER}"
      ansible_private_key_path: "${HOME}/.ssh/private_key.pem"
  ```
