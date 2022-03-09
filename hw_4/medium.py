from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

import concurrent
import math
import multiprocessing as mp
import time


def integrate(f, a, b, job=0, n_jobs=1, n_iter=10000):
    result = 0
    start_time = time.time()
    start = job * (n_iter // n_jobs)
    end = min(n_iter, (job + 1) * (n_iter // n_jobs))
    for i in range(start, end):
        result += f(a + i * (b - a) / n_iter) * (b - a) / n_iter
    return result, f'\tJob: {job}, start: {start_time}, iterate: {start} - {end}, result: {result}\n'


def count_time(f, a, b, steps, executor, log_file):
    threads = []
    start_time = time.time()
    with executor(max_workers=steps) as executor:
        result = 0
        for i in range(steps):
            threads.append(executor.submit(integrate, f, a, b, i, steps))
        for t in concurrent.futures.as_completed(threads):
            acc, log = t.result()
            result += acc
            log_file.write(log)
    log_file.write(f'Result: {result}\n\n')
    return time.time() - start_time, result


if __name__ == '__main__':
    with open('artifacts/medium_log.txt', "w") as log_file, open('artifacts/medium.txt', "w") as file:
        for steps in range(1, 2 * mp.cpu_count() + 1):
            log_file.write(f'Integration with {steps} jobs:\n')
            log_file.write(f'Thread:\n')
            time__, result = count_time(math.cos, 0, math.pi / 2, steps, ThreadPoolExecutor, log_file)
            file.write(f'Step: {steps}\n')
            file.write(f'\ttime_threads: {time__}\n')
            file.write(f'\tresult_threads: {result}\n')
            file.write(f'\t====================================\n')
            log_file.write(f'Process:\n')
            time__, result = count_time(math.cos, 0, math.pi / 2, steps, ProcessPoolExecutor, log_file)
            file.write(f'\ttime_process: {time__}\n')
            file.write(f'\tresult_process: {result}\n')
            log_file.write(f'========================================================================\n')
