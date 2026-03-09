import subprocess
from pathlib import Path


def verify_command(command: list[str]) -> bool:
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            shell=False
        )
        return result.returncode == 0
    except Exception:
        return False


def verify_git() -> bool:
    possible_paths = [
        ["git", "--version"],
        [r"C:\Program Files\Git\cmd\git.exe", "--version"],
        [r"C:\Program Files\Git\bin\git.exe", "--version"],
    ]

    for command in possible_paths:
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                shell=False
            )
            if result.returncode == 0:
                return True
        except Exception:
            continue

    return False


def verify_venv() -> bool:
    return Path(".venv").exists()


def get_venv_python() -> str:
    return str(Path(".venv") / "Scripts" / "python.exe")


def verify_python_package(package_name: str) -> bool:
    try:
        venv_python = get_venv_python()
        result = subprocess.run(
            [venv_python, "-m", "pip", "show", package_name],
            capture_output=True,
            text=True,
            shell=False
        )
        return result.returncode == 0
    except Exception:
        return False