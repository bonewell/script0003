import os.path
from .phones import create_phone, generate_number_strings

def test_phone_len_is_10():
    assert 10 == len(create_phone())


def test_first_digit_is_9():
    assert '9' == create_phone()[0]


def test_all_digits_are_digit():
    for i in create_phone():
        assert i in "0123456789"


def test_file_is_created():
    name = "phones_test.txt"
    generate_number_strings(0, name)
    assert os.path.exists(name) and os.path.isfile(name)
    os.remove(name)


def test_file_contains_5_lines():
    name = "phones_test.txt"
    generate_number_strings(5, name)
    assert 5 == len(open(name).readlines())
    os.remove(name)