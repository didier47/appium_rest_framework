#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from prueba_appium.settings import SERVER_PORT


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prueba_appium.settings')
    try:
        from django.core.management import execute_from_command_line

        from django.core.management.commands.runserver import Command
        Command.default_port = f'{SERVER_PORT}'

    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
