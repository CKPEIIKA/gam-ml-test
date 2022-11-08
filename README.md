# Installation Guide

Installation guide via built-in `venv` package.

1) Install Python 3.10 for yor system: [Download](https://www.python.org/downloads/release/python-3108/).
    - Make sure your system meets all the requirements (for Windows users: Win8 and higher).
    - Make sure to toggle "Add to PATH" checkbox in the installation menu if you have some.
    - **(Optional)** Delete other Python versions installed on your system or make sure to launch Jupyter via Python 3.10.

1) Pull the repository to your local machine.
    - **(Git installed)** `git clone https://github.com/quantum-entangled/gam-ml-test.git`.
    - **(Git not installed)** [Git Installation Guide](https://github.com/git-guides/install-git) / [Git Bash](https://git-scm.com/downloads).
    - **(Git not installed and you don't want to do that)** Just download the ZIP-folder with source code via green Code button in the upper right corner of the page.

1) Open your terminal/cmd (not `conda` or similar, just system built-in) and `cd` to the repository directory on your machine. Useful guide if your not familiar with `cd`: [Video](https://www.youtube.com/watch?v=KNjzcJhUwuA).

1) Via the same terminal/cmd type: `python -m venv venv`.
    - **(If `(venv)` badge has not appeared)** Type `venv/Scripts/activate.bat` or `venv/Scripts/activate`.
    - **(If `(venv)` badge has appeared)** Your virtual environment has been activated.

1) Type `pip install -r requirements.txt`. Wait for the installation.

1) Type `jupyter notebook src/main.ipynb`.

1) Activate `venv` and run last step every time you start the app.

You're good to go if you haven't missed any steps or points. You can do the same using `conda` or similar virtualizers if you are familiar with them.
