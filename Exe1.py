def fibo(n):
    a = 0
    b = 1
    while a <= n:
        if a == n:
            return True
        a, b = b, a + b
    return False
    


n = int(input("Informe o numero para a Fibonacci:"))

if fibo(n) == True:
    print("Onumero pertence a Fibonacci")
else:
    print("O numero não pertence a Fibonacci")