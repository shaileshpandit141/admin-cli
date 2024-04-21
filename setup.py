from setuptools import setup


setup(
    name='admin-cli',
    version='1.0.0',
    author='Shailesh',
    author_email='shaileshpandit141@gmail.com',
    description='Admin CLI is a command-line tool for creating boilerplate code for various types of applications.',
    long_description='Admin CLI is a command-line tool for creating boilerplate code for various types of applications including vanilla JavaScript frontend web apps, Python modules, Python apps, and Flask apps.',
    long_description_content_type='text/markdown',
    url='https://github.com/shaileshpandit141/Admin-CLI',
    packages=['app'],
    install_requires=[
        # List of dependencies your module requires.
        'typer',
        'live-server'
    ],
    entry_points={
        'console_scripts': [
            'admin create-py-app=app:create_py_app',
            'admin create-js-app=app:create_js_app',
            'admin create-flask-app=app:create_flask_app',
            'admin create-py-module=app:create_py_module',
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)