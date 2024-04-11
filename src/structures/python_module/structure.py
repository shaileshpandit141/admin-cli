from ..code_formatter import CodeFormatter
from ..license_text import licence_text
from .templets import PythonModuleTemplets


def python_module_structure(*args, **kwargs) -> list[dict]:

    module_name: str = kwargs.get('module_name', "module").lower()

    templets: PythonModuleTemplets = PythonModuleTemplets(module_name)

    return [
        {
            "directory": "docs",
            "files": [
                {
                    "name": "index.md",
                    "content": None,
                },
            ],
        },
        {
            "directory": module_name,
            "files": [
                {
                    "name": "__init__.py",
                    "content": f"from .{module_name} import *",
                },
                {
                    "name": f"{module_name}.py",
                    "content": templets.main_py(),
                },
            ],
        },
        {
            "directory": None,
            "files": [
                {
                    "name": "LICENSE.txt",
                    "content": licence_text,
                },
                {
                    "name": "README.md",
                    "content": None,
                },
                {
                    "name": "requirements.txt",
                    "content": None,
                },
                {
                    "name": "setup.py",
                    "content": None,
                },
                {
                    "name": "test.py",
                    "content": templets.test_py(),
                },
                {
                    "name": ".gitignore",
                    "content": None,
                },
                {
                    "name": "confg.py",
                    "content": None,
                },
            ],
        },
    ]
