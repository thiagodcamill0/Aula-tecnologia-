# test_conversor_moedas.py
import pytest
from conversor_moedas import dolares_para_euro, real_para_dolares, euro_para_real

def test_dolares_para_euro():
    assert dolares_para_euro(100) == 85
    assert dolares_para_euro(50) == 42.5
    assert dolares_para_euro(0) == 0

def test_real_para_dolares():
    assert real_para_dolares(100) == 19
    assert real_para_dolares(50) == 9.5
    assert real_para_dolares(0) == 0

def test_euro_para_real():
    assert euro_para_real(100) == 529
    assert euro_para_real(50) == 264.5
    assert euro_para_real(0) == 0


def dolares_para_euro(valor_em_dolares):
    return valor_em_dolares * 0.85  # taxa de conversão atual (apenas um exemplo)

def real_para_dolares(valor_em_reais):
    return valor_em_reais * 0.19  # taxa de conversão atual (apenas um exemplo)

def euro_para_real(valor_em_euro):
    return valor_em_euro * 5.29  # taxa de conversão atual (apenas um exemplo)