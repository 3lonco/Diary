# Add path for CI/CD tool
import sys
import os
from typing import Type

sys.path.append(
    os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/../script/")
)
import step_function
import numpy as np
import pytest

def test_step_function():
    x = np.arange(-5.0, 5.0, 0.1)
    y = step_function.step_function(x)
    #All figures are expected to be larger than equal zero
    assert y.all() >= 0

def test_step_function_type_error():
    # Raise TypeError when you give str into step_function
    with pytest.raises(TypeError) as e:
        step_function.step_function("a")

def test_step_function_error():
    a = step_function.step_function(1)
    # 1を入れたら1が返ってくる
    assert a == 1