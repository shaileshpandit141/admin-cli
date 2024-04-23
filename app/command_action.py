import os
from modules import (
    Structure,
    Run
)
from structures import (
    frontend_structure,
    python_module_structure,
    python_structure,
    flask_structure
)


class CommandAction:
    def __init__(self) -> None:
        pass

    @staticmethod
    def is_exist(app_name: str):
        return os.path.exists(os.path.join(os.getcwd(), app_name))

    @staticmethod
    def create_py_module(module_name: str):
        if not CommandAction.is_exist(module_name):
            # Creating app structure using Structure.make function.
            Structure.make(module_name, python_module_structure(module_name=module_name))

            # Success message.
            print(f"Your Python module has been created successfully and its name is `{module_name}`.")

            # Open your app in VS-Code.
            Run.open_with_vscode(module_name)
        else:
            print("Oops! Your entered module name already exists. Please try another name.")

            # Open your app in VS-Code.
            Run.open_with_vscode(module_name)
            print("Exit.")

    @staticmethod
    def create_py_app(app_name: str):
        if not CommandAction.is_exist(app_name):
            # Creating app structure using Structure.make function.
            Structure.make(app_name, python_structure(app_name=app_name))

            # Success message.
            print(f"Your Python App has been created successfully and its name is `{app_name}`.")

            # Open your app in VS-Code.
            Run.open_with_vscode(app_name)
        else:
            print(f"Oops! Your entered app name already exists. Please try another name.")

            # Open your app in VS-Code.
            Run.open_with_vscode(app_name)
            print("Exit.")

    @staticmethod
    def create_flask_app(app_name: str):

        if not CommandAction.is_exist(app_name):
            # Creating app structure using Structure.make function.
            Structure.make(app_name, flask_structure(app_name=app_name))

            # Success message.
            print(f"Your Flask App has been created successfully and its name is `{app_name}`.")

            # Open your app in VS-Code.
            Run.open_with_vscode(app_name)
        else:
            print(f"Oops! Your entered flask app name already exists. Please try another name.")

            # Open your app in VS-Code.
            Run.open_with_vscode(app_name)
            print("Exit.")

    @staticmethod
    def create_js_app(app_name: str):

        if not CommandAction.is_exist(app_name):
            # Creating app structure using Structure.make function.
            Structure.make(app_name, frontend_structure(app_name=app_name))

            # Success message.
            print(f"Your Web App has been created successfully and its name is `{app_name}`.")

            # Open your app in VS-Code.
            Run.open_with_vscode(app_name)
            # Run your app with live-server.
            Run.live_server(app_name)
        else:
            print(f"Oops! Your entered app name already exists. Please try another name.")

            # Open your app in VS-Code.
            Run.open_with_vscode(app_name)
            # Run your app with live-server.
            Run.live_server(app_name)
