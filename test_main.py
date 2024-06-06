from main import soma, sub

def test_soma():
    assert soma(1, 1) == 2

def test_soma_2():
    assert soma(2, 3) == soma(3, 2)

def test_soma_sub():
    assert sub(3, 1) == soma(1, 1)