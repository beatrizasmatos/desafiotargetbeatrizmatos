def calcula_fibonacci(n):
    a , b = 0 , 1
    while b < n:
        a ,b = b , a + b
    print( f"O Número {n} {'pertence'  if b == n else 'não pertence'} a sequência de Fibonacci")
n = 13
calcula_fibonacci(n)