import datetime
import string
import time
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
    assert order2 < order1


def test_delivery_date():
    order = study.Order()
    order.delivery_date = datetime.date(2018, 6, 26)
    assert datetime.date(2018, 6, 26) == order.delivery_date


def test_representation():
    order = study.Order(datetime.datetime(2018, 6, 26, 14, 5, 1))
    order._id = "abc"
    assert "abc[26.06.2018 14:05]" == repr(order)


def test_print_delivery_date():
    order = study.Order()
    order.delivery_date = datetime.date(2018, 7, 1)
    assert "01 Jul 2018" == order.print_delivery_date()


def test_create_order2():
    o = study.Order()
    assert hasattr(o, "created_at")
    assert o._created_at == o.created_at
    assert hasattr(o, "id")
    assert len(o.id) == 20


def test_compare_orders2():
    o1 = study.Order()
    o2 = study.Order()
    assert o1 > o2
