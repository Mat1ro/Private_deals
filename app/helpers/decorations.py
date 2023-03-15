import jwt

from flask import request, abort
from app.helpers.constants import PWD_ALGORITHM, PWD_SECRET


def auth_required(func):
    """Checking authorization in web-site"""
    def wrapper(*args, **kwargs):
        if "Authorization" not in request.headers:
            abort(401)

        token = request.headers['Authorization'].split("Bearer ")[-1]
        try:
            jwt.decode(token, PWD_SECRET, algorithms=[PWD_ALGORITHM])
        except Exception as e:
            print("JWT Decode Exception", e)
            abort(401)
        return func(*args, **kwargs)

    return wrapper


def admin_required(func):
    """Checking role in web-site"""
    def wrapper(*args, **kwargs):
        if "Authorization" not in request.headers:
            abort(401)
        token = request.headers["Authorization"].split("Bearer ")[-1]
        role = None
        try:
            user_token = jwt.decode(token, PWD_SECRET, algorithms=[PWD_ALGORITHM])
            role = user_token.get("role", "user_token")
        except Exception as e:
            print("JWT Decode Exception", e)
            abort(401)

        if role != "admin":
            abort(403)

        return func(*args, **kwargs)

    return wrapper
