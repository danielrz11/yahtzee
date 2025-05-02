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
