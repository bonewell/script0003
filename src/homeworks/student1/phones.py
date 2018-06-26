import random
import string
import os

def create_phone():
    return '9' + ''.join(random.choice(string.digits) for _ in range(9))


def generate_number_strings(n, name):
    with open(name, 'w') as f:
        for _ in range(n):
            f.write(create_phone() + '\n')


def check_format(phone):
    return phone.isdigit() is True and len(phone) == 10 and phone[0] == '9'


def read_numbers(name):
    try:
        with open(name) as f:
            for line in f:
                phone = line.strip()
                if check_format(phone):
                    yield phone
    except OSError:
         pass
