import bson

from app import schemas


def test_user_schema():
    find_result = {'_id': bson.ObjectId('6512a9206f0d4b9a6fb92565'), 'name': 'string', 'email': 'zzzzz@example.com',
                   'phone': 'string', 'password': 'sdsdsdsd'}
    user = schemas.users.User(**find_result)
    print(user)
    assert user is not None
