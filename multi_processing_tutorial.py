# Program:
#
# Programs are piece of code, developed to automate certain tasks, typically stored on disk or in
# non-volatile memory in a form that can be executed by your computer. When a program is run, it is loaded
# into memory in binary form. The computer's CPU understands only Binary instructions.
#
# Process
# When a program is loaded into the memory along with the resources and dependencies that enable it operate, is
# called a process. The OS is the brain behind allocation of resources. There can be multiple instances of the same
# program and each instance of that running program is a process. Each process has a separate memory address
# space. Therefore, each process runs independently and is isolated from other processes.
#
# Threads
# A thread is the unit of execution within a process. A process can have multiple threads. When a process
# starts, it is assigned memory and resources. Each thread in the process shares the memory and resources.
# Each thread will have its own stack, however all threads in a process will share the heap. Since threads share
# the same address space, operational cost for communication between the threads is low. However, one therad in a
# process will impact other threads, causing unexpected behavior.
#
# Threads
#
import time
import logging
import multiprocessing

from os import getpid
from queue import Queue
from threading import Thread
from logging.handlers import QueueListener, QueueHandler
from multiprocessing import Pool, Process, Lock, Value


def inspect_func(i):
    print("I'm executed in process {}".format(getpid()))
    return i * 2


def add_100_no_mp(total):
    for i in range(100):
        time.sleep(0.01)
        total = total + 1
    return total


def sub_100_no_mp(total):
    for i in range(100):
        time.sleep(0.01)
        total = total - 1
    return total


def add_100_no_lock(total):
    for i in range(100):
        time.sleep(0.01)
        total.value = total.value + 1
    # return total


def sub_100_no_lock(total):
    for i in range(100):
        time.sleep(0.01)
        total.value = total.value - 1
    # return total


def add_100_lock(total, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        total.value = total.value + 1
        lock.release()
    # return total


def sub_100_lock(total, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        total.value = total.value - 1
        lock.release()
    # return total


def setup_logging():
    # Logs get written to a queue, and then a thread reads
    # from that queue and writes messages to a file:
    _log_queue = Queue()
    QueueListener(_log_queue, logging.FileHandler("out.log")).start()
    logging.getLogger().addHandler(QueueHandler(_log_queue))

    # Our parent process is running a thread that
    # logs messages:
    def write_logs():
        while True:
            logging.error("hello, I just did something")

    Thread(target=write_logs).start()


def runs_in_subprocess():
    print("About to log...")
    logging.error("hello, I did something")
    print("...logged")


if __name__ == "__main__":
    # print(multiprocessing.cpu_count())
    # with Pool(2) as pool:
    # res = pool.map(inspect_func, [1, 2, 3, 4])
    # print(res)
    # total = Value("i", 500)
    # lock = Lock()
    # print(f"Starting point: {total}")
    # total = add_100_no_mp(total)
    # print(f"after adding: {total}")
    # total = sub_100_no_mp(total)
    # print(f"after sub: {total}")
    # add_process = Process(target=add_100_no_lock, args=(total,))
    # sub_process = Process(target=sub_100_no_lock, args=(total,))
    # add_process = Process(target=add_100_lock, args=(total, lock))
    # sub_process = Process(target=sub_100_lock, args=(total, lock))

    # add_process.start()
    # sub_process.start()

    # add_process.join()
    # sub_process.join()

    # print(total.value)
    setup_logging()
    while True:
        with Pool() as pool:
            pool.apply(runs_in_subprocess)

