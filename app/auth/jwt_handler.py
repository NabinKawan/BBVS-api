import time
from decouple import config
from jose import jwt

JWT_SECRET = config('JWT_SECRET')
JWT_ALGORITHM = config('JWT_ALGORITHM')

print(JWT_SECRET)
print(JWT_ALGORITHM)

# returns generated token


def generate_token_response(token: str):
    return {
        'access_token': token
    }


# Functions used for signing jwt string


def sign_jwt(user_id: str, end_time_ms=5*60*1000):
    payload = {
        'user_id': user_id,
        "expiry": time.time() + end_time_ms
    }
    token = jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM)
    return generate_token_response(token)


def decode_jwt(token: str):
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, JWT_ALGORITHM)
        return decoded_token if decoded_token['expiry'] >= time.time() else None

    except:
        return {}
