# Django Application Template

A Django template designed to provide a foundation for projects with structured models, reusable components, and scalable features. This template simplifies creating a well-organized Django application by predefining a modular architecture and essential database models.

## About

This template serves as a starting point for Django projects. It includes models, views, and URL patterns for managing data related to entities

## Features

- Modular Django app structure with reusable components.
- Predefined models for common data entities such as artists, songs, and metadata.
- Ready-to-use admin configurations and example class-based views.
- Built-in support for importing data via custom management commands.

## Prerequisites

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) (or install via `pip install uv`)
- SQLite (or any supported database backend)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/opethef10/django_template.git
cd django_template
```

### 2. Install Dependencies

Install [uv](https://docs.astral.sh/uv/) and set up the environment:

```bash
pip install uv
uv sync --group dev
```

### 3. Configure the Database

Run migrations to set up the database:

```bash
uv run python manage.py makemigrations
uv run python manage.py migrate
```

### 4. Run the Development Server

Start the server to see the app in action:

```bash
uv run python manage.py runserver
```

Visit [http://localhost:8000](http://localhost:8000) to explore the project.

## Contributing

Fork this repository and contribute by submitting pull requests. Feel free to suggest improvements or share how you've adapted the template for your own projects.

## License

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) file for details.
