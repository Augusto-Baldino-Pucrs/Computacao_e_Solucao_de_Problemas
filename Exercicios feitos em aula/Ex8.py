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

cont = 0  
for k in range(10000):
    J = gerarListaRepeticao(6, 1, 10, 1)
    Jp = [x for x in J if x % 2 == 0]  
    if len(Jp) == 6:  
        cont += 1 

print(f'{cont}')  # Exibe o resultado final




