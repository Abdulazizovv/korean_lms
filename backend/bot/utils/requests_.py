import requests
from requests.exceptions import RequestException
from requests.adapters import HTTPAdapter
from requests.exceptions import ConnectionError, Timeout

URL = 'http://127.0.0.1:8000/api/'
session = requests.Session()
session.mount('http://', HTTPAdapter(max_retries=3))

def get(url, headers=None, params=None):
    try:
        response = session.get(URL + url, headers=headers, params=params)
        response.raise_for_status()
    except ConnectionError as e:
        raise RequestException('Connection error') from e
    except Timeout as e:
        raise RequestException('Timeout error') from e
    return response


def post(url, headers=None, data=None):
    try:
        response = session.post(URL + url, headers=headers, data=data)
        response.raise_for_status()
    except ConnectionError as e:
        raise RequestException('Connection error') from e
    except Timeout as e:
        raise RequestException('Timeout error') from e
    return response


def put(url, headers=None, data=None):
    try:
        response = session.put(URL + url, headers=headers, data=data)
        response.raise_for_status()
    except ConnectionError as e:
        raise RequestException('Connection error') from e
    except Timeout as e:
        raise RequestException('Timeout error') from e
    return response


def delete(url, headers=None):
    try:
        response = session.delete(URL + url, headers=headers)
        response.raise_for_status()
    except ConnectionError as e:
        raise RequestException('Connection error') from e
    except Timeout as e:
        raise RequestException('Timeout error') from e
    return response


def create_user(**data):
    """
    Register a new bot user
    :param data: dict
    :return: Response

    Example:
    data = {
        'user_id': 123456789,
        'phone_number': '998901234567',
        'first_name': 'John',
        'last_name': 'Doe', | optional
        'username': 'johndoe', | optional
        'language_code': 'en', | optional | default: 'uz'
        'is_active': True | optional | default: True
    }
    """
    return post('botusers/register/', data=data)