# test_sistema_reservas.py
import pytest
from sistema_reservas import SistemaReservas

def test_sistema_reservas():
    sistema = SistemaReservas()

    # Adicionar voos
    sistema.adicionar_voo("São Paulo", "Rio de Janeiro", "2024-03-25", 100)
    sistema.adicionar_voo("Rio de Janeiro", "São Paulo", "2024-03-26", 50)

    # Pesquisar voos
    assert sistema.pesquisar_voos("São Paulo", "Rio de Janeiro", "2024-03-25") == 100
    assert sistema.pesquisar_voos("Rio de Janeiro", "São Paulo", "2024-03-26") == 50
    assert sistema.pesquisar_voos("São Paulo", "Rio de Janeiro", "2024-03-26") == 0

    # Fazer reserva
    assert sistema.fazer_reserva("São Paulo", "Rio de Janeiro", "2024-03-25", 2) == True
    assert sistema.fazer_reserva("Rio de Janeiro", "São Paulo", "2024-03-26", 60) == False

    # Visualizar reservas
    assert sistema.visualizar_reservas() == {("São Paulo", "Rio de Janeiro", "2024-03-25"): 2}

    # Cancelar reserva
    assert sistema.cancelar_reserva("São Paulo", "Rio de Janeiro", "2024-03-25", 1) == True
    assert sistema.visualizar_reservas() == {("São Paulo", "Rio de Janeiro", "2024-03-25"): 1}

class SistemaReservas:
    def __init__(self):
        self.voos_disponiveis = {}
        self.reservas = {}

    def adicionar_voo(self, origem, destino, data, numero_de_assentos):
        chave = (origem, destino, data)
        self.voos_disponiveis[chave] = numero_de_assentos

    def pesquisar_voos(self, origem, destino, data):
        chave = (origem, destino, data)
        if chave in self.voos_disponiveis:
            return self.voos_disponiveis[chave]
        else:
            return 0

    def fazer_reserva(self, origem, destino, data, assentos):
        chave = (origem, destino, data)
        if chave in self.voos_disponiveis:
            if self.voos_disponiveis[chave] >= assentos:
                if chave not in self.reservas:
                    self.reservas[chave] = assentos
                else:
                    self.reservas[chave] += assentos
                self.voos_disponiveis[chave] -= assentos
                return True
        return False

    def visualizar_reservas(self):
        return self.reservas

    def cancelar_reserva(self, origem, destino, data, assentos):
        chave = (origem, destino, data)
        if chave in self.reservas and self.reservas[chave] >= assentos:
            self.reservas[chave] -= assentos
            self.voos_disponiveis[chave] += assentos
            return True
        return False
