import threading
import time

deposit = 50
lock = threading.Lock()

def depositAmount():
    global deposit 
    while True:
        lock.acquire()
        deposit += 1
        print(f"added into deposit : {deposit}")
        time.sleep(2)
        lock.release()

def consumeAmount():
    global deposit 
    while True:
        deposit -= 1
        print(f"consumed from deposit : {deposit}")
        time.sleep(1)

t1 = threading.Thread(target=depositAmount)
t2 = threading.Thread(target=consumeAmount)

t1.start()
t2.start()

