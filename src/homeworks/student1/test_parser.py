import os.path
from unittest.mock import Mock
from .parser import Parser

def test_get_users():
    parser = Parser('fakeuri')
    parser._conn.load = Mock(return_value=[{"id": 1, "name": "Bone Well"}])

    parser.get_users()
    assert parser._users == [{"id": 1, "name": "Bone Well"}]


def test_get_tasks():
    parser = Parser('fakeuri')
    parser._conn.load = Mock(return_value=[{"userId": 1, "id": 2,
                                            "title": "do it",
                                            "completed": False}])

    parser.get_tasks()
    assert parser._tasks == [{"userId": 1, "id": 2,
                              "title": "do it", "completed": False}]


def test_create_file():
    name = "users-tasks.txt"
    parser = Parser('fakeuri')

    parser.save_tasks(name)
    assert os.path.exists(name) and os.path.isfile(name)

    os.remove(name)


def test_write_users():
    name = "users-tasks.txt"
    parser = Parser('fakeuri')
    parser._users = [{"id": 1, "name": "Bone Well"}, {"id": 2, "name": "Waist Sparrow"}]

    parser.save_tasks(name)
    with open(name) as f:
        assert f.readline() == "1 Bone Well\n"
        assert f.readline() == "2 Waist Sparrow\n"

    os.remove(name)


def test_write_users_sorted_by_id():
    name = "users-tasks.txt"
    parser = Parser('fakeuri')
    parser._users = [{"id": 3, "name": "Bone Well"}, {"id": 1, "name": "Waist Sparrow"}]

    parser.save_tasks(name)
    with open(name) as f:
        assert f.readline() == "1 Waist Sparrow\n"
        assert f.readline() == "3 Bone Well\n"

    os.remove(name)


def test_write_tasks():
    name = "users-tasks.txt"
    parser = Parser('fakeuri')
    parser._users = [{"id": 1, "name": "Bone Well"}]
    parser._tasks = [{"userId": 1, "id": 1, "title": "do it one", "completed": False},
                     {"userId": 1, "id": 2, "title": "do it two", "completed": True}]

    parser.save_tasks(name)
    with open(name) as f:
        f.readline()
        assert f.readline() == "  1:do it one; STATUS: Not completed\n"
        assert f.readline() == "  2:do it two; STATUS: Completed\n"

    os.remove(name)
