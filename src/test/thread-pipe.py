import threading
import queue
import time


number_queue = queue.Queue()


def thread_one(n):
    for i in range(1, n+1):
        number_queue.put(i)
        time.sleep(1)


def thread_two():
    while True:
        num = number_queue.get()
        if num is None:
            break

        result = "Even" if num % 2 else "Odd"
        print(f"Number {num} is {result}")
        number_queue.task_done()


if __name__ == "__main__":
    N = 10;

    t1 = threading.Thread(target=thread_one, args=(N,))
    t2 = threading.Thread(target=thread_two, daemon=True)

    t1.start()
    t2.start()

    t1.join()

    number_queue(None)
    t2.join()

    print("Threads execution completed.")
