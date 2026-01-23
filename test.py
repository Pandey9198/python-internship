import threading
import time
class A(thread):

    def run(self):
        for i in range(3):
            print("Thread A running...")
            time.sleep(1)
class B(thread):

    def run(self):
        for i in range(3):
            print("Thread B running...")
            time.sleep(1)
a = A()
b = B()
a.start()
b.start() 
b.join()
a.join()
# import threading
def task():
#     for i in range(3):
#         print("Task running...")
#         time.sleep(1)

# t1 = threading.Thread(target=task)
# t2 = threading.Thread(target=task)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print("Done")
