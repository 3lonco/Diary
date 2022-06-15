import sys
import pytest
def add(x,y):
  return x+y


def div(x,y):
  return x/y
def test_add():
  res = add(1,2)
  assert res==3


def exit(status):
  sys.exit(status)


def test_exception():
  with pytest.raises(ZeroDivisionError):
    res = div(1,0)
      

def test_exit_status():
  #sys.exitが実行されると　systemExitが選出される
  with pytest.raises(SystemExit) as e:
    exit(1)
  
  assert e.value.code ==1