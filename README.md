# Building Fullstack Apps with FastAPI

## Setup
1. Install latest [Python (3.12 as of writing this)](https://www.python.org/)
   - Make sure the commands `python` and `pip` works from the command line/terminal
   - If the above commands are not working, make sure you [add it to the path](https://realpython.com/add-python-to-path/)
2. Clone this repository
   - Install [Git](https://git-scm.com/)
   - Run in terminal `git clone https://github.com/JadeMaveric/fullstack-fastapi-tutorial`
3. Install an IDE/Text Editor
   - [VSCode](https://code.visualstudio.com/) with [Python Extension](https://code.visualstudio.com/docs/languages/python)
   - or [Pycharm Community Edition](https://www.jetbrains.com/pycharm/)
4. Open the cloned directory in cmd/terminal `python -m venv venv`
5. Activate the virtual environment
   - Linux/MacOS: `. ./venv/bin/activate`
   - Windows: `\venv\Scripts\activate`
6. Install the dependencies `pip install -r requirements.txt`
7. To test that it's working
    - Start the server
      - Linux/MacOS: `./start.sh`
      - Windows: `\start.bat`
    - Wait until the log prints `INFO:  Application startup complete.`
    - Using a browser visit the [Homepage](http://localhost:7000/) or the [API Docs](http://localhost:7000/docs)
