# test_ordenacao_lista.py
import pytest
from ordenacao_lista import ordenar_crescente, ordenar_decrescente

def test_ordenar_crescente():
    # Lista desordenada
    lista = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    
    # Ordenação crescente
    resultado = ordenar_crescente(lista)
    assert resultado == [1, 1, 2, 3, 4, 5, 5, 6, 9]

def test_ordenar_decrescente():
    # Lista desordenada
    lista = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    
    # Ordenação decrescente
    resultado = ordenar_decrescente(lista)
    assert resultado == [9, 6, 5, 5, 4, 3, 2, 1, 1]
