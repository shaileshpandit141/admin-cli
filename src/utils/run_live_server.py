from os import system


def run_live_server(app_name: str) -> None:
    # User input and checking for runn created App or not.
    is_run = input(
        ":: Do you want to run it with live-server then press [y/n]:\n:: ")
    print()

    # Checking user input.
    if is_run.lower() == "y" or is_run.lower == "yes":
        print("Now that the App is running with live-server.\n")
        system(f"cd ./{app_name} && live-server && cd ..")
    else:
        print('Exit.\n')
