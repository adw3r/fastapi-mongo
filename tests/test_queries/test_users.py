from app import queries, schemas


def test_get_all_users():
    users = queries.users.get_all_users()
    print(users)
    assert type(users) is list
    for user in users:
        assert type(user) is schemas.users.User
