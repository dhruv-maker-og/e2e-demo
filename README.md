# igi-demo

A minimal Flask + SQLite service for the IGI End-to-End GitHub Experience demo.

## Run locally

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Then visit:

- `GET /` — service status
- `GET /users` — list all users
- `GET /user?name=Ada%20Lovelace` — look up a user by name

## Test

```powershell
pytest -q
```
test
