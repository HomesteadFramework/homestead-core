import typer

app = typer.Typer()


@app.command()
def create(name: str):
    """Create a new module"""
    print("Creating module:", name)
