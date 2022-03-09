import time
from multiprocessing import Process
from threading import Thread

N = 10000
threads_number = 10


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


def count_time_sync():
    start = time.time()
    for _ in range(threads_number):
        fibonacci(N)
    return time.time() - start


def count_threads_time():
    threads = [Thread(target=fibonacci, args=(N,)) for _ in range(threads_number)]
    start = time.time()
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return time.time() - start


def count_process_time():
    process = [Process(target=fibonacci, args=(N,)) for _ in range(threads_number)]
    start = time.time()
    for p in process:
        p.start()
    for p in process:
        p.join()
    return time.time() - start


if __name__ == '__main__':
    with open('artifacts/easy.txt', 'w') as file:
        file.write('sync time: ' + str(count_time_sync()) + '\n')
        file.write('threads time: ' + str(count_threads_time()) + '\n')
        file.write('processes time: ' + str(count_process_time()) + '\n')
