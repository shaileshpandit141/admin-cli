# Importing mknod, and getcwd method from os built-in module.
from os import (
    mknod,
    getcwd
)

# Importing exists, and join methods from os.path built-in module.
from os.path import (
    exists,
    join
)


# Define a File clsss.
class File:
    def __init__(self, app_name: str) -> None:
        self.root_dir = join(getcwd(), app_name)

    def get_absolute_path(self, relative_path_name: str) -> str:
        return join(self.root_dir, relative_path_name)
    
    def exists(self, file_path: str) -> bool:
        is_exit = exists(self.get_absolute_path(file_path))
        return is_exit
    
    def create(self, file_path: str) -> None:
        if not self.exists(self.get_absolute_path(file_path)):
            mknod(self.get_absolute_path(file_path))

    def write(self, file_path: str, default_data: str="") -> None:
        with open(self.get_absolute_path(file_path), "w+") as file:
            file.write(default_data)


# Define main entry function for module testing.
def main() -> None:
    file: File = File("test_app")
    file.create("src/test.py")
    file.write("src/test.py", "print('Hello, Python')")


if __name__ == "__main__":
    main()
