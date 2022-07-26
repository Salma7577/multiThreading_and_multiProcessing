
#required libraries
#all are bulit-in libraries
import time
from threading import Thread
from multiprocessing import Process


COUNT = 200000000


def task0(n):
    while n > 0:
        n -= 1


if __name__ == '__main__':
    start = time.time()

    # task0(COUNT)
    # task0(COUNT)

    # t1 = Thread(target=task0, args=[COUNT])
    # t2 = Thread(target=task0, args=[COUNT])
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()

    p1 = Process(target=task0, args=[COUNT])
    p2 = Process(target=task0, args=[COUNT])
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    end = time.time()
    print('Time taken in seconds -', end - start)
