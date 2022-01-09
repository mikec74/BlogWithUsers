from flask import abort
from flask_login import current_user
from functools import wraps


def admin_only(func):
    @wraps(func)
    def wrapper_admin_only(*args, **kwargs):
        if not current_user.is_authenticated or current_user.id != 1:
            abort(403)
        else:
            return func(*args, **kwargs)

    return wrapper_admin_only
