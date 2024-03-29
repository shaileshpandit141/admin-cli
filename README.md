# Admin CLI

Admin CLI is a command-line tool for creating boilerplate code for various types of applications including vanilla JavaScript frontend web apps, Python modules, Python apps, and Flask apps.

### Installation
- vs-code
- live-server (install by `sudo npm install -g live-server` and `pip install live-server`)

- You can install Admin CLI:
    ```shell
    Under the devlopment
    ```

### Usage

Once installed, you can use the following commands to create different types of applications:

### Create a Vanilla JavaScript Frontend Web App
**Command**
```shell
admin-cli create-js-app <app_name>
```
This command will create a basic boilerplate for a vanilla JavaScript frontend web app in the specified directory `<app_name>`.

**Directorys**
```
app_name/
│
├── assets/
│   ├── icons/
|   |   └── favicon.svg
|   └── images/
|
├── meta/
│   ├── config_script.js
│   └── config_styles.css
|
├── src/
│   ├── index.js
│   └── other_js_files
|
├── styles/
│   ├── styles.css
│   └── other_css_files
|
├── .gitignore
├── index.html
├── LICENSE.txt
└── README.md
```

### Create a Python Module
**Command**
```shell
admin-cli create-py-module <module_name>
```

This command will generate a basic Python module structure with the specified `<module_name>`.

**Directorys**
```
module_name/
│
├── docs/
|   └── index.md
|
├── module_name/
│   ├── utils/
|   |   └── __init__.py
│   ├── __init__.py
│   └── main.py
|
├── tests/
│   └── test.py
|
├── config.py
├── .gitignore
├── LICENSE.txt
├── README.md
└── requirements.txt
```

### Create a Python App
**Command**
```shell
admin-cli create-py-app <app_name>
```

Use this command to create a basic Python application structure in the specified directory `<app_name>`.

**Directorys**
```
app_name/
|
├── app_name/
│   ├── utils/
|   |   └── __init__.py
│   ├── __init__.py
│   └── main.py
|
├── docs/
|   └── index.md
|
├── tests/
│   └── test.py
|
├── config.py
├── .gitignore
├── LICENSE.txt
├── README.md
└── requirements.txt
```

### Create a Flask App
**Command**
```shell
admin-cli create-flask-app <app_name>
```

This command will generate a basic Flask application structure with the specified `<app_name>`.

**Directorys**
```
flask_app_name/
│
├── docs/
|   └── index.md
|
├── src/
│   ├── __init__.py
│   ├── views.py
│   ├── models.py
│   ├── forms.py
│   ├── static/
│   │   ├── css/
│   │   |    └── style.css
|   |   ├── images/
|   |   ├── icons/
|   |   └── js/
|   |       └── script.html
│   ├── templates/
│   │   ├── base.html
│   │   └── home.html
│   └── utils/
│       └── helper_functions.py
│
├── tests/
│   └── test.py
│
├── config.py
├── .gitignore
├── LICENSE.txt
├── README.md
├── run.py
└── requirements.txt
```

### Contributing
Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Author
If you have any questions or need assistance with this project, please contact `Shailesh` at `shaileshpandit141@gmail.com`.

Thank you for using Admin-CLI.

