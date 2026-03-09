# 🏴‍☠️ Pirate Essentials

**Pirate Essentials** is a bootstrap installer that prepares a Python development environment on Windows in a single command.

The utility automatically installs essential tools and libraries required for Python development.

---

## ⚙️ What it installs

Pirate Essentials installs and configures:

* **Python** (if not already installed)
* **Git**
* **virtual environment (.venv)**

### Python development libraries

The installer also installs commonly used development libraries:

* `virtualenv`
* `ipython`
* `requests`
* `httpx`
* `rich`
* `typer`
* `python-dotenv`
* `pytest`
* `black`
* `ruff`
* `fastapi`
* `uvicorn`
* `sqlalchemy`
* `numpy`
* `pandas`
* `matplotlib`
* `jupyter`

---

## 🚀 Usage

Clone the repository:

```bash
git clone https://github.com/ALEXPAN-DEV/pirate-essentials
cd pirate-essentials
```

Run the installer:

```bash
run.bat
```

The installer will:

1. Check internet connectivity
2. Install Python if it is missing
3. Install Git
4. Create a `.venv` environment
5. Install essential Python development packages

---

## 📋 Requirements

* Windows 10 / Windows 11
* Internet connection
* Administrator privileges may be required for some installations

---

## 🧪 Project Goals

This project was created to provide a quick way to bootstrap a Python development environment without manually installing each tool.

---

## 📁 Project Structure

```
pirate-essentials
│
├─ assets/        # ASCII art and static assets
├─ config/        # installation configuration
├─ logs/          # installation logs
├─ src/           # installer source code
│
├─ run.bat        # bootstrap launcher
├─ requirements.txt
└─ README.md
```

---

## ⚠️ Security Note

Windows SmartScreen may show a warning when launching `run.bat` because the script is unsigned.

To run the installer:

```
More info → Run anyway
```

---

## 📬 Contact

If you have questions or suggestions, open an issue or contact:

https://github.com/ALEXPAN-DEV
