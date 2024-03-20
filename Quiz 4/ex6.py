# test_contador_palavras.py
import pytest
from contador_palavras import contar_palavras

def test_contar_palavras():
    # Texto com 5 palavras
    texto_1 = "Isso é um texto de teste"
    assert contar_palavras(texto_1) == 5

    # Texto com 10 palavras
    texto_2 = "Python é uma linguagem de programação muito popular e versátil"
    assert contar_palavras(texto_2) == 10

    # Texto vazio
    texto_vazio = ""
    assert contar_palavras(texto_vazio) == 0

    # Texto com apenas uma palavra
    texto_uma_palavra = "Python"
    assert contar_palavras(texto_uma_palavra) == 1
