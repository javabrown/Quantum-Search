import threading 
import time
import random

def process1(x):
    while True:
        time.sleep(1)
        print(x)
        x = x + 1


def process2(y):
    while True:
        r = random.Random()
        print (f"Thread-2: {r.random()}")
        time.sleep(1)

if __name__ == "__main__":
    t1 = threading.Thread(target=process1, args=(10,))
    t1.start()

    t2 = threading.Thread(target=process2, args=(10,))
    t2.start()
    
    t1.join()
    t2.join()
    