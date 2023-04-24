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

    