from datetime import datetime
from multiprocessing import Queue, Process, Pipe
from multiprocessing.connection import Connection

import codecs
import time


def A(in_queue: Queue, out_pipe: Connection):
    while True:
        time.sleep(5)
        out_pipe.send(in_queue.get().lower())


def B(in_pipe: Connection, out_pipe: Connection):
    while True:
        out_pipe.send(codecs.encode(in_pipe.recv(), "rot13"))


if __name__ == '__main__':
    with open('artifacts/hard.txt', 'w') as file:
        main_to_a = Queue()
        a_to_b, b_to_a = Pipe()
        b_to_main, main_to_b = Pipe()
        Process(target=A, args=(main_to_a, a_to_b), daemon=True).start()
        Process(target=B, args=(b_to_a, b_to_main), daemon=True).start()
        while True:
            msg = input('To exit type "exit"\nInput: ')
            print()
            if msg == 'exit':
                file.write(f'End: {datetime.now()}\n')
                break
            file.write(f'Input: "{msg}"\tdate: {datetime.now()}\n')
            main_to_a.put(msg)
            msg = main_to_b.recv()
            file.write(f'Output: "{msg}"\tdate: {datetime.now()}\n')
