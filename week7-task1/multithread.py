##multi threading-----------------

import threading
def fun():
    for i in range(1, 11):
        print(i)
def fun1():
    for letter in 'abcdefghij':
        print(letter)
thread1 = threading.Thread(target=fun)
thread2 = threading.Thread(target=fun1)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("All threads have finished.")




import threading
def fun():
    for i in range(2,12):
        print(i)
def fun1():
    for letter in ("gayathri"):
        print(letter)
thread1 = threading.Thread(target=fun)
thread2 = threading.Thread(target=fun1)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("All are done.")

import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(1000000):
        with lock:
            counter += 1

def decrement():
    global counter
    for _ in range(1000000):
        with lock:
            counter -= 1

# Create threads
thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=decrement)

# Start the threads
thread1.start()
thread2.start()

# Wait for the threads to finish
thread1.join()
thread2.join()

print("Counter:", counter)


import threading
def fun():
    for i in range(2,8):
        print(i)
def fun1():
    for letter in ("gayathri"):
        print(letter)
thread1 = threading.Thread(target=fun)
thread2 = threading.Thread(target=fun1)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("All are done.")

