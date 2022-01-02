import typer

from .commands import module_commands

app = typer.Typer()

app.add_typer(module_commands.app, name="module")

if __name__ == "__main__":
    app()