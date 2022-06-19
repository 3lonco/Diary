# Add path for CI/CD tool
import sys
import os
from typing import Type

sys.path.append(
    os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/../script/")
)
import step_function
import sigmoid
import numpy as np
import pytest


def test_step_function():
    x = np.arange(-5.0, 5.0, 0.1)
    y = step_function.step_function(x)
    # All figures are expected to be larger than equal zero
    assert y.all() >= 0


def test_step_function_type_error():
    # Raise TypeError when you give str into step_function
    with pytest.raises(TypeError) as e:
        step_function.step_function("a")


def test_step_function_error():
    a = step_function.step_function(1)
    # 1を入れたら1が返ってくる
    assert a == 1


def test_sigmoid_1():
    # create the values only with nagative values
    x = np.array([-100.0, 100, -1.5])
    y = sigmoid.sigmoid(x)
    assert y.all() >= 0


def test_sigmoid_assertion_error():
    x = np.array([-1.0, 1.0, 2.0])
    y = sigmoid.sigmoid(x)
    # Create the theorotical vaulues
    ans = np.array([0.26894142, 0.73105858, 0.88079707])
    np.testing.assert_array_almost_equal(y, ans, decimal=3)


def test_sigmoid_assertion_error():
    x = np.array([-1.0, 1.0, 2.0])
    y = sigmoid.sigmoid(x)
    ans = np.array([3.26894142, 0.73105858, 0.88079707])
    # Raise AssetionError by putting wrong numbers
    with pytest.raises(AssertionError) as e:
        np.testing.assert_array_almost_equal(y, ans, decimal=1)


def test_sigmoid_type_error():
    with pytest.raises(TypeError) as e:
        sigmoid.sigmoid("a")
