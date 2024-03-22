# Import Typer class from typer module.
from typer import Typer

# Import os module
import os

# Import make_app_structure Function.
from utils import (
    make_app_structure,
    run_with_live_server
)

# Import All App structures data.
from app_structure import (
    py_app_structure,
    frontend_app_structure,
)


app = Typer()


@app.command()
def create_py_app(app_name: str):

    if not os.path.exists(os.path.join(os.getcwd(), app_name)):
        # Creating app structure using make_app_structure function.
        make_app_structure(app_name, py_app_structure)

        # Success message.
        print(f"\nYour App has been created successfully and its name is `{app_name}`.\n")
    else:
        print(f"\nOops! Your entered app name already exists. Please try another name.\n")


@app.command()
def create_js_app(app_name: str):

    if not os.path.exists(os.path.join(os.getcwd(), app_name)):
        # Creating app structure using make_app_structure function.
        make_app_structure(app_name, frontend_app_structure)

        # Success message.
        print(f"\nYour App has been created successfully and its name is `{app_name}`.\n")
        
        # Run your app with live-server.
        run_with_live_server(app_name)
    else:
        print(f"\nOops! Your entered app name already exists. Please try another name.\n")
        # Run your app with live-server.
        run_with_live_server(app_name)


# Define main entry function for run app().
def main() -> None:
    app()


if __name__ == "__main__":
    main()
