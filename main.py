# funcao 1 print

produto = "iphone"
quantidade_estoque = 200

print("O produto", produto, "tem", quantidade_estoque, "unidades no estoque.")
print("O produto", produto, "tem", quantidade_estoque, "unidades no estoque.", sep=";")

import time

print("Contagem")
for i in range(5):
    # print(5 - i)
    # print(5 - i, end="\n")
    print(5 - i, end="\r")
    time.sleep(1)
print("Acabou")

# funcao 2 help

help(print)

def calcular_imposto(faturamento, taxa):
    """
    faturamento (float): o faturamento da empresa que vamos calcular o imposto
    taxa (float): a taxa percentual de imposto sobre o faturamento (ex: 0.2)

    returns: imposto, faturamento_liquido
    imposto (float): valor total do imposto calculado sobre o faturamento
    faturamento_liquido (float): quanto sobrou do faturamento depois de descontado o imposto"""
    imposto = faturamento * taxa
    return imposto, faturamento - imposto

help(calcular_imposto)

# funcao 3 range

lista = list(range(5))
lista = list(range(1, 6))
lista = list(range(1, 10, 2))
lista = list(range(5, 0, -1))

print(lista)

import time
for i in range(5, 0, -1):
    print(i, end="/r")
    time.sleep(1)

# funcao 4 map

salarios = [1000, 5000, 7000, 850]

def aumentar_salario(salario):
    if salario > 3000:
        novo_salario = salario * 1.08
    else:
        novo_salario = salario * 1.1
    return novo_salario

novos_salarios = list(map(aumentar_salario, salarios))


