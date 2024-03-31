from os import system


class Run:
    def __init__(self) -> None:
        pass

    @staticmethod
    def open_with_vscode(root_dir_name: str) -> None:
        # User input and checking for App dir open in vscode or not.
        is_run = input(":: Do you want to open it in VS-Code then press [y/n]:\n:: ")

        # Checking user input.
        if is_run.lower() == "y" or is_run.lower == "yes":
            print("The created app remains open in VS-Code.")
            system(f"code {root_dir_name} && cd ..")
            

    @staticmethod
    def live_server(app_name: str) -> None:
        # User input and checking for run created App or not.
        is_run = input(":: Do you want to run it with live-server then press [y/n]:\n:: ")

        # Checking user input.
        if is_run.lower() == "y" or is_run.lower == "yes":
            print("The app is running with live-server.")
            system(f"cd ./{app_name} && live-server && cd ..")
        else:
            print('Exit.')
