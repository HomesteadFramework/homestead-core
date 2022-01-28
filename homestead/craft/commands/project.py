from cookiecutter.main import cookiecutter
import typer

app = typer.Typer()


@app.command()
def init():
    project_dir = typer.prompt("Where should your project be created: Please enter the full path")
    project_dir = project_dir.rstrip('/')

    cookiecutter(
        'https://github.com/HomesteadFramework/cookiecutter.git',
        output_dir=project_dir,
    )


if __name__ == "__main__":
    app()
