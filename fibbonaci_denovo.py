print('Seja bem vindo!\n')

def fib(n):
    if n > 1:
        return fib(n-1) + fib(n-2)
    return n

for i in range(50):
    if fib(i) < 500:
        print(fib(i))
    else:
        break


