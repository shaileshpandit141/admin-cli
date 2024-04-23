from ..code_formatter import CodeFormatter


class PythonModuleTemplets:
    def __init__(self, module_name: str) -> None:
        self.module_name = module_name

    def main_py(self) -> str:

        class_comment = lambda name : f'''"""Implementaion of {name.capitalize()}."""'''

        return CodeFormatter.format(f"""   
        class {self.module_name.capitalize()}:
            {class_comment(self.module_name)}

            def __init__(self) -> None:
                # Assign to self object.
                pass
        """)

    def test_py(self) -> str:
        return CodeFormatter.format(f"""
        from {self.module_name} import {self.module_name.capitalize()}
        
                                    
        def main() -> None:
            {self.module_name}: {self.module_name.capitalize()}  = {self.module_name.capitalize()}()


        if __name__ == "__main__":
            main()
        """)
    
    def setuptools(self) -> str:
        return CodeFormatter.format(f"""
        from setuptools import setup


        setup(
            name='{self.module_name}',
            version='1.0.0',
            author='Author',
            author_email='author@gmail.com',
            description='Write a short description for your project.',
            long_description='Write a long description for your project.',
            long_description_content_type='text/markdown',
            url='https://github.com/username/project_name',
            packages=[{self.module_name}],
            install_requires=[
                # List of dependencies your module requires.
            ],
            entry_points={{
                'console_scripts': [
                    # 'command_name=module_name:function name',
                ]
            }},
            classifiers=[
                'Programming Language :: Python :: 3',
                'License :: OSI Approved :: MIT License',
                'Operating System :: OS Independent',
            ],
        )
        """)