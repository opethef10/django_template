#!/usr/bin/env python3
"""Setup script for PythonAnywhere deployment.

This script automates the initial setup of a Django project on PythonAnywhere,
including webapp creation, static file mappings, environment configuration,
database migrations, and superuser creation.
"""

import os
from pathlib import Path
import secrets
import subprocess
import sys

from pythonanywhere_core.base import get_username, helpful_token_error_message
from pythonanywhere_core.webapp import Webapp


PYTHON_VERSION = "3.13"
USERNAME = get_username()
WEBAPP_NAME = f"{USERNAME}.pythonanywhere.com"
VIRTUALENV_PATH = Path(f"/home/{USERNAME}/.virtualenvs/{USERNAME}")
VIRTUALENV_PYTHON = VIRTUALENV_PATH / "bin" / "python"

PROJECT_PATH = Path(f"/home/{USERNAME}/{WEBAPP_NAME}")
DJANGO_SETTINGS = "src.settings.production"
DJANGO_BASE_CMD = [str(VIRTUALENV_PYTHON), "manage.py"]
ENV_FILE_PATH = PROJECT_PATH / ".env"

ENV_FILE_TEMPLATE = """\
PROJECT_SLUG={}
PROJECT_NAME={}
PROJECT_DESCRIPTION={}
PROJECT_DOMAIN={}
DJANGO_SECRET_KEY={}
DJANGO_ALLOWED_HOSTS={}
"""

VAR_WWW = Path("/var/www/")
WSGI_FILE_PATH = VAR_WWW / f"{USERNAME}_pythonanywhere_com_wsgi.py"
BASHRC_PATH = Path(f"/home/{USERNAME}/.bashrc")

STATIC_FILE_MAPPINGS = [
    ("/static/", VAR_WWW / "static"),
    ("/media/", VAR_WWW / "media"),
    ("/favicon.ico", VAR_WWW / "static" / "favicon.ico"),
    ("/robots.txt", VAR_WWW / "static" / "robots.txt"),
    ("/ads.txt", VAR_WWW / "static" / "ads.txt"),
]

WSGI_FILE_CONTENT = f"""\
import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings.production')

path = '{PROJECT_PATH}'
if path not in sys.path:
    sys.path.insert(0, path)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
"""


def check_api_token():
    """Check that the API_TOKEN environment variable is set.

    Exits with error if not set.
    """
    token = os.environ.get("API_TOKEN")
    if token is None:
        print(helpful_token_error_message())
        sys.exit(1)


def check_project_folder():
    """Check that the project folder exists.

    Exits with error if PROJECT_PATH does not exist.
    """
    if not PROJECT_PATH.exists():
        print(f"Error: Project folder {PROJECT_PATH} does not exist.")
        print("Please clone your repository first.")
        sys.exit(1)


def check_virtualenv():
    """Check that the virtualenv is created and activated.

    Verifies VIRTUAL_ENV matches VIRTUALENV_PATH and that the Python
    executable exists. Exits with error if either check fails.
    """
    if os.environ.get("VIRTUAL_ENV") != str(VIRTUALENV_PATH):
        print("Error: Virtualenv not activated or activated incorrectly.")
        print(f"Expected VIRTUAL_ENV={VIRTUALENV_PATH}")
        print(f"Got VIRTUAL_ENV={os.environ.get('VIRTUAL_ENV')}")
        sys.exit(1)

    if not VIRTUALENV_PYTHON.exists():
        print(f"Error: Virtualenv not found at {VIRTUALENV_PATH}.")
        print("Please create and activate your virtualenv first.")
        sys.exit(1)


def check_manage_py():
    """Check that manage.py exists in the project folder.

    Exits with error if not found.
    """
    manage_py_path = PROJECT_PATH / "manage.py"
    if not manage_py_path.exists():
        print(f"Error: manage.py not found at {manage_py_path}.")
        sys.exit(1)


def check_var_www():
    """Create /var/www/ directory if it does not exist."""
    VAR_WWW.mkdir(parents=True, exist_ok=True)


