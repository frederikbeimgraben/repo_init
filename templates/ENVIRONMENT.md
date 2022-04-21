# Using the Python Environment / Installation (Anaconda)

## Prerequisites
- [Anaconda](https://www.anaconda.com/)

## Set up Environment *(from conda prompt)*
```bash
# Create a conda environment
conda create -n {{PACKAGENAME_LC}} python=3.8
# Activate the environment
conda activate {{PACKAGENAME_LC}}
# Install the required packages
conda env update --file environment.yml --prune
# (This will take a while)
```

## Add Packages to Environment
## Edit `environment.yml`
```yml
name: {{PACKAGENAME_LC}}
dependencies:
  ...
  # Add your conda packages here
  your-conda-package=your-version
  pip:
    ...
    # Add your PyPI packages here
    your-pypi-package=your-version
```

## Install changes
```bash
# Activate the environment
conda activate {{PACKAGENAME_LC}}
# Install Packages
conda env update --file environment.yml --prune
```

> For more information, consider the [conda documentation](https://conda.io/docs/user-guide/tasks/manage-environments.html).