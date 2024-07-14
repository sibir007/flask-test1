import pytest


@pytest.fixture
def order():
    print(f'in: order():')
    return []


@pytest.fixture
def append_first(order):
    print(f'in: append_first(order):')
    order.append(1)


@pytest.fixture
def append_second(order, append_first):
    print(f'in: append_second(order, append_first):')
    order.extend([2])


@pytest.fixture(autouse=True)
def append_third(order, append_second):
    print(f'in: append_third(order, append_second):')
    order += [3]


def test_order(order):
    print(f'in: test_order(order):')
    assert order == [1, 2, 3]