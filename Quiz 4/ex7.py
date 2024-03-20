# diferenca_datas.py
from datetime import datetime

def diferenca_entre_datas(data1, data2, unidade="dias"):
    formato = "%Y-%m-%d %H:%M:%S"
    data1 = datetime.strptime(data1, formato)
    data2 = datetime.strptime(data2, formato)

    diferenca = data2 - data1

    if unidade == "dias":
        return diferenca.days
    elif unidade == "meses":
        return diferenca.days // 30
    elif unidade == "anos":
        return diferenca.days // 365
    elif unidade == "horas":
        return diferenca.total_seconds() // 3600
    elif unidade == "minutos":
        return diferenca.total_seconds() // 60
    else:
        raise ValueError("Unidade de medida inválida")

# test_diferenca_datas.py
import pytest
from diferenca_datas import diferenca_entre_datas

def test_diferenca_dias():
    assert diferenca_entre_datas("2024-03-20 12:00:00", "2024-03-22 12:00:00", "dias") == 2

def test_diferenca_meses():
    assert diferenca_entre_datas("2024-03-20 12:00:00", "2024-05-20 12:00:00", "meses") == 2

def test_diferenca_anos():
    assert diferenca_entre_datas("2024-03-20 12:00:00", "2026-03-20 12:00:00", "anos") == 2

def test_diferenca_horas():
    assert diferenca_entre_datas("2024-03-20 12:00:00", "2024-03-21 12:00:00", "horas") == 24

def test_diferenca_minutos():
    assert diferenca_entre_datas("2024-03-20 12:00:00", "2024-03-20 12:30:00", "minutos") == 30

def test_unidade_invalida():
    with pytest.raises(ValueError):
        diferenca_entre_datas("2024-03-20 12:00:00", "2024-03-22 12:00:00", "semanas")

# Chamada para teste de unidade inválida
