# Building Fullstack Apps with FastAPI

## Setup
1. Install a version of Python>=3.10 from [python.org](https://www.python.org/downloads/) or using your OS package manager
   - Make sure the commands `python` and `pip` work in the command line/terminal
   - If the commands don't work, make sure you've [added them to the path](https://realpython.com/add-python-to-path/)
   - If python was installed using a package manager, it might be called `python3` or `pip3`
2. Clone this repository
   - Install [Git](https://git-scm.com/)
   - Open a terminal when the repository folder should be saved
   - Run `git clone https://github.com/JadeMaveric/fullstack-fastapi-tutorial`
3. Install an IDE/Text Editor
   - [VSCode](https://code.visualstudio.com/) with [Python Extension](https://code.visualstudio.com/docs/languages/python)
   - or [Pycharm Community Edition](https://www.jetbrains.com/pycharm/)
4. Open the cloned directory in cmd/terminal `python -m venv venv`
5. Activate the virtual environment
   - Linux/MacOS: `. ./venv/bin/activate`
   - Windows: `.\venv\Scripts\activate`
6. Install the dependencies `pip install -r requirements.txt`
7. To test that it's working
    - Start the server
      - Linux/MacOS: `./start.sh`
      - Windows: `.\start.bat`
    - Wait until the log prints `INFO:  Application startup complete.`
    - Using a browser visit the [Homepage](http://localhost:7000/) or the [API Docs](http://localhost:7000/docs)
