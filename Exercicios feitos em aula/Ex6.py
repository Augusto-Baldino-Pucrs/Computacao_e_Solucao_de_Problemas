def fibonacci(n):
    if n <= 0:
        return 0
    
    a = 1  
    b = 1  
    
    for i in range(2, n):  
        a=b
        b= a +b
    return b

n = 15
print(f"O {n}º número de Fibonacci é: {fibonacci(n)}")
    
