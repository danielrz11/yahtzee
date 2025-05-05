from funcoes import *

cartela = {
    'regra_simples': {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1},
    'regra_avancada': {
        'sem_combinacao': -1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}

imprime_cartela(cartela)
for rodada in range(12):
    dados_rolados = rolar_dados(5)
    dados_guardados = []
    rerrolagens = 0

    while True:
        print("Dados rolados:", dados_rolados)
        print("Dados guardados:", dados_guardados)
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        acao = input()

        while acao not in ["1","2","3","4","0"]:
            print("Opção inválida. Tente novamente.")
            acao = input()

        if acao == "1":
            print("Digite o índice do dado a ser guardado (0 a 4):")
            indice = int(input())
            if indice >= 0 and indice < len(dados_rolados):
                resultado = guardar_dado(dados_rolados, dados_guardados, indice)
                dados_rolados = resultado[0]
                dados_guardados = resultado[1]
            else:
                print("Índice inválido.")
        elif acao == "2":
            print("Digite o índice do dado a ser removido (0 a 4):")
            indice = int(input())
            if indice >= 0 and indice < len(dados_guardados):
                resultado = remover_dado(dados_rolados, dados_guardados, indice)
                dados_rolados = resultado[0]
                dados_guardados = resultado[1]
            else:
                print("Índice inválido.")
        elif acao == "3":
            if rerrolagens < 2:
                rerrolagens += 1
                dados_rolados = rolar_dados(5 - len(dados_guardados))
            else:
                print("Você já usou todas as rerrolagens.")
        elif acao == "4":
            imprime_cartela(cartela)
        elif acao == "0":
            print("Digite a combinação desejada:")
            while True:
                categoria = input()
                if categoria in ["1", "2", "3", "4", "5", "6"]:
                    if cartela["regra_simples"][int(categoria)] != -1:
                        print("Essa combinação já foi utilizada.")
                    else:
                        break
                    
                elif categoria in cartela["regra_avancada"]:
                    if cartela["regra_avancada"][categoria] != -1:
                        print("Essa combinação já foi utilizada.")
                    else:
                        break
                else:
                    print("Combinação inválida. Tente novamente.")

            dados = dados_guardados + dados_rolados
            faz_jogada(dados, categoria, cartela)
            break
        else:
            print("error")

imprime_cartela(cartela)

total = 0
simples = 0

for i in [1, 2, 3, 4, 5, 6]:
    if cartela["regra_simples"][i] != -1:
        simples += cartela["regra_simples"][i]
        total += cartela["regra_simples"][i]

for nome in ['sem_combinacao', 'quadra', 'full_house', 'sequencia_baixa', 'sequencia_alta', 'cinco_iguais']:
    if cartela["regra_avancada"][nome] != -1:
        total += cartela["regra_avancada"][nome]

if simples >= 63:
    total += 35

print("Pontuação total:", total)