from cookiecutter.main import cookiecutter
import typer

app = typer.Typer()


@app.command()
def init():
    project_name = typer.prompt("Enter your project name: ")
    project_dir = typer.prompt("Where should your project be created: ")

    project_dir = project_dir.rstrip('/')
    project_path = f"{project_dir}/{project_name}"
    extra_context = {
        "app_name": project_name,
    }
    cookiecutter(
        'https://github.com/HomesteadFramework/cookiecutter.git',
        output_dir=project_path,
        extra_context=extra_context,
    )


if __name__ == "__main__":
    app()
