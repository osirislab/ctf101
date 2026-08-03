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

---
### Analytics

CTF101 uses Google Analytics / GA4 for basic traffic analytics. The Measurement
ID is configured in `mkdocs.yml`, and the local initialization code lives in
`docs/js/analytics.js`.

The GA4 property is owned by an OSIRIS-controlled Google account, not by an
individual contributor. If the Measurement ID needs to change, update both the
Google tag URL in `mkdocs.yml` and the `gtag("config", "...")` value in
`docs/js/analytics.js`.

To test locally, run `mkdocs serve`, open the local site, and check the browser
developer tools Network tab for a request to `googletagmanager.com/gtag/js`.

---
### Contributing

> First off, thank you so much for contributing to CTF101's wiki repository. It's contributions from people like you who makes this page what it is. Thank you for making this page be the first step for many more security engineers!

1. Open an issue if you see something you would like to see changed!
2. Please create a branch to add/commit changes to followed with a pull request.
3. Link the relevant [**issue**](https://github.com/osirislab/ctf101/issues) in the pull request history and it'll be assigned a reviewer!
