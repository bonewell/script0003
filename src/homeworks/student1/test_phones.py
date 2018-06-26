import os.path
import string
from .phones import create_phone, generate_number_strings
from .phones import read_numbers, format_number

def test_number_length_is_10():
    assert 10 == len(create_phone())


def test_first_digit_is_9():
    assert '9' == create_phone()[0]


def test_number_contains_just_digits():
    for i in create_phone():
        assert i in string.digits


def test_create_empty_file():
    name = "phones_test.txt"
    generate_number_strings(0, name)
    assert os.path.exists(name) and os.path.isfile(name)
    os.remove(name)


def test_create_file_with_5_lines():
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


def test_read_just_lines_with_correct_format():
    name = "phones_test.txt"
    open(name, 'w').writelines(["9123456789\n", "1234567890\n", "234\n", "9abc123efg\n"])
    assert 1 == len(list(read_numbers(name)))
    os.remove(name)


def test_add_prefix():
    assert "+7 " == format_number("9123456789")[0:3]


def test_add_parenthesis():
    assert "(912)" == format_number("9123456789")[3:8]


def test_add_spaces():
    assert " 345 67 89" == format_number("9123456789")[8:]


def test_format_few_numbers():
    seq = (n for n in ["9123456789", "9012345678"])
    assert ["+7 (912) 345 67 89", "+7 (901) 234 56 78"] == list(format_number(seq))
