from setuptools import setup


setup(
    name='admin-cli',
    version='1.0.0',
    author='Shailesh',
    author_email='shaileshpandit141@gmail.com',
    description='Admin CLI is a command-line tool for creating boilerplate code for various types of applications.',
    long_description="""Admin CLI is a command-line tool for creating boilerplate code for various types of applications including vanilla JavaScript frontend web apps, Python modules, Python apps, and Flask apps.""",
    long_description_content_type='text/markdown',
    url='https://github.com/shaileshpandit141/Admin-CLI',
    packages=['app'],
    install_requires=[
        # List of dependencies your module requires.
    ],
    entry_points={
        'console_scripts': [
            'admin-cli=app.main:main',
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)