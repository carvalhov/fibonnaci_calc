def fibonnaci(num: int):
    fib = []
    fib.append(0)
    fib.append(1)
    for i in range(2, num):
        fib.append(fib[i-2] + fib[i-1])
    return print(fib)
