import threading
import time

def batting():
    for ball in range(1, 6):
        print(f"Batsman hits ball {ball}")
        time.sleep(1)  

def bowling():
    for ball in range(1, 6):
        print(f"Bowler bowls ball {ball}")
        time.sleep(1)  

# creating threads
t1 = threading.Thread(target=batting)
t2 = threading.Thread(target=bowling)

#starting the threads
t1.start()
t2.start()

# wait for both threads to finish
t1.join()
t2.join()

print("Over finished")
