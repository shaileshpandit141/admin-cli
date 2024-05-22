from ..license_text import licence_text
from .templets import JavaScriptAppTemplets


def frontend_structure(*args, **kwargs) -> list[dict]:

    app_name: str = kwargs.get('app_name', "js-app").lower()

    templets: JavaScriptAppTemplets = JavaScriptAppTemplets(app_name)

    return [
        {
            "directory": "assets/icons",
            "files": [
                {
                    "name": "favicon.svg",
                    "content": templets.favicon()
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
                    "content": templets.style(),
                },
            ],
        },
        {
            "directory": "src",
            "files": [
                {
                    "name": "index.js",
                    "content": templets.script(),
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
                    "content": templets.document(),
                },
                {
                    "name": "meta.js",
                    "content": templets.mata_data(),
                },
            ],
        },
    ]
