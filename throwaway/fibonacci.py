__author__ = 'Aristide'

def fib(x):
    return (x if x<2 else fib(x-1)+fib(x-2))

print fib (9)
