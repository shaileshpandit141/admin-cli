from typing import Any

from .default_templets import (
    license_txt,
    default_config_script,
    default_config_styles,
    default_document,
    default_styles,
    default_script,
    default_app_favicon
)


def py_module_structure(*args, **kwargs) -> list[dict]:

    module_name: str | Any = kwargs.get('module_name')

    main_py_content: str = (
    f"""# Define class for {module_name} module.
    \rclass {module_name.capitalize()}:
    def __init__(self) -> None:
        pass
    """
    )

    return [
        {
            "directory": None,
            "files": [
                {
                    "name": "LICENSE.txt",
                    "content": license_txt,
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
                    "name": "test.py",
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
            "directory": "docs",
            "files": [
                {
                    "name": "index.md",
                    "content": None,
                },
                {
                    "name": "conf.py",
                    "content": None,
                },
            ],
        },
    ]


def py_app_structure(*args, **kwargs) -> list[dict]:

    app_name: str | Any = kwargs.get('app_name')

    return [
        {
            "directory": None,
            "files": [
                {
                    "name": "LICENSE.txt",
                    "content": license_txt,
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
                    "name": "test.py",
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
            "directory": "docs",
            "files": [
                {
                    "name": "index.md",
                    "content": None,
                },
                {
                    "name": "conf.py",
                    "content": None,
                },
            ],
        },
    ]


def frontend_app_structure(*args, **kwargs) -> list[dict]:
    return [
        {
            "directory": None,
            "files": [
                {
                    "name": "LICENSE.txt",
                    "content": license_txt,
                },
                {
                    "name": "README.md",
                    "content": None,
                },
                {
                    "name": ".gitignore",
                    "content": None,
                },
            ],
        },
        {
            "directory": None,
            "files": [
                {
                    "name": "index.html",
                    "content": default_document,
                },
            ],
        },
        {
            "directory": "styles",
            "files": [
                {
                    "name": "styles.css",
                    "content": default_styles,
                },
            ],
        },
        {
            "directory": "src",
            "files": [
                {
                    "name": "index.js",
                    "content": default_script,
                },
            ],
        },
        {
            "directory": "assets",
            "files": None
        },
        {
            "directory": "assets/images",
            "files": None
        },
        {
            "directory": "assets/icons",
            "files": [
                {
                    "name": "favicon.svg",
                    "content": default_app_favicon
                },
            ]
        },
        {
            "directory": "meta",
            "files": [
                {
                    "name": "config_styles.css",
                    "content": default_config_styles
                },
                {
                    "name": "config_script.js",
                    "content": default_config_script
                },
            ]
        },
    ]
