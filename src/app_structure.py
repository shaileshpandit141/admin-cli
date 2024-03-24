from default_templets import (
    default_config_script,
    default_config_styles,
    default_document,
    default_styles,
    default_script,
    default_app_favicon
)


py_module_structure: list = [
    {
        "directory": None,
        "files": [
            {
                "name": "__init__.py",
                "content": None,
            },
            {
                "name": "README.md",
                "content": None,
            },
            {
                "name": "dependencies.py",
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
        ],
    },
    {
        "directory": "src",
        "files": [
            {
                "name": "main.py",
                "content": None,
            },
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


frontend_app_structure: list = [
    {
        "directory": None,
        "files": [
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
        "directory": "assets/fonts",
        "files": None
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