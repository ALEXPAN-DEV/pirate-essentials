from installer import (
    create_venv,
    install_apps,
    install_python_packages,
    load_json,
    load_python_packages,
    upgrade_venv_pip,
)
from logger_setup import setup_logger
from ui import ask_confirmation, show_install_header, show_intro, show_results


def main() -> None:
    logger = setup_logger()

    apps = load_json("config/apps.json")
    packages = load_python_packages("config/python_packages.txt")

    all_items = (
        [item["name"] for item in apps]
        + [".venv", "pip in .venv"]
        + packages
    )

    total_steps = len(apps) + 2 + len(packages)

    show_intro(all_items)

    if not ask_confirmation():
        print("Installation cancelled.")
        return

    show_install_header(total_steps)

    successful: list[str] = []
    failed: list[str] = []

    current_step = 1

    success_apps, failed_apps, current_step = install_apps(apps, logger, current_step, total_steps)
    successful.extend(success_apps)
    failed.extend(failed_apps)

    venv_ok, current_step = create_venv(logger, current_step, total_steps)
    if venv_ok:
        successful.append(".venv")
    else:
        failed.append(".venv")
        show_results(successful, failed + packages + ["pip in .venv"])
        return

    pip_ok, current_step = upgrade_venv_pip(logger, current_step, total_steps)
    if pip_ok:
        successful.append("pip in .venv")
    else:
        failed.append("pip in .venv")
        show_results(successful, failed + packages)
        return

    success_pkgs, failed_pkgs, current_step = install_python_packages(packages, logger, current_step, total_steps)
    successful.extend(success_pkgs)
    failed.extend(failed_pkgs)

    show_results(successful, failed)


if __name__ == "__main__":
    main()