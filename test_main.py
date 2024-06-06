from main import soma

def test_soma():
    assert soma(1, 1) == 2

def test_soma_2():
    assert soma(2, 3) == soma(3, 2)