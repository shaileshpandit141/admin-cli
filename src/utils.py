from os import system
from modules.directory import Directory
from modules.file import File


def make_app_structure(app_name: str, app_structure: list) -> None:
    dir: Directory = Directory(app_name)
    file: File = File(app_name)

    for structure in app_structure:
        directory_name: str = structure.get("directory")
        if directory_name is not None:
            dir.create(directory_name)

        files: list = structure.get("files")
        if files is not None:
            for file_data in files:
                file_path: str = f"{directory_name}/{file_data.get('name')}" if directory_name is not None else file_data.get("name")
                file.create(file_path)
                content = file_data.get("content") if file_data.get("content") is not None else ""
                file.write(file_path, content)


def run_with_live_server(app_name: str) -> None:
    # User input and checking for runn created App or not.
    is_run = input(":: Do you want to run it with live-server then press [y/n]:\n:: ")
    print()

    # Checking user input.
    if is_run.lower() == "y" or is_run.lower == "yes":
        print("Now that the App is running with live-server.\n")
        system(f"cd ./{app_name} && live-server && cd ..")
    else:
        print('Exit.\n')
