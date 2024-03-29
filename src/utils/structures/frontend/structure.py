from ..license_text import licence_text
from .templets import (
    config_styles,
    config_script,
    document,
    styles,
    script,
    favicon
)

def frontend_structure(*args, **kwargs) -> list[dict]:
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
                    "content": document,
                },
            ],
        },
        {
            "directory": "styles",
            "files": [
                {
                    "name": "styles.css",
                    "content": styles,
                },
            ],
        },
        {
            "directory": "src",
            "files": [
                {
                    "name": "index.js",
                    "content": script,
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
                    "content": favicon
                },
            ]
        },
        {
            "directory": "meta",
            "files": [
                {
                    "name": "config_styles.css",
                    "content": config_styles
                },
                {
                    "name": "config_script.js",
                    "content": config_script
                },
            ]
        },
    ]
