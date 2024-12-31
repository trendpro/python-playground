"""Python Unit Testing."""


def add(num):
    return num + 1


def test_add():
    assert add(3) == 4


test_add()
