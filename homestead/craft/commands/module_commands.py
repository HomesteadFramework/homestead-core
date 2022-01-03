import pathlib
import shutil

import typer
import questionary

from homestead.utils.filesystem import get_file_path

app = typer.Typer()


@app.command()
def create(
        name: str = typer.Option(..., help="Name of the module"),
):
    """Create a new module"""
    app_root_path = get_file_path("")
    modules_path = app_root_path.joinpath("app/modules")

    # create module directory
    new_module_path = str(modules_path.joinpath(name.lower()))
    pathlib.Path(new_module_path).mkdir(parents=True)

    type_of_controller = questionary.select(
        "What kind of router do you want?",
        choices=["web", "api"],
    ).ask()

    # create required files
    craft_path = str(pathlib.Path(__file__).parent.parent)
    modules_stubs_path = f"{craft_path}/stubs/modules"

    # create controller
    controller_file_path = f"{new_module_path}/controller.py"

    if type_of_controller == "web":
        controller_stub_path = f"{modules_stubs_path}/web_controller.py"
        shutil.copyfile(controller_stub_path, controller_file_path)
    elif type_of_controller == "api":
        controller_stub_path = f"{modules_stubs_path}/api_controller.py"
        shutil.copyfile(controller_stub_path, controller_file_path)

    # create init models and schemas files
    open(f"{new_module_path}/__init__.py", "a").close()
    open(f"{new_module_path}/models.py", "a").close()
    open(f"{new_module_path}/schemas.py", "a").close()

    # create services dir and file
    services_dir_path = f"{new_module_path}/services"
    pathlib.Path(services_dir_path).mkdir(parents=True)
    open(f"{services_dir_path}/{name.lower()}_service.py", "a").close()


if __name__ == "__main__":
    app()
