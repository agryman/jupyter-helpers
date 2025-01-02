"""This module lists the source code for Python objects."""

import inspect
from rich.console import Console
from rich.syntax import Syntax


def lst(name, lexer='python', theme='default', line_numbers=True) -> None:
    """Print a source code listing for the named Python object."""

    code = inspect.getsource(name)
    syntax = Syntax(code, lexer=lexer, theme=theme, line_numbers=line_numbers)
    console = Console()
    console.print(syntax)
