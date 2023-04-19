def define_posicoes(linha,coluna,orientacao,tamanho):
    grid=[0]*10
    Tabuleiro = [grid]*10
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
