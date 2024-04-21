from os import system


class Git:
    def __init__(self, app_name) -> None:
        self.app_name = app_name

    def init(self) -> None:
        system(f"cd ./{self.app_name} && git init && cd ..")

    def add(self) -> None:
        system(f"cd ./{self.app_name} && git add . && cd ..")

    def commit(self) -> None:
        system(f"cd ./{self.app_name} && git branch -M main && git commit -m 'Initial setup is done using the Admin-CLI.' && cd ..")