def create_wsgi_file():
    """Write the WSGI configuration file to /var/www/."""
    with open(WSGI_FILE_PATH, "w") as f:
        f.write(WSGI_FILE_CONTENT)
    print(f"Created WSGI file at {WSGI_FILE_PATH}")


def run_django_migrate():
    """Run Django database migrations.

    Exits with error if migration fails.
    """
    result = subprocess.run(
        DJANGO_BASE_CMD + ["migrate", f"--settings={DJANGO_SETTINGS}"],
        cwd=PROJECT_PATH,
    )
    if result.returncode != 0:
        print("Error: Django migrate failed.")
        sys.exit(1)
    print("Django migrations applied successfully.")


def run_django_collectstatic():
    """Collect static files for Django.

    Exits with error if collection fails.
    """
    result = subprocess.run(
        DJANGO_BASE_CMD + ["collectstatic", "--no-input", f"--settings={DJANGO_SETTINGS}"],
        cwd=PROJECT_PATH,
    )
    if result.returncode != 0:
        print("Error: Django collectstatic failed.")
        sys.exit(1)
    print("Static files collected successfully.")


def run_django_createsuperuser():
    """Create a Django superuser.

    Exits with error if creation fails.
    """
    result = subprocess.run(
        DJANGO_BASE_CMD + ["createsuperuser", f"--settings={DJANGO_SETTINGS}"],
        cwd=PROJECT_PATH,
    )
    if result.returncode != 0:
        print("Error: Django createsuperuser failed.")
        sys.exit(1)
    print("Superuser created successfully.")


def copy_environment_variables():
    """Create .env file with project configuration.

    Prompts for project name and description. Skips if .env already exists.
    """
    if ENV_FILE_PATH.exists():
        print(f"Environment file {ENV_FILE_PATH} already exists. Skipping creation.")
        return

    project_name = input("Enter your project name: ")
    project_description = input("Enter a description of your project: ")

    env_content = ENV_FILE_TEMPLATE.format(
        PROJECT_SLUG=USERNAME,
        PROJECT_NAME=project_name,
        PROJECT_DESCRIPTION=project_description,
        PROJECT_DOMAIN=WEBAPP_NAME,
        DJANGO_SECRET_KEY=secrets.token_urlsafe(50),
        DJANGO_ALLOWED_HOSTS=WEBAPP_NAME,
    )
    with open(ENV_FILE_PATH, "w") as f:
        f.write(env_content)
    print(f"Created environment file at {ENV_FILE_PATH}")


def set_django_settings_module():
    """Append DJANGO_SETTINGS_MODULE to .bashrc if not already present."""
    export_line = f"export DJANGO_SETTINGS_MODULE={DJANGO_SETTINGS}\n"

    if BASHRC_PATH.exists():
        with open(BASHRC_PATH, "r") as f:
            content = f.read()
        if export_line.strip() in content:
            print(f"DJANGO_SETTINGS_MODULE already set in {BASHRC_PATH}")
            return

    with open(BASHRC_PATH, "a") as f:
        f.write(export_line)
    print(f"Added DJANGO_SETTINGS_MODULE to {BASHRC_PATH}")


if __name__ == "__main__":
    check_api_token()
    check_project_folder()
    check_virtualenv()
    check_manage_py()
    webapp = Webapp(WEBAPP_NAME)
    webapp.create(
        python_version=PYTHON_VERSION,
        virtualenv_path=Path(VIRTUALENV_PATH),
        project_path=PROJECT_PATH,
        nuke=False,
    )
    print("Webapp created successfully.")
    webapp.patch({"force_https": True})
    print("Enabled force HTTPS.")
    for url_prefix, directory in STATIC_FILE_MAPPINGS:
        webapp.create_static_file_mapping(url_prefix, directory)
    print("Created static file mappings.")

    copy_environment_variables()
    set_django_settings_module()
    run_django_migrate()
    run_django_collectstatic()
    run_django_createsuperuser()
    check_var_www()
    create_wsgi_file()
    webapp.reload()
    print("Webapp reloaded successfully.")
