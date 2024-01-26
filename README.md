<img src='docs/images/ctf101_dark.png'>

## CTF 101

This is the official repository for CTF101 hosted at [ctf101.org](https://ctf101.org).

This branch uses [MKdocs](https://www.mkdocs.org/) and [MKdocs-Material](https://squidfunk.github.io/mkdocs-material/).

The site is maintained by the [OSIRIS Lab](https://osiris.cyber.nyu.edu/) in collaboration with [CTFd](https://ctfd.io/).

---
### Installation
1. Verify **python 3** and **python-pip** is installed. Otherwise, you can find the installation [here](https://www.python.org/downloads/).
    ```sh
    python3 --version
    pip --version
    ```

2. Clone the repository.
    ```sh
    git clone git@github.com:osirislab/ctf101.git
    cd ctf101
    ```

3. Create a virtual environment. If this step doesn't work, follow this for [**python-venv**](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/). 
    ```sh
    python3 -m venv .venv
    source .venv/bin/activate
    ```

4. Install the necessary packages.
    ```sh
    pip install -r requirements.txt
    ```

5. Run the development server.
    ```sh
    mkdocs serve
    ```