# Import Typer class from typer module.
from typer import Typer

# Import os module
import os

# Import All utils.
from utils import (
    Run,
    make_app_structure
)

# Import All structures functions.
from structures import (
    frontend_structure,
    python_module_structure,
    python_structure,
    flask_structure,
)


app = Typer()


def is_exist(app_name: str):
    return os.path.exists(os.path.join(os.getcwd(), app_name))


# This command is responsible for creating js-app structure.
@app.command()
def create_js_app(app_name: str):

    if not is_exist(app_name):
        # Creating app structure using make_app_structure function.
        make_app_structure(app_name, frontend_structure(app_name=app_name))

        # Success message.
        print(f"\nYour Web App has been created successfully and its name is `{app_name}`.\n")

        # Open your app in VS-Code.
        Run.open_with_vscode(app_name)
        # Run your app with live-server.
        Run.live_server(app_name)
    else:
        print(f"\nOops! Your entered app name already exists. Please try another name.\n")

        # Open your app in VS-Code.
        Run.open_with_vscode(app_name)
        # Run your app with live-server.
        Run.live_server(app_name)


# This command is responsible for creating python module structure.
@app.command()
def create_py_module(module_name: str):

    if not is_exist(module_name):
        # Creating app structure using make_app_structure function.
        make_app_structure(module_name, python_module_structure(module_name=module_name))

        # Success message.
        print(f"\nYour Python module has been created successfully and its name is `{module_name}`.\n")

        # Open your app in VS-Code.
        Run.open_with_vscode(module_name)
    else:
        print(f"\nOops! Your entered module name already exists. Please try another name.\n")

        # Open your app in VS-Code.
        Run.open_with_vscode(module_name)
        print("Exit.\n")


# This command is responsible for creating python app structure.
@app.command()
def create_py_app(app_name: str):

    if not is_exist(app_name):
        # Creating app structure using make_app_structure function.
        make_app_structure(app_name, python_structure(app_name=app_name))

        # Success message.
        print(f"\nYour Python App has been created successfully and its name is `{app_name}`.\n")

        # Open your app in VS-Code.
        Run.open_with_vscode(app_name)
    else:
        print(f"\nOops! Your entered app name already exists. Please try another name.\n")

        # Open your app in VS-Code.
        Run.open_with_vscode(app_name)
        print("Exit.\n")


# This command is responsible for creating Flask app structure.
@app.command()
def create_flask_app(app_name: str):

    if not is_exist(app_name):
        # Creating app structure using make_app_structure function.
        make_app_structure(app_name, flask_structure(app_name=app_name))

        # Success message.
        print(f"\nYour Flask App has been created successfully and its name is `{app_name}`.\n")

        # Open your app in VS-Code.
        Run.open_with_vscode(app_name)
    else:
        print(f"\nOops! Your entered flask app name already exists. Please try another name.\n")

        # Open your app in VS-Code.
        Run.open_with_vscode(app_name)
        print("Exit.\n")


# Define main entry function for run app().
def main() -> None:
    app()


if __name__ == "__main__":
    main()
