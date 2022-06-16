from ..script import world


def add(x, y):
    return x + y


def div(x, y):
    return x / y


def test_add():
    res = add(1, 2)
    w = world.World()

    assert res == 3
