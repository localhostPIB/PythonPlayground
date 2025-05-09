#!/usr/bin/python3

import os
import venv
import subprocess
from typing import Final


venv_dir: Final[str] = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "venv"))
requirements_file: Final[str] = "../requirements.txt"


def create_venv(venv_dir: str):
    """
    Create the Virtual environment (venv) for the project.

    :param venv_dir: name of the virtual environment (venv) directory.
    """
    print(f"Creating venv (virtual environment) '{venv_dir}'...")
    builder = venv.EnvBuilder(with_pip=True)
    builder.create(venv_dir)
    print("Virtual environment created.")

def get_os_path(filename: str) -> str:
    """
    Retrieve the path of the virtual environment (venv) based on the operating system used.

    :param filename: name of the virtual environment (venv) file.
    :returns: The path of the virtual environment (venv) directory as string.
    :rtype: str
    """
    folder: Final[str] = "Scripts" if os.name == "nt" else "bin"

    return os.path.join(venv_dir, folder, filename)


def install_requirements(requirements_file="requirements.txt"):
    """
    Installs all libs from the requirements txt.

    :param requirements_file: file name of the requirements txt. Default is requirements.txt
    """
    pip_executable: Final[str] = get_os_path("pip.exe" if os.name == "nt" else "pip")

    print(f"Install packages from: '{requirements_file}'...")
    subprocess.check_call([pip_executable, "install", "-r", requirements_file])
    print("Packages installed.")

def create_executable():
    """
    Creates a executable.
    """
    print(f"Creating executable:")
    python_executable: Final[str] = get_os_path("python.exe" if os.name == "nt" else "python")
    # cmd: pyinstaller --noconsole --onefile --windowed tk_bloch.py
    subprocess.check_call([python_executable, "-m", "PyInstaller", "--noconsole", "--onefile", "--windowed" ,"tk_bloch.py"])


if __name__ == "__main__":
    create_venv(venv_dir)
    install_requirements(requirements_file)
    create_executable()
    print("Finish")
