import time
from decouple import config
from jose import jwt

JWT_SECRET = '68f47a2ceab553363e07'
JWT_ALGORITHM = "HS256"


# returns generated token


def generate_token_response(user_id: str, token: str):
    return {
        'user_id': user_id,
        'access_token': token
    }


# Functions used for signing jwt string


def sign_jwt(user_id: str, end_time_ms=5 * 60 * 1000):
    payload = {
        'user_id': user_id,
        "expiry": time.time() + end_time_ms
    }
    token = jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM)
    return generate_token_response(user_id, token)


def decode_jwt(token: str):
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, JWT_ALGORITHM)
        return decoded_token if decoded_token['expiry'] >= time.time() else None

    except:
        return {}
