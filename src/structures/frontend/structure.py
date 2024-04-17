from ..license_text import licence_text
from .templets import (
    mataData,
    document,
    style,
    script,
    favicon
)


def frontend_structure(*args, **kwargs) -> list[dict]:
    return [
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
            "directory": "assets/images",
            "files": None
        },
        {
            "directory": "css",
            "files": [
                {
                    "name": "style.css",
                    "content": style,
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
                {
                    "name": "index.html",
                    "content": document,
                },
                {
                    "name": "meta.js",
                    "content": mataData,
                },
            ],
        },
    ]
