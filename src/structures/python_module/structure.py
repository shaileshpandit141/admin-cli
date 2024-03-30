from typing import Any
from ..code_formatter import CodeFormatter
from ..license_text import licence_text


def python_module_structure(*args, **kwargs) -> list[dict]:

    module_name: str | Any = kwargs.get('module_name')

    main_py_content: str = f"""
    # Define class for {module_name} module.
    class {module_name.capitalize()}:
        def __init__(self) -> None:
            pass
    """

    main_py_content = CodeFormatter.format(main_py_content)

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
                    "content": f"from {module_name}.main import *",
                },
                {
                    "name": "main.py",
                    "content": main_py_content,
                },
            ],
        },
        {
            "directory": f"{module_name}/utils",
            "files": [
                {
                    "name": "__init__.py",
                    "content": None,
                }
            ],
        },
        {
            "directory": "tests",
            "files": [
                {
                    "name": "test.py",
                    "content": None,
                }
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
