from multiprocessing import Process

# Task 1
def task1():
    for i in range(5):
        print("Task 1 running", i)

# Task 2
def task2():
    for i in range(5):
        print("Task 2 running", i)

if __name__ == "__main__":
    # Create processes
    p1 = Process(target=task1)
    p2 = Process(target=task2)

    # Start processes
    p1.start()
    p2.start()

    # Wait for them to finish
    p1.join()
    p2.join()

    print("Both tasks finished!")
