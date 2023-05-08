def define_posicoes(linha,coluna,orientacao,tamanho):
        origem = [linha, coluna]
        posiçoes_do_barco = []
        if orientacao == 'vertical':
            for e in range(tamanho): 
                origem = [linha, coluna]
                posiçoes_do_barco.append(origem)
                linha+=1
        if orientacao == 'horizontal':
            for e in range(tamanho): 
                origem = [linha, coluna]
                posiçoes_do_barco.append(origem)
                coluna+=1
        return posiçoes_do_barco



def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    if nome_navio not in frota:
         
         frota[nome_navio] = []

    frota[nome_navio].append(define_posicoes(linha,coluna,orientacao,tamanho))

    return frota
#Faz jogada 
def faz_jogada(tabuleiro,linha,coluna):
    if tabuleiro[linha][coluna]== 1:
        tabuleiro[linha][coluna] ='X'
    else:
        tabuleiro[linha][coluna] ='-'
    return tabuleiro
#posiciona frota

def posiciona_frota(frota):
    
    tabuleiro = [[0,0,0,0,0,0,0,0,0,0,],[0,0,0,0,0,0,0,0,0,0,],[0,0,0,0,0,0,0,0,0,0,],[0,0,0,0,0,0,0,0,0,0,],[0,0,0,0,0,0,0,0,0,0,],[0,0,0,0,0,0,0,0,0,0,],[0,0,0,0,0,0,0,0,0,0,],[0,0,0,0,0,0,0,0,0,0,],[0,0,0,0,0,0,0,0,0,0,],[0,0,0,0,0,0,0,0,0,0,]]
    posicao = []
    for chave in frota:
        posicao.append(frota[chave][0])
        if len(frota[chave])>1:
            for k in range(1 , len(frota[chave])):
                posicao.append(frota[chave][k])
    for e in range(len(tabuleiro)):
        for i in range(len(tabuleiro)):
            for j in range(len(posicao)):
                if [e,i] in posicao[j]:

                    tabuleiro[e][i] = 1
                    break
                else:
                    tabuleiro[e][i] = 0

        
    return tabuleiro
# afundados
def afundados(frota,tabuleiro):
    navios_afundados = 0 
    destruidos = []
    posiçao = []
    r= 0
    for chave in frota:
        posiçao.append(frota[chave][0])
        if len(frota[chave])>1:
            for k in range(1 , len(frota[chave])):
                posiçao.append(frota[chave][k])
    for e in range (len (tabuleiro)):
        for i in range (len (tabuleiro)):
            if tabuleiro[e][i] == 'X':
                for j in range(len(posiçao)):
                    if [e,i] in posiçao[j]:
                        destruidos.append([e,i])
                        break
    for chave in frota: 
        for k in range (len(frota[chave])):
            r = 0
            for n in destruidos:
                if n in frota[chave][k]:
                    r+=1
                    if r == len (frota[chave][k]):
                        navios_afundados += 1
                        r = 0
    return navios_afundados

# Posição válida
def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    for e in define_posicoes(linha,coluna,orientacao,tamanho):
        if e[0]>9 or e[1]>9:
            return False
        for nome in frota:
            posiçao = frota[nome]
            for barco in posiçao:
                for coordenada in barco:
                    if coordenada == e:
                        return False
    return True 


# posicionando frota



jogando =True
jogadas = []
frota_oponente = {'porta-aviões': [[[9, 1], [9, 2], [9, 3], [9, 4]]],'navio-tanque': [[[6, 0], [6, 1], [6, 2]],[[4, 3], [5, 3], [6, 3]]],'contratorpedeiro': [[[1, 6], [1, 7]],[[0, 5], [1, 5]],[[3, 6], [3, 7]]],'submarino': [[[2, 7]],[[0, 6]],[[9, 7]],[[7, 6]]]}

frota_tamanho = {"porta-aviões":{'quantidade':1,'tamanho':4},"navio-tanque":{'quantidade':2,'tamanho':3},"contratorpedeiro":{'quantidade':3,'tamanho':2},"submarino":{'quantidade':4,'tamanho':1}}
frota = {}
lista= []
orientacao = 0
for nome in frota_tamanho:
    i=0
    lista = []
    while i <(frota_tamanho[nome]['quantidade']):
        tamanho = frota_tamanho[nome]['tamanho']
        print(f'Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}')
        linha = int(input("linha: "))
        coluna = int(input("coluna: "))
        if nome != 'submarino':
            orientacao = int(input("Orientação: "))
        if orientacao == 1:
            orientacao = 'vertical'
        if orientacao == 2:
            orientacao = 'horizontal'
        if posicao_valida(frota, linha, coluna, orientacao, tamanho) == True:
            lista.append(define_posicoes(linha,coluna,orientacao,tamanho))
            frota[nome] = lista
            i+=1
        elif posicao_valida(frota, linha, coluna, orientacao, tamanho) == False:
            print('Esta posição não está válida!')


tabuleiro_oponente = posiciona_frota(frota_oponente)




def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto


while jogando:
    print(monta_tabuleiros(posiciona_frota(frota),tabuleiro_oponente))
    invalido =True
    while invalido:
        LinhaA = int(input("Jogador, qual linha deseja atacar? "))
        if LinhaA < 0 or LinhaA > 9:
            print('Linha inválida!')
        else:
            invalido = False
    invalido = True
    while invalido:
        ColunaA = int(input("Jogador, qual coluna deseja atacar? "))
        if ColunaA < 0 or ColunaA > 9:
            print('Linha inválida!')
        else:
            invalido = False
    
    if [LinhaA,ColunaA] in jogadas:
           
        print(f'A posição linha {LinhaA} e coluna {ColunaA} já foi informada anteriormente!')
    else:
        jogadas.append([LinhaA,ColunaA])

        tabuleiro_oponente = faz_jogada(tabuleiro_oponente,LinhaA,ColunaA)

        

        if afundados(frota_oponente,tabuleiro_oponente)== 10:
            print('Parabéns! Você derrubou todos os navios do seu oponente!')
            jogando = False