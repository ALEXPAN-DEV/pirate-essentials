import json
import subprocess
import venv
from pathlib import Path
from typing import Any

from rich.console import Console

from verifier import get_venv_python, verify_command, verify_python_package, verify_venv

console = Console()


def load_json(path: str) -> list[dict[str, Any]]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def load_python_packages(path: str) -> list[str]:
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    return [line.strip() for line in lines if line.strip()]


def install_command(command: list[str]) -> tuple[bool, str]:
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            shell=False
        )
        output = (result.stdout or "") + "\n" + (result.stderr or "")
        return result.returncode == 0, output.strip()
    except Exception as exc:
        return False, str(exc)


def print_step(index: int, total: int, name: str, status: str) -> None:
    console.print(f"[cyan][{index}/{total}][/cyan] {name} | {status}")


def install_apps(apps: list[dict[str, Any]], logger, start_index: int, total: int) -> tuple[list[str], list[str], int]:
    successful: list[str] = []
    failed: list[str] = []
    current = start_index

    for app in apps:
        name = app["name"]
        print_step(current, total, name, "installing")
        logger.info("Installing app: %s", name)

        ok, output = install_command(app["install"])
        logger.info("Install output for %s:\n%s", name, output)

        verified = verify_command(app["verify"])
        if ok and verified:
            successful.append(name)
            print_step(current, total, name, "installed")
            logger.info("Installed successfully: %s", name)
        else:
            failed.append(name)
            print_step(current, total, name, "failed")
            logger.error("Failed to install: %s", name)

        current += 1

    return successful, failed, current


def create_venv(logger, index: int, total: int) -> tuple[bool, int]:
    print_step(index, total, ".venv", "creating")
    logger.info("Creating virtual environment")

    try:
        if not verify_venv():
            venv.create(".venv", with_pip=True)
        ok = verify_venv()
        if ok:
            print_step(index, total, ".venv", "created")
            logger.info("Virtual environment ready")
            return True, index + 1
        print_step(index, total, ".venv", "failed")
        logger.error("Failed to create virtual environment")
        return False, index + 1
    except Exception as exc:
        logger.exception("Error creating virtual environment: %s", exc)
        print_step(index, total, ".venv", "failed")
        return False, index + 1


def upgrade_venv_pip(logger, index: int, total: int) -> tuple[bool, int]:
    print_step(index, total, "pip in .venv", "upgrading")
    logger.info("Upgrading pip in virtual environment")

    venv_python = get_venv_python()
    ok, output = install_command([venv_python, "-m", "pip", "install", "--upgrade", "pip"])
    logger.info("pip upgrade output:\n%s", output)

    if ok:
        print_step(index, total, "pip in .venv", "upgraded")
        logger.info("pip upgraded successfully")
        return True, index + 1

    print_step(index, total, "pip in .venv", "failed")
    logger.error("Failed to upgrade pip in .venv")
    return False, index + 1


def install_python_packages(packages: list[str], logger, start_index: int, total: int) -> tuple[list[str], list[str], int]:
    successful: list[str] = []
    failed: list[str] = []
    current = start_index

    venv_python = get_venv_python()

    for package in packages:
        print_step(current, total, package, "installing")
        logger.info("Installing Python package: %s", package)

        ok, output = install_command([venv_python, "-m", "pip", "install", "-U", package])
        logger.info("Install output for %s:\n%s", package, output)

        verified = verify_python_package(package)
        if ok and verified:
            successful.append(package)
            print_step(current, total, package, "installed")
            logger.info("Installed successfully: %s", package)
        else:
            failed.append(package)
            print_step(current, total, package, "failed")
            logger.error("Failed to install: %s", package)

        current += 1

    return successful, failed, current