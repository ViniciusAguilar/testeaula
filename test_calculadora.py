from calculadora import somar, subtrair


def test_somar():
    assert somar(2,2) == 4

def test_subtrair():
    assert subtrair(2,2) == 0