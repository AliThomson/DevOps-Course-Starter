# DevOps Apprenticeship: Project Exercise

> If you are using GitPod for the project exercise (i.e. you cannot use your local machine) then you'll want to launch a VM using the [following link](https://gitpod.io/#https://github.com/CorndelWithSoftwire/DevOps-Course-Starter). Note this VM comes pre-setup with Python & Poetry pre-installed.

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.8+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

You can check poetry is installed by running `poetry --version` from a terminal.

**Please note that after installing poetry you may need to restart VSCode and any terminals you are running before poetry will be recognised.**

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/2.3.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

### Trello
You'll need an account on Trello: https://trello.com. Once you have this you need to create a Trello Power Up (https://trello.com/power-ups/admin). And then you can create a new API key and API Token (for the token you need to click on the "Token" link in the blurb next to your API key). These 2 values will then need to be added to your .env file. You will also need the ID of your Trello board. Once you've created one use this endpoint to find it's id: https://api.trello.com/1/members/me/boards?fields=name,url&key={yourKey}&token={yourToken}. You will also need the ids for the lists ("To Do", "Doing", "Done") on your board, which you can get using this endpoint: https://api.trello.com/1/boards/{yourBoardId}/lists?key={yourKey}&token={yourToken}&cards=open&card_fields=id,name&fields=id,name. Add these list IDs to your .env file.

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app 'todo_app/app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 113-666-066
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Testing the App
### Dependencies

You can run the tests from within VS Code by installing the pytest configuration. Click on the flask in the Activity Bar, usually found to the left. You can then run or debug individual tests using the play button in the LH margin next to it.

You can run all tests from the command line by running:

```bash
$ poetry run pytest
```

You can specify all the tests within one module by running:

```bash
$ poetry run pytest todo_app/tests/<path to file>/<filename>
```

### Adding new tests
Add your new tests into todo_app/tests. To ensure your tests are 'discovered' and run by pytest you must name the file ```test_<module_under_test>.py``` and name the individual tests ```test_<description_of_test_case>```.

If you add a new folder for your tests remember to add an empty ```__init__.py``` file to the folder
