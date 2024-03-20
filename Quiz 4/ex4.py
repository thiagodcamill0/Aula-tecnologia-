# test_validador_emails.py
import pytest
from validador_emails import validar_email

def test_validar_email():
    # E-mails válidos
    assert validar_email("usuario@example.com") == True
    assert validar_email("nome.sobrenome@example.com") == True
    assert validar_email("usuario123@example.com") == True
    assert validar_email("usuario+algo@example.com") == True
    
    # E-mails inválidos
    assert validar_email("usuario@example") == False  # domínio incompleto
    assert validar_email("usuario@example.") == False  # domínio incompleto
    assert validar_email("usuarioexample.com") == False  # sem '@'
    assert validar_email("usuario@examplecom") == False  # domínio inválido
    assert validar_email("usuario@.com") == False  # domínio inválido
