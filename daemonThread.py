# Deamon Thread = a thread that runs in the background, not important for program to run
# your program will not wait for daemon threads to complete before exiting
# None daemon threads cannot normally be killed, stay alive until task is complete
# examples : background tasks, garbage collection, waiting for input, long running process


import threading
import time

def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for: ", count, "seconds")
x = threading.Thread(target=timer, daemon=True)  #Setting deamon true kills all programs when they are finished running
x.start()

#x.setDaemon(True) #You can set Daemon true/false
print(x.isDaemon()) 

answer = input("Do you wish to exit?")

