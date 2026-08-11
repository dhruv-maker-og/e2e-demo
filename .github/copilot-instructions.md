# Copilot instructions — igi-demo

A small Flask + SQLite service used for the IGI end-to-end GitHub demo.

## Conventions
- Python 3.12, Flask 3.x. Keep dependencies minimal (`requirements.txt`).
- Routes live in `app/routes.py` as functions on the `main` blueprint.
- All DB access goes through `get_db()` in `app/db.py`. **Always use parameterized
  queries** (`conn.execute(sql, (param,))`) — never string-concatenate user input.
- Endpoints return JSON via `flask.jsonify`.
- Every new endpoint ships with a matching test in `tests/test_app.py`.

## Testing
- Run `pytest -q` from the repository root. CI (`.github/workflows/ci.yml`)
  runs the same command on every pull request and must pass before merge.

## Style
- Small, focused functions. Snake_case names. No unused imports.
