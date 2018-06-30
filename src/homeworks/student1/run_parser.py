from parser import Parser

parser = Parser("http://jsonplaceholder.typicode.com")
parser.get_users()
parser.get_tasks()
parser.save_tasks("users-tasks-status.txt")