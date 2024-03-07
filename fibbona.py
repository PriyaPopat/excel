def fibonacci(n):
    fib_sequence=[0,1]
    while len(fib_sequence)<n:
        fib_sequence.append(fib_sequence[-1]+fib_sequence[-2])
    return fib_sequence

result_fibonacci=fibonacci(8)
print(result_fibonacci)




