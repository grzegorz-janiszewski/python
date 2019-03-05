def fib(x):
    if x > 2:
        return fib(x-2) + fib(x-1)
    else:
        return 1

print(fib(3))
print(fib(6))
print(fib(13))