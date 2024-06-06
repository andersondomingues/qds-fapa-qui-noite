from main import soma, sub, div

def test_soma():
    assert soma(1, 1) == 2

def test_soma_2():
    assert soma(2, 3) == soma(3, 2)

def test_soma_sub():
    assert sub(3, 1) == soma(1, 1)

def test_div():
    assert div(10, 0) == None

def teste_div_2():
    assert div(20, 10) == div(10, 5)

def teste_neg():
    #TODO: atualizar quando o outro colega 
    # enviar a função neg
    pass