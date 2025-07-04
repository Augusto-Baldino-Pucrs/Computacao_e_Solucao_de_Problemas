from random import randint                                                                          

def comparaAcertos(seuJogo,jogoLotoFacil):
    acertos = 0
    for i in range(len(seuJogo)):
        if(seuJogo[i] == jogoLotoFacil[i]):
            acertos+=1
    
    return acertos

def gerarLista(n, nInicio, nFim):                                                                           
    numeros = []                                                                            
    for i in range(n):                                                                          
        numeros.append(randint(nInicio, nFim))                                                                          
    numeros.sort()                                                                          
    return numeros  

if __name__ == '__main__':
    seuJogo = [1,2,3,4,5,6]
    jogoLotoFacil = gerarLista(6,1,10)
    
    print(f' o números de acertos do seu jogo, em comparação ao do jogo da loto fácil foi {comparaAcertos(seuJogo,jogoLotoFacil)} acertos')
