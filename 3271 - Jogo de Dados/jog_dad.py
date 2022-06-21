# Monta os quatro dados do jogo.
def monta_dado(a: int, b: int):
    c = 0
    dado = []
    while c < (b-a+1):
        dado.append(a+c)
        c+=1
    return dado

# Define o ganhador
def ganhador(dados: dict):
    # Primeiro montamos uma lista com todas as somas possíveis nos dados de Gunnar
    sum_lis_G = []    
    for e1 in dados['Dado_G1']:
        for e2 in dados['Dado_G2']:
            sum_lis_G.append(e1+e2)
    
    # Depois montamos uma lista com todas as somas possíveis nos dados de Emma
    sum_lis_E = []
    for e1 in dados['Dado_E1']:
        for e2 in dados['Dado_E2']:
            sum_lis_E.append(e1+e2)
    
    # Verificação de quem tem mais chances de vencer. 
    #   Para isto, comparamos todos os cenários possíveis da disputa, 
    #   adicionando 1 ponto cada vez que um jogador ganhar a comparação.
    pontos_Gunnar = 0
    pontos_Emma = 0
    for eG in sum_lis_G:
        for eE in sum_lis_E:
            if eG > eE:
                pontos_Gunnar += 1
            elif eE > eG:
                pontos_Emma += 1    

    # Verificamos quem ganha na maioria dos cenários.
    if pontos_Gunnar > pontos_Emma:
        ganhador = "Gunnar"
    elif pontos_Emma > pontos_Gunnar:
        ganhador = "Emma"
    else:
        ganhador = "Tie"

    # Retornamos o ganhador mais provável.
    return ganhador

try:
    # Recebendo as entradas do problema.
    entradaG = input().split()
    a1, b1, a2, b2 = list(map(int, entradaG))
    entradaE = input().split()
    a3, b3, a4, b4 = list(map(int, entradaE))

    # Verificação de entradas na faixa permitida pelo exercício. 
    if a1 not in list(range(1, 98))\
        or a2 not in list(range(1, 98))\
        or a3 not in list(range(1, 98))\
        or a4 not in list(range(1, 98)):
            print ("Os valores de 'a' devem estar entre 1 e 97!")
    elif b1 not in list(range(4, 101))\
        or b2 not in list(range(4, 101))\
        or b3 not in list(range(4, 101))\
        or b4 not in list(range(4, 101)):
            print ("Os valores de 'b' devem estar entre 4 e 100!")
    elif b1<(a1+3) or b2<(a2+3) or b3<(a3+3) or b4<(a4+3):
        print ("Os dados devem ter pelo menos 4 lados!")
    else:
        # Montagem de um dicionário com os elementos dos 2 dados de cada jogador.
        dados = {
                    "Dado_G1": monta_dado(a1, b1),
                    "Dado_G2": monta_dado(a2,b2),
                    "Dado_E1": monta_dado(a3,b3),
                    "Dado_E2": monta_dado(a4,b4)        
                }
        print (ganhador(dados))

except ValueError:
    print ("Insira apenas números inteiros, "+
            "escrevendo quatro na primeira linha e mais quatro na segunda!")
