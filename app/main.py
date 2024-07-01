from sys import argv
from modules import CodeFormatter
from command_action import CommandAction


def main() -> None:
    command_list: list[str] = argv

    if len(command_list) == 1:
        print(CodeFormatter.format(f"""
            {" Help ".center(50, "-")}

            :: admin-cli            <- command

            Admin-CLI Required at list one argument.

            List of supported argument are:

            :: create-py-module
            :: create-py-app
            :: create-flask-app
            :: create-js-app

            {"-".center(50, "-")}

        """))

    elif 1 < len(command_list) <= 3:
        match command_list[1]:
            case "create-py-module":
                if len(command_list) == 3:

                    CommandAction.create_py_module(command_list[2])

                else:
                    print(CodeFormatter.format(f"""
                        {" Error ".center(50, "-")}

                        :: create-py-module       <- command

                        option [required]: app_name

                        Example: admin-cli create-py-module <module_name>

                        {"-".center(50, "-")}
                    """))

            case "create-js-module":
                if len(command_list) == 3:

                    CommandAction.create_js_module(command_list[2])

                else:
                    print(CodeFormatter.format(f"""
                        {" Error ".center(50, "-")}

                        :: create-js-module       <- command

                        option [required]: module_name

                        Example: admin-cli create-py-module <module_name>

                        {"-".center(50, "-")}
                    """))

            case "create-py-app":
                if len(command_list) == 3:

                    CommandAction.create_py_app(command_list[2])

                else:
                    print(CodeFormatter.format(f"""
                        {" Error ".center(50, "-")}

                        :: create-py-app       <- command

                        option [required]: app_name

                        Example: admin-cli create-py-app <app_name>

                        {"-".center(50, "-")}
                    """))

            case "create-flask-app":
                if len(command_list) == 3:

                    CommandAction.create_flask_app(command_list[2])

                else:
                    print(CodeFormatter.format(f"""
                        {" Error ".center(50, "-")}

                        :: create-flask-app       <- command

                        option [required]: app_name

                        Example: admin-cli create-flask-app <app_name>

                        {"-".center(50, "-")}
                    """))

            case "create-js-app":
                if len(command_list) == 3:

                    CommandAction.create_js_app(command_list[2])

                else:
                    print(CodeFormatter.format(f"""
                        {" Error ".center(50, "-")}

                        :: create-js-app        <- command

                        option [required]: app_name

                        Example: admin-cli create-js-app <app_name>

                        {"-".center(50, "-")}
                    """))

            case _:
                command_name: str = command_list[1]
                print(CodeFormatter.format(f"""
                    {" command not found ".center(50, "-")}

                    {command_name}          <- command not found

                    List of supported command are

                    :: create-py-module     -> option [required]: module_name
                    :: create-js-module     -> option [required]: module_name
                    :: create-py-app        -> option [required]: app_name
                    :: create-flask-app     -> option [required]: app_name
                    :: create-js-app        -> option [required]: app_name

                    Example: admin-cli create-js-app <js_app_name>

                    {"-".center(50, "-")}
                """))
    else:
        print(CodeFormatter.format(f"""
            {" command not found ".center(50, "-")}

            admin-cli {" ".join(command_list[1:])}          <- command not found

            List of supported command are:

            :: admin-cli create-js-app <app_name>
            :: admin-cli create-py-app <app_name>
            :: admin-cli create-py-module <module_name>
            :: admin-cli create-js-module <module_name>
            :: admin-cli create-flask-app <app_name>

            Example:

            admin-cli create-js-app js_test_app
            admin-cli create-py-app py_test_app
            admin-cli create-py-module py_test_module
            admin-cli create-js-module js_test_module
            admin-cli create-flask-app flask_test_app

            {"-".center(50, "-")}
        """))



if __name__ == "__main__":
    main()

