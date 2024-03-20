# test_verificador_senhas.py
import pytest
from verificador_senhas import verificar_senha_segura

def test_verificar_senha_segura():
    # Senhas seguras
    assert verificar_senha_segura("Senha@123") == True
    assert verificar_senha_segura("MinhaSenha@2022") == True
    assert verificar_senha_segura("123Senha@") == True
    
    # Senhas inseguras (não atendem a todos os critérios)
    assert verificar_senha_segura("senha123") == False  # sem caracteres especiais
    assert verificar_senha_segura("SENHA@123") == False  # sem letras minúsculas
    assert verificar_senha_segura("S@1") == False  # muito curta
    assert verificar_senha_segura("Senha Sem Caracteres Especiais") == False  # sem caracteres especiais
