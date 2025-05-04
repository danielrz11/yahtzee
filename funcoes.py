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

def calcula_pontos_sequencia_baixa(dadosrolados):                   
    if 1 in dadosrolados and 2 in dadosrolados and 3 in dadosrolados and 4 in dadosrolados:  
        return 15
    if 2 in dadosrolados and 3 in dadosrolados and 4 in dadosrolados and 5 in dadosrolados:
        return 15
    if 3 in dadosrolados and 4 in dadosrolados and 5 in dadosrolados and 6 in dadosrolados:
        return 15
    else:
        return 0

def calcula_pontos_sequencia_alta(dadosrolados):
    if 2 in dadosrolados and 3 in dadosrolados and 4 in dadosrolados and 5 in dadosrolados and 6 in dadosrolados:
        return 30
    if 1 in dadosrolados and 2 in dadosrolados and 3 in dadosrolados and 4 in dadosrolados and 5 in dadosrolados:
        return 30
    else:
        return 0 

def calcula_pontos_full_house(dadosrolados):
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
            s2 += 1
        elif dado == 3:
            s3 += 1
        elif dado == 4:
            s4 += 1
        elif dado == 5:
            s5 += 1
        elif dado == 6:
            s6 += 1
    listaquantdados = [s1,s2,s3,s4,s5,s6]
    if 3 in listaquantdados and 2 in listaquantdados:
        return s1*1 + s2*2 + s3*3 + s4*4 + s5*5 + s6*6
    else:
        return 0

def calcula_pontos_quadra(dadosrolados):
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
            s2 += 1
        elif dado == 3:
            s3 += 1
        elif dado == 4:
            s4 += 1
        elif dado == 5:
            s5 += 1
        elif dado == 6:
            s6 += 1
    listaquantdados = [s1,s2,s3,s4,s5,s6]
    m = 0
    for i in listaquantdados:
        if i > m:
            m = i
    if m >= 4:
        return s1*1 + s2*2 + s3*3 + s4*4 + s5*5 + s6*6 
    else:
        return 0

def calcula_pontos_quina(dadosrolados):
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
            s2 += 1
        elif dado == 3:
            s3 += 1
        elif dado == 4:
            s4 += 1
        elif dado == 5:
            s5 += 1
        elif dado == 6:
            s6 += 1
    listaquantdados = [s1,s2,s3,s4,s5,s6]
    m = 0
    for i in listaquantdados:
        if i > m:
            m = i
    if m >= 5:
        return 50 
    else:
        return 0

def calcula_pontos_regra_avancada(dadosrolados):
    ra = {'sem_combinacao':calcula_pontos_soma(dadosrolados),
          'sequencia_baixa':calcula_pontos_sequencia_baixa(dadosrolados),
          'sequencia_alta':calcula_pontos_sequencia_alta(dadosrolados),
          'full_house':calcula_pontos_full_house(dadosrolados),
          'quadra':calcula_pontos_quadra(dadosrolados),
          'cinco_iguais':calcula_pontos_quina(dadosrolados)}
    return ra

def faz_jogada(dados, categoria,cartela):
    if categoria == '1':
        cartela['regra_simples'][1] = calcula_pontos_regra_simples(dados)[1]
    elif categoria == '2':
        cartela['regra_simples'][2] = calcula_pontos_regra_simples(dados)[2]
    elif categoria == '3':
        cartela['regra_simples'][3] = calcula_pontos_regra_simples(dados)[3]
    elif categoria == '4':
        cartela['regra_simples'][4] = calcula_pontos_regra_simples(dados)[4]
    elif categoria == '5':
        cartela['regra_simples'][5] = calcula_pontos_regra_simples(dados)[5]
    elif categoria == '6':
        cartela['regra_simples'][6] = calcula_pontos_regra_simples(dados)[6]

    elif categoria == 'sem_combinacao':
        cartela['regra_avancada']['sem_combinacao'] = calcula_pontos_regra_avancada(dados)['sem_combinacao']
    elif categoria == 'sequencia_baixa':
        cartela['regra_avancada']['sequencia_baixa'] = calcula_pontos_regra_avancada(dados)['sequencia_baixa']
    elif categoria == 'sequencia_alta':
        cartela['regra_avancada']['sequencia_alta'] = calcula_pontos_regra_avancada(dados)['sequencia_alta']
    elif categoria == 'full_house':
        cartela['regra_avancada']['full_house'] = calcula_pontos_regra_avancada(dados)['full_house']
    elif categoria == 'quadra': 
        cartela['regra_avancada']['quadra'] = calcula_pontos_regra_avancada(dados)['quadra']
    elif categoria == 'cinco_iguais':
        cartela['regra_avancada']['cinco_iguais'] = calcula_pontos_regra_avancada(dados)['cinco_iguais']

    return cartela
