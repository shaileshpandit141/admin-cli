from typing import Any
from ..license_text import licence_text

def python_structure(*args, **kwargs) -> list[dict]:

    app_name: str | Any = kwargs.get('app_name')

    return [
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
                    "name": ".gitignore",
                    "content": None,
                },
                {
                    "name": "confg.py",
                    "content": None,
                },
            ],
        },
        {
            "directory": app_name,
            "files": [
                {
                    "name": "main.py",
                    "content": None,
                },
            ],
        },
        {
            "directory": f"{app_name}/utils",
            "files": [
                {
                    "name": "__init__.py",
                    "content": None,
                },
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
            "directory": "docs",
            "files": [
                {
                    "name": "index.md",
                    "content": None,
                }
            ],
        },
    ]
