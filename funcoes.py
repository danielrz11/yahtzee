def rolar_dados(nd):
    from random import randint
    return [randint(1, 6) for _ in range(nd)]

def guardar_dado(dadosrolados,dadosestoque,dadoparaguardar):
    dadosestoque.append(dadosrolados[dadoparaguardar])
    del dadosrolados[dadoparaguardar]
    return [dadosrolados,dadosestoque]

def remover_dado(dadosrolados,dadosestoque,dadopararemover):
    dadosrolados.append(dadosestoque[dadopararemover])
    del dadosestoque[dadopararemover]
    return [dadosrolados,dadosestoque]

def calcula_pontos_regra_simples(dadosrolados):
    s1 = 0
    s2 = 0
    s3 = 0
    s4 = 0
    s5 = 0
    s6 = 0
    for dado in dadosrolados:
        if dado == 1:
            s1 += 1
        elif dado == 2:
            s2 += 2
        elif dado == 3:
            s3 += 3
        elif dado == 4:
            s4 += 4
        elif dado == 5:
            s5 += 5
        elif dado == 6:
            s6 += 6
    somasimples = {1:s1, 2:s2, 3:s3, 4:s4, 5:s5, 6:s6}
    return somasimples

def calcula_pontos_soma(dadosrolados):
    soma = 0
    for dado in dadosrolados:
        soma += dado
    return soma
