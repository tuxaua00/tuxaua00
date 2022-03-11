print('Seja bem vindo!\n')

def fib(n):
    if n > 1:
        return fib(n-1) + fib(n-2)
    return n

for i in range(15):
    print(fib(i))

