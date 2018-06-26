import datetime
import string
import random

def fib(n):
    if n < 2:
        raise Exception("Error")
    nums = [1, 1]
    for i in range(2, n):
        item = nums[i - 2] + nums[i - 1]
        nums.append(item)
    return nums


def fibgen(n):
    if n < 2:
        raise Exception("Error")
    nums = (1, 1)
    yield nums[0]
    yield nums[1]
    for i in range(2, n):
        item = nums[0] + nums[1]
        nums = (nums[1], item)
        yield item


def remove_doubles(inl):
    outl = []
    for i in inl:
        if i not in outl:
            outl.append(i)
    return outl


def convert(inl):
    txt = ""
    for i in inl:
        txt += i
    return txt


def smart_convert(inl):
    return ''.join(inl)


def do_flat_list(inl):
    outl = []
    for i in inl:
        if isinstance(i, list):
            outl.extend(do_flat_list(i))
        else:
            outl.append(i)
    return outl


def square_dictionary(n):
    return {i: i * i for i in range(1, n + 1)}


def print_square_dictionary(n):
    print(square_dictionary(n))


class Order:
    def __init__(self, dt=datetime.datetime.now()):
        self._created_at = dt
        self._id = Order._generate_id()

    @property
    def created_at(self):
        return self._created_at

    @property
    def id(self):
        return self._id

    def __lt__(self, other):
        return self._created_at > other._created_at

    @staticmethod
    def _generate_id():
        return ''.join([Order._get_char() for _ in range(20)])

    @staticmethod
    def _get_char():
        choices = string.ascii_uppercase + "0123456789"
        return random.choice(choices)
