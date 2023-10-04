#student name:   Sophie Lin
#student number: 70196886

import threading

def mySort(myList) -> list:
    # using bubble sort algorithm
    length = len(myList)

    for i in range(length):
        # flag to break if nothing is left to sort
        sorted = True

        for j in range(length - i - 1):
            # swap adjacent values if they are out of order
            if myList[j] > myList[j + 1]:
                myList[j], myList[j + 1] = myList[j + 1], myList[j]
                sorted = False

        if sorted:
            break

    return myList 

def sortingWorker(firstHalf: bool) -> None:
    """
       If param firstHalf is True, the method
       takes the first half of the shared list testcase,
       and stores the sorted version of it in the shared 
       variable sortedFirstHalf.
       Otherwise, it takes the second half of the shared list
       testcase, and stores the sorted version of it in 
       the shared variable sortedSecondHalf.
       The sorting is ascending and you can choose any
       sorting algorithm of your choice and code it.
    """
    if (firstHalf):
        # make variable avaible outside this function's scope
        global sortedFirstHalf

        # sort first half: index 0 to (length of testcase /2) -1
        sortedFirstHalf = mySort(testcase[0:int(len(testcase)/2)-1])
    else:
        # make variable avaible outside this function's scope
        global sortedSecondHalf

        # sort second half: index (length of testcase /2) to (length of testcase)
        sortedSecondHalf = mySort(testcase[int(len(testcase)/2):len(testcase)-1])

def mergingWorker() -> None:
    """ This function uses the two shared variables 
        sortedFirstHalf and sortedSecondHalf, and merges/sorts
        them into a single sorted list that is stored in
        the shared variable SortedFullList.
    """
    lengthFirstHalf = len(sortedFirstHalf)
    lengthSecondHalf = len(sortedSecondHalf)

    # stores the current index of sortedFirstHalf and sortedSecondHalf
    f = 0
    s = 0

    # make variable avaible outside this function's scope
    global SortedFullList

    for i in range(len(testcase)):
        if (f >= lengthFirstHalf) or (s >= lengthSecondHalf):
            break

        print(f"i: {i}, f: {f}, s: {s}")
        # sortedFirstHalf and sortedSecondHalf not merged yet
        if (f < lengthFirstHalf) and (s < lengthSecondHalf):
            if (sortedFirstHalf[f] >= sortedSecondHalf[s]):
                # merge from first half
                SortedFullList[i] = sortedFirstHalf[f]
                f = f+1
            else:
                # merge from second half
                SortedFullList[i] = sortedSecondHalf[s]
                s = s+1
        # sortedFirstHalf merged
        elif (f >= lengthFirstHalf):
            SortedFullList[i] = sortedSecondHalf[s]
            s = s+1
        # sortedSecondHalf merged
        else:
            SortedFullList[i] = sortedFirstHalf[f]
            f = f+1



if __name__ == "__main__":
    #shared variables
    testcase = [8,5,7,7,4,1,3,2]
    sortedFirstHalf: list = []
    sortedSecondHalf: list = []
    SortedFullList: list = []
    
    #to implement the rest of the code below, as specified 
    t1 = threading.Thread(target=sortingWorker, args=(True,))
    t1.start()
    t2 = threading.Thread(target=sortingWorker, args=(False,))
    t2.start()
    t3 = threading.Thread(target=mergingWorker)
    t3.start()

    # join the threads
    t1.join()
    t2.join()
    t3.join()
    


    #as a simple test, printing the final sorted list
    print("The final sorted list is ", SortedFullList)
