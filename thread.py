import threading
import time


def slp(name, n):
    print(f'I am {name} will sleep for {n}')
    # for i in range(n):
    #     time.sleep(1)
    #     print(n-i)
    time.sleep(n)
    print(f'slept for {n}')

t1 = threading.Thread(target=slp, args=('number one',5))
t2 = threading.Thread(target=slp, args=('number one',4))
t3 = threading.Thread(target=slp, args=('number one',6))
t4 = threading.Thread(target=slp, args=('number one',2))

t1.start()
t2.start()
t3.start()
t4.start()
