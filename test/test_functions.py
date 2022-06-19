# Add path for CI/CD tool
import sys
import os
from typing import Type

sys.path.append(
    os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/../script/")
)
import step_function
import sigmoid
import reluFunction
import identity_function
import softmax
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


def test_relu_negative():
    x = np.array([-100, 0, 1.0])
    y = reluFunction.relu(x)
    assert y.all() <= 0


def test_relu_positive():
    x = np.array([0.1, 100, 1.0])
    y = reluFunction.relu(x)
    assert y.all() > 0


def test_identity_function():
    x = np.array([1, 2, 0.1])
    y = identity_function.identity_function(x)
    assert y.all() == x.all()


def test_identity_function():
    with pytest.raises(TypeError) as e:
        identity_function.identity_function("a")


def test_softmax():
    a = np.array([0.3, 2.9, 4.0])
    y = softmax.softmax(a)
    # Check the output of softmax is the same as the following numbers
    ans = np.array([0.01821127, 0.24519181, 0.73659691])
    assert y.all() == ans.all()


def test_softmax_sum():
    arr = np.random.rand(1000)
    sum = np.sum(softmax.softmax(arr))
    # Check if the sum of an randam array is equal to 1.
    assert pytest.approx(sum, 0.00001) == 1.0
