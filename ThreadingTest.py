import threading
import time
import random


def printA():
    for i in range(6):
        print("A... ..." + str(i))
        time.sleep(random.randint(1, 4) * 0.1)


def printB():
    for i in range(6):
        print("B... ..." + str(i))
        time.sleep(random.randint(1, 4) * 0.1)


def printAny(inlist):
    for item in inlist:
        print(str(item))
        time.sleep(random.randint(1, 4) * 0.1)


thread1 = threading.Thread(target=printA)

intup = (789, "Hello", [1, 2, 3])
thread2 = threading.Thread(target=printAny, args=(intup,))

thread1.start()
thread2.start()

printB()

thread1.join()
thread2.join()

print("End here")
