from . import Directory, File, Git


class Structure:
    def __init__(self):
        pass

    @staticmethod
    def make(app_name: str, app_structure: list) -> None:
        dir_name: Directory = Directory(app_name)
        file: File = File(app_name)

        for structure in app_structure:
            directory_name: str = structure.get("directory")
            if directory_name is not None:
                dir_name.create(directory_name)
                print(f"create {directory_name} directory")

            files: list = structure.get("files")
            if files is not None:
                for file_data in files:
                    file_path: str | None = None
                    if directory_name is not None:
                        file_path: str = f"{directory_name}/{file_data.get('name')}"
                    else:
                        file_path: str = file_data.get("name")
                    file.create(file_path)
                    print(f"create {file_path} file")
                    content: str | None = None
                    if file_data.get("content") is not None:
                        content = file_data.get("content")
                    else:
                        content = ""
                    file.write(file_path, content)

        # Creating instance for Git class
        git: Git = Git(app_name)
        git.init()
        git.add()
        git.commit()