def fibonacci(n):
    if n <= 0:
        raise RuntimeError()
    else:
        fibonacci_list = []
        fib1 = fib2 = 1
        fibonacci_list.append(fib1)
        fibonacci_list.append(fib2)

        for i in range(2, n):
            fib1, fib2 = fib2, fib1 + fib2
            fibonacci_list.append(fib2)
        return fibonacci_list
