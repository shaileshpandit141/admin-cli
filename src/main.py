# Import Typer class from typer module.
from typer import Typer

# Import os module
import os

# Import All utils data.
from utils import (
    make_app_structure,
    run_live_server,
    py_module_structure,
    py_app_structure,
    frontend_app_structure
)


app = Typer()


# This command is responsible for creating python module structure.
@app.command()
def create_py_module(module_name: str):

    if not os.path.exists(os.path.join(os.getcwd(), module_name)):
        # Creating app structure using make_app_structure function.
        make_app_structure(module_name, py_module_structure)

        # Success message.
        print(
            f"\nYour module has been created successfully and its name is `{module_name}`.\n")
    else:
        print(
            f"\nOops! Your entered module name already exists. Please try another name.\n")


# This command is responsible for creating python app structure.
@app.command()
def create_py_app(app_name: str):

    if not os.path.exists(os.path.join(os.getcwd(), app_name)):
        # Creating app structure using make_app_structure function.
        make_app_structure(app_name, py_app_structure)

        # Success message.
        print(
            f"\nYour app has been created successfully and its name is `{app_name}`.\n")
    else:
        print(
            f"\nOops! Your entered app name already exists. Please try another name.\n")


# This command is responsible for creating js-app structure.
@app.command()
def create_js_app(app_name: str):

    if not os.path.exists(os.path.join(os.getcwd(), app_name)):
        # Creating app structure using make_app_structure function.
        make_app_structure(app_name, frontend_app_structure)

        # Success message.
        print(
            f"\nYour App has been created successfully and its name is `{app_name}`.\n")

        # Run your app with live-server.
        run_live_server(app_name)
    else:
        print(f"\nOops! Your entered app name already exists. Please try another name.\n")
        # Run your app with live-server.
        run_live_server(app_name)


# Define main entry function for run app().
def main() -> None:
    app()


if __name__ == "__main__":
    print()
    main()
