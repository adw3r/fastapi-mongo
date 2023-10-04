import httpx


def test_patch_user():
    user_id = '6512f79e5a8c7f1ec640096e'
    user = {
        "name": "asdasdasd",
        "email": "asdasd@gmail.com",
        "phone": "123123123"
    }

    response = httpx.patch(f'http://127.0.0.1:8000/users/{user_id}', json=user)
    print(response.text)
