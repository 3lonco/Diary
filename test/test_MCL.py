# Add path for CI/CD tool
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/../script/"))
import world
def add(x, y):
    return x + y


def div(x, y):
    return x / y


def test_add():
    res = add(1, 2)
    w = world.World()
    assert res == 3
