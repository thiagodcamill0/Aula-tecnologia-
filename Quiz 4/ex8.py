import pytest
from validador_telefone import validar_telefone

def test_validar_telefone():
    # Telefones válidos
    assert validar_telefone("(11) 91234-5678") == True
    assert validar_telefone("(55) 99321-6547") == True
    assert validar_telefone("(21) 2345-6789") == True
    
    # Telefones inválidos
    assert validar_telefone("123") == False  # muito curto
    assert validar_telefone("(11) 12345-6789") == False  # DDD incorreto
    assert validar_telefone("(11) 9123-45678") == False  # formato incorreto
    assert validar_telefone("(11) 91234-567") == False  # formato incorreto


def validar_telefone(telefone):
    # Expressão regular para validar o formato do telefone
    # Vamos considerar o formato padrão brasileiro: (XX) XXXX-XXXX ou (XX) 9XXXX-XXXX
    # Onde X é um dígito de 0 a 9
    padrao = r'^\([1-9]{2}\) (?:[2-8]|9[1-9])[0-9]{3}\-[0-9]{4}$'
    
    # Verifica se o telefone corresponde ao padrão
    return bool(re.match(padrao, telefone))