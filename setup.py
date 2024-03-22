from os import system


def run_command(command_name: str) -> None:
    system(command_name)


# Installing requirements.txt using pip.
run_command("pip install -r requirements.txt")
    
# Installing live-server using pip.
run_command("pip install live-server")

# Installing git using pip.
run_command("pip install python-git")
