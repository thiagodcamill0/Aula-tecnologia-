# test_calculadora.py
import pytest
from calculadora import adicao, subtracao, multiplicacao, divisao

def test_adicao():
    assert adicao(3, 5) == 8
    assert adicao(-1, 1) == 0
    assert adicao(0, 0) == 0

def test_subtracao():
    assert subtracao(10, 5) == 5
    assert subtracao(-1, 1) == -2
    assert subtracao(0, 0) == 0

def test_multiplicacao():
    assert multiplicacao(3, 5) == 15
    assert multiplicacao(-1, 1) == -1
    assert multiplicacao(0, 5) == 0

def test_divisao():
    assert divisao(10, 5) == 2
    assert divisao(-10, 2) == -5
    assert divisao(0, 5) == 0

    with pytest.raises(ValueError):
        divisao(10, 0)

