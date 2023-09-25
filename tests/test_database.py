from app import database


def test_database_is_connected():
    assert database.mongo_client.admin.command('ping') == {'ok': 1.0}
