from bvulist import bvulist
import pytest

@pytest.fixture
def newList():
    L = bvulist()
    L.append(1)
    L.append(2)
    L.append(3)

    yield L

@pytest.fixture
def emptyList():
    L = bvulist()

    yield L

def test_prepend(newList):
    newList.prepend(0)
    assert newList[0] == 0 and len(newList) == 4

def test_pop_back(newList):
    x = newList.pop_back()
    assert newList[:] == [1,2] and x == 3

def test_pop_front(newList):
    x = newList.pop_front()
    assert newList[:] == [2,3] and x == 1

    
def test_pop_back_empty(emptyList):
    with pytest.raises(IndexError):
        emptyList.pop_back()


def test_pop_front_empty(emptyList):
    with pytest.raises(IndexError):
        emptyList.pop_front()

    
