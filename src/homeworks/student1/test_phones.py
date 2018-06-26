import os.path
from .phones import create_phone, generate_number_strings
from .phones import read_numbers

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


def test_read_file_with_3_lines():
    name = "phones_test.txt"
    with open(name, 'w') as f: f.writelines(['9123456789\n', '9234567890\n', '9345678901\n'])
    assert 3 == len(list(read_numbers(name)))
    os.remove(name)


def test_read_not_existing_file():
    assert 0 == len(list(read_numbers("this_file_does_not_exist.txt")))


def test_correct_format_of_the_line():
    name = "phones_test.txt"
    open(name, 'w').writelines(["9123456789\n", "1234567890\n", "234\n", "9abc123efg\n"])
    assert 1 == len(list(read_numbers(name)))
    os.remove(name)
