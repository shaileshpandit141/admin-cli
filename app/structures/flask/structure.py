from ..license_text import licence_text
from .templets import FlaskTemplets


def flask_structure(*args, **kwargs) -> list[dict]:

    templets: FlaskTemplets = FlaskTemplets()

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
                    "content": "from src.routes import app",
                },
                {
                    "name": "routes.py",
                    "content": templets.routes_py(),
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
                    "name": "base.css",
                    "content": templets.base_style(),
                },
                {
                    "name": "global.css",
                    "content": templets.global_style(),
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
                    "name": "index.js",
                    "content": templets.index_script(),
                },
            ],
        },
        {
            "directory": "src/templates",
            "files": [
                {
                    "name": "base.html",
                    "content": templets.base_document(),
                },
            ],
        },
        {
            "directory": "src/templates/includes",
            "files": [
                {
                    "name": "header.html",
                    "content": templets.header_document(),
                },
                {
                    "name": "footer.html",
                    "content": templets.footer_document(),
                },
            ],
        },
        {
            "directory": "src/templates/layouts",
            "files": [
                {
                    "name": "main-layout.html",
                    "content": templets.main_layout_document(),
                },
            ],
        },
        {
            "directory": "src/templates/pages",
            "files": [
                {
                    "name": "home.html",
                    "content": templets.home_document(),
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
                    "content": templets.run_py()
                },
                {
                    "name": "requirements.txt",
                    "content": None
                },
            ],
        },
    ]
