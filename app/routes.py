from flask import Blueprint, jsonify, request

from .db import get_db

bp = Blueprint("main", __name__)


@bp.get("/health")
def health():
    return jsonify({"status": "healthy"})


@bp.get("/")
def index():
    return jsonify({"service": "igi-demo", "status": "ok"})


@bp.get("/users")
def users():
    with get_db() as conn:
        rows = conn.execute(
            "SELECT id, name, email FROM users ORDER BY id"
        ).fetchall()
    return jsonify([dict(r) for r in rows])


@bp.get("/user")
def user_search():
    name = request.args.get("name", "")
    with get_db() as conn:
        query = "SELECT id, name, email FROM users WHERE name = '" + name + "'"
        rows = conn.execute(query).fetchall()
    return jsonify([dict(r) for r in rows])
