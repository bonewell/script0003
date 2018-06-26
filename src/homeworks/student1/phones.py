import os
import random
import string
import types

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


def format_single_number(number):
    return '+7 ' + '(' + number[0:3] + ') ' + ' '.join([number[3:6], number[6:8], number[8:10]])


def format_number(seq):
    if isinstance(seq, types.GeneratorType):
        return (format_single_number(number) for number in seq)
    else:
        return format_single_number(seq)
