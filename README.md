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

## Setting up the Mongo DB database
The items are stored in a Mongo DB database. You'll need an account and a database.

Once you have these you'll need to update the .env file with the database connection string. 

NB: By default all user data in MongoDB  is encrypted at rest, with no controls available to change this.

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

## Deploying the application
### Azure
The pipeline will automatically build and deploy to Azure whenever code is pushed to main. See '## Hosting the app on Azure' below.

### Ansible
You'll need: 
1. Ansible installed on a machine to act as your control node.
2. Passwordless SSH access from your control nodes to your managed nodes

All the code you need is within the ```ansible``` folder. Update the inventory with your managed node IPs and then copy the whole folder to your control node (under ```/home/user/```). From there run the following command:
```
ansible-playbook install-to-do-app.yml -i inventory
```

## Building and running the app via Docker
Make sure you're running Docker Desktop and then choose from the options below

To login to DockerHub locally you may need to use Powershell
```
docker login
```

### For local development
To run:
```bash
docker compose up
```

To build and run without docker compose:

Build with:
```bash
docker build --tag todo-app:dev --target development .
```

Test with:
```bash
docker build --tag todo-app:test --target test .
```

Run (with hotloading):
```bash
docker run --publish 8000:5000 --env-file .env --mount "type=bind,source=$(pwd)/todo_app,target=/app/todo_app" todo-app:dev
```

Run tests:
```bash
docker run todo-app:test
```

### Production
Build with: 
```bash
docker build --tag todo-app:prod --target production .
```
Run with:
```bash
docker run --publish 8000:5000 --env-file=.env todo-app:prod
```

## Hosting the app on Azure
You can see a working version here:
`https://alithowebapp.azurewebsites.net/`

To set up from scratch:
### Docker
Login to DockerHub locally (you may need to do this in PowerShell)
To login to DockerHub locally you may need to use Powershell
```
docker login
```

Build the image using
```
docker build --tag <username>/todo-app --target production .
```

Push the image using
```
docker push <username>/todo-app
```

### Azure
Create a service plan with 
```
az appservice plan create --resource-group <resource_group_name> -n <unique_service_plan_name> --sku B1 --is-linux
```

And then create the WebApp
```
az webapp create --resource-group <resource_group_name> --plan <unique_service_plan_name> --name <webapp_name> --deployment-container-image-name docker.io/<dockerhub_username>/<container-image-name>:latest
```

Set up your environment variables in your WebApp configuration. These are found inn Azure, under Settings. Add each key value air from the .env file. Additionally, add a value for `WEBSITES_PORT` of `5000`, and then save. This will restart the web app.


## Diagrams
There are architecture in the `diagrams` subfolder. These were created using [app.diagrams.net](https://app.diagrams.net/) and you can use the `draw.io` file to edit them.
