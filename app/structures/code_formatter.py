from textwrap import dedent


class CodeFormatter:
    def __init__(self) -> None:
        pass

    @staticmethod
    def format(sting_code: str) -> str:
        return dedent(sting_code).strip("\n")
