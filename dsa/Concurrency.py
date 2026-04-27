"""
Concurrency basics in Python
threading
Lock
race condition
GIL basics
when to use multiprocessing instead of threads
"""

from threading import Lock

class Counter:
    def __init__(self):
        self.value = 0
        self.lock = Lock()

    def increment(self):
        with self.lock:
            self.value += 1

