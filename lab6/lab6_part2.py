#student name:   Sophie Lin
#student number: 70196886

# part 2 - allow philosopher to pick up chopsticks if both chopsticks are available

import multiprocessing
import random #is used to cause some randomness 
import time   #is used to cause some delay to simulate thinking or eating times

def philosopher(id: int, chopstick: list, bothChopstick: list): 
    """
       implements a thinking-eating philosopher
       id is used to identifier philosopher #id (id is between 0 to numberOfPhilosophers-1)
       chopstick is the list of semaphores associated with the chopsticks 
    """
    def eatForAWhile():   #simulates philosopher eating time with a random delay
        print(f"DEBUG: philosopher{id} eating")
        time.sleep(round(random.uniform(.1, .3), 2)) #a random delay (100 to 300 ms)
    
    def thinkForAWhile(): #simulates philosopher thinking time with a random delay
        print(f"DEBUG: philosopher{id} thinking")
        time.sleep(round(random.uniform(.1, .3), 2)) #a random delay (100 to 300 ms)
    
    # part 2 - map id to bothChopstick semaphore
    if (id == 0 or id == 1):
        bothChopstick[0].acquire()
    if (id == 1 or id == 2):
        bothChopstick[1].acquire()
    if (id == 2 or id == 3):
        bothChopstick[2].acquire()
    if (id == 3 or id == 4):
        bothChopstick[3].acquire()
    if (id == 4 or id == 0):
        bothChopstick[4].acquire()

    for _ in range(6): #to make testing easier, instead of a forever loop we use a finite loop
        leftChopstick = id
        rightChopstick = (id + 1) % 5      #5 is number of philosophers

        #to simplify, try statement not used here
        chopstick[leftChopstick].acquire()
        print(f"DEBUG: philosopher{id} has chopstick{leftChopstick}")
        chopstick[rightChopstick].acquire()
        print(f"DEBUG: philosopher{id} has chopstick{rightChopstick}")

        eatForAWhile()  #use this line as is

        print(f"DEBUG: philosopher{id} is to release chopstick{rightChopstick}")
        chopstick[rightChopstick].release()
        print(f"DEBUG: philosopher{id} is to release chopstick{leftChopstick}")
        chopstick[leftChopstick].release()

        thinkForAWhile()  #use this line as is

    # part 2 - map id to bothChopstick semaphore
    if (id == 0 or id == 1):
        bothChopstick[0].release()
    if (id == 1 or id == 2):
        bothChopstick[1].release()
    if (id == 2 or id == 3):
        bothChopstick[2].release()
    if (id == 3 or id == 4):
        bothChopstick[3].release()
    if (id == 4 or id == 0):
        bothChopstick[4].release()

if __name__ == "__main__":
    semaphoreList = list()          #this list will hold one semaphore per chopstick
    numberOfPhilosophers = 5

    for i in range(numberOfPhilosophers):             
        semaphoreList.append(multiprocessing.Semaphore(1))    #one semaphore per chopstick

    # part 2 - semaphore for each philosopher indicating if both chopsticks are available
    bothChopstickSemaphoreList = list()
    for i in range(numberOfPhilosophers):             
        bothChopstickSemaphoreList.append(multiprocessing.Semaphore(1))    #one semaphore per chopstick

    philosopherProcessList = list()
    for i in range(numberOfPhilosophers): #instantiate all processes representing philosophers
        philosopherProcessList.append(multiprocessing.Process(target=philosopher, args=(i, semaphoreList, bothChopstickSemaphoreList)))
    for j in range(numberOfPhilosophers): #start all child processes
        philosopherProcessList[j].start()
    for k in range(numberOfPhilosophers): #join all child processes
        philosopherProcessList[k].join()
