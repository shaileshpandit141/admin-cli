from typing import Any
from ..license_text import licence_text


def javascript_structure(*args, **kwargs) -> list[dict]:

    module_name: str | Any = kwargs.get("module_name")

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
                    "name": 'index.js',
                    "content": None,
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
                    "name": "webpack.config.js",
                    "content": None,
                },
                {
                    "name": "test.js",
                    "content": None,
                },
                {
                    "name": ".gitignore",
                    "content": None,
                },
            ],
        },
    ]