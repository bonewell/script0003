import datetime
import string
import homeworks.student1.study as study


def test_fib():
    assert [1, 1, 2, 3, 5, 8, 13] == study.fib(7)


def test_fibgen():
     assert [1, 1, 2, 3, 5, 8, 13] == list(study.fibgen(7))


def test_rmd():
    assert [1, 2, 3, 4] == study.remove_doubles([1, 2, 3, 3, 2, 1, 3, 4, 1])


def test_convert():
    assert "abc" == study.convert(['a', 'b', 'c'])


def test_smart_convert():
    assert "abec" == study.smart_convert(['a', 'b', 'e', 'c'])


def test_do_flat_list():
    assert [1, 2, 3, 4, 5, 6, 7, 8, 9] == study.do_flat_list([1, [2, 3], [4, 5, 6], 7, [8, 9]])
    assert [1, 2, 3, 4, 5, 6, 7, 8, 9] == study.do_flat_list([1, [2, 3], [[4, 5], 6], 7, [8, 9]])


def test_square_dictionary():
    assert {1: 1, 2: 4, 3: 9, 4: 16, 5: 25} == study.square_dictionary(5)


def test_print_square_dictionary():
    study.print_square_dictionary(7)


def test_create_order():
    order = study.Order(datetime.datetime(2018, 6, 26, 14, 5, 1))
    assert datetime.datetime(2018, 6, 26, 14, 5, 1) == order.created_at
    for char in order.id:
        assert char in string.ascii_uppercase + "0123456789"


def test_compare_orders():
    order1 = study.Order(datetime.datetime(2018, 6, 26, 14, 5, 1))
    order2 = study.Order(datetime.datetime(2018, 6, 26, 14, 5, 2))
    assert True == (order1 < order2)