import os.path
import requests

class Connection(object):
    def __init__(self, uri):
        self._uri = uri

    def load(self, path):
        return requests.get(os.path.join(self._uri, path)).json()


class Parser(object):
    def __init__(self, uri):
        self._conn = Connection(uri)
        self._users = []
        self._tasks = []

    def get_users(self):
        self._users = [{"id": u['id'], "name": u['name']} for u in self._conn.load('users')]

    def get_tasks(self):
        self._tasks = self._conn.load('todos')

    def save_tasks(self, filename):
        self._sort_users()
        with open(filename, 'w') as f:
            for u in self._users:
                self._write_user_tasks(f, u)

    def _sort_users(self):
        self._users = sorted(self._users, key=lambda u: u['id'])

    def _write_user_tasks(self, fd, user):
        fd.write(Parser._format_user(user))
        fd.writelines((Parser._format_task(t) for t in self._tasks
                       if t['userId'] == user['id']))

    @staticmethod
    def _format_user(user):
        return "{id} {name}\n".format(**user)

    @staticmethod
    def _format_task(task):
        return "  {}:{}; STATUS: {}\n".format(task['id'], task['title'],
            'Completed' if task['completed'] else 'Not completed')
