---
description: Publish the Python package to PyPI
---

This workflow will guide you through publishing your Python package to PyPI.

## Prerequisites

1.  **PyPI Account**: You need an account on [PyPI](https://pypi.org/).
2.  **API Token**: Create an API token in your PyPI account settings.

## Steps

1.  **Install Twine**
    We need `twine` to upload the package.
    ```bash
    pip install twine
    ```

2.  **Build the Package** (If you haven't already)
    ```bash
    python -m build
    ```

3.  **Upload to PyPI**
    Run the following command. You will be prompted for your username and password.
    - **Username**: `__token__`
    - **Password**: Your PyPI API token (starts with `pypi-`)

    ```bash
    python -m twine upload dist/*
    ```

    > **Note:** If you want to test first, you can upload to [TestPyPI](https://test.pypi.org/) using:
    > `python -m twine upload --repository testpypi dist/*`

4.  **Verify**
    Visit your project page on PyPI to verify the release.
