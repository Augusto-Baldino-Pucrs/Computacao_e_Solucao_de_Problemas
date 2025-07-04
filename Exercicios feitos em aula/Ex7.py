from random import randint                                                                          
                                                                            
def gerarLista(n, nInicio, nFim):                                                                           
    numeros = []                                                                            
    for i in range(n):                                                                          
        numeros.append(randint(nInicio, nFim))                                                                          
    numeros.sort()                                                                          
    return numeros                                                                          
                                                                            
def gerarListaRepeticao(n, nInicio, nFim, rep):                                                                         
    numeros = []                                                                            
                                                                            
    if rep == 1:                                                                            
        numeros = gerarLista(n, nInicio, nFim)                                                                          
    else:                                                                           
        while len(numeros) < n:                                                                         
            numero = randint(nInicio, nFim)                                                                         
            if numero not in numeros:                                                                           
                numeros.append(numero)                                                                          
                                                                            
    numeros.sort()                                                                          
    return numeros                                                                          
                                                                            
print(gerarLista(5, 1, 10))                                                                         
print(gerarListaRepeticao(5, 1, 10, 1))                                                                             
print(gerarListaRepeticao(5, 1, 10, 0))                                                                         
