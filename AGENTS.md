# Repository Guidelines

## Project Structure & Module Organization

This is a Django 6 personal blog project. The active app lives in `blog/`, with models in `blog/models.py`, class-based views in `blog/views.py`, URL routes in `blog/urls.py`, templates in `blog/templates/blog/`, and migrations in `blog/migrations/`. Project settings and root routing are in `personal_blog/settings.py` and `personal_blog/urls.py`. The root `manage.py` is the primary Django command entrypoint. Deployment files include `Dockerfile`, `entrypoint.sh`, and `requirements.txt`.

## Build, Test, and Development Commands

Create an environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run the app locally with SQLite:

```bash
python manage.py migrate
python manage.py runserver
```

Run tests:

```bash
python manage.py test
```

Build and run the container:

```bash
docker build -t py-blog .
docker run --rm -p 8000:80 py-blog
```

## Coding Style & Naming Conventions

Follow standard Django and PEP 8 conventions: 4-space indentation, `snake_case` for functions and variables, `PascalCase` for classes, and descriptive template names such as `post_detail.html`. Keep app behavior in the `blog` app unless it clearly belongs at project level. Prefer Django class-based view patterns already used in `blog/views.py`; add mixins only when auth behavior is implemented.

## Testing Guidelines

Use Django’s built-in test runner and place tests in `blog/tests.py` or a `blog/tests/` package if tests grow. Name test methods with `test_...` and focus on models, view status codes, redirects, permissions, and template usage. Add or update tests for any model, URL, or view behavior change before running `python manage.py test`.

## Commit & Pull Request Guidelines

Recent commits use short imperative messages, sometimes with a conventional prefix, for example `chore: dockerize django app, fix settings, add entrypoint` and `Add CRUD views, templates, URLs, and blog app wiring`. Keep commits focused and mention the main area changed.

For pull requests, include a concise summary, test results, related issue links if any, and screenshots for template or UI changes. Note any migration, environment variable, or deployment impact.

## Security & Configuration Tips

Local configuration is loaded from `.env` by `personal_blog/settings.py`. Do not commit real `SECRET_KEY` values, credentials, or production database files. Set `DEBUG=False`, explicit `ALLOWED_HOSTS`, and `CSRF_TRUSTED_ORIGINS` for deployed environments.
