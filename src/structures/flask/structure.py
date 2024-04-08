from ..license_text import licence_text


def flask_structure(*args, **kwargs) -> list[dict]:
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
            "directory": "src",
            "files": [
                {
                    "name": "__init__.py",
                    "content": None,
                },
                {
                    "name": "views.py",
                    "content": None,
                },
                {
                    "name": "models.py",
                    "content": None,
                },
                {
                    "name": "forms.py",
                    "content": None,
                },
            ],
        },
        {
            "directory": "src/static/css",
            "files": [
                {
                    "name": "style.css",
                    "content": None,
                },
                {
                    "name": "base.css",
                    "content": None,
                },
            ],
        },
        {
            "directory": "src/static/images",
            "files": None,
        },
        {
            "directory": "src/static/icons",
            "files": None,
        },
        {
            "directory": "src/static/js",
            "files": [
                {
                    "name": "script.js",
                    "content": None
                },
            ],
        },
        {
            "directory": "src/templates",
            "files": [
                {
                    "name": "base.html",
                    "content": None
                },
            ],
        },
        {
            "directory": "src/templates/includes",
            "files": [
                {
                    "name": "header.html",
                    "content": None
                },
                {
                    "name": "footer.html",
                    "content": None
                },
            ],
        },
        {
            "directory": "src/templates/layoutes",
            "files": [
                {
                    "name": "main-layout.html",
                    "content": None
                },
            ],
        },
        {
            "directory": "src/templates/pages",
            "files": [
                {
                    "name": "home.html",
                    "content": None
                },
            ],
        },
        {
            "directory": "src/utils",
            "files": [
                {
                    "name": "__init__.py",
                    "content": None
                },
                {
                    "name": "helper.py",
                    "content": None
                },
            ],
        },
        {
            "directory": "tests",
            "files": [
                {
                    "name": "test.py",
                    "content": None
                },
            ],
        },
        {
            "directory": None,
            "files": [
                {
                    "name": "config.py",
                    "content": None
                },
                {
                    "name": ".gitignore",
                    "content": None
                },
                {
                    "name": "LICENCE.txt",
                    "content": licence_text
                },
                {
                    "name": "README.md",
                    "content": None
                },
                {
                    "name": "run.py",
                    "content": None
                },
                {
                    "name": "requirements.txt",
                    "content": None
                },
            ],
        },
    ]
