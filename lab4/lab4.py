#student name:   Sophie Lin
#student number: 70196886

import threading


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
    # Inner function to sort a list
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

    if (firstHalf):
        # make variable avaible outside this function's scope
        global sortedFirstHalf

        # sort first half: index 0 to (length of testcase /2) -1
        sortedFirstHalf = mySort(testcase[0:int(len(testcase)/2)])
    else:
        # make variable avaible outside this function's scope
        global sortedSecondHalf

        # sort second half: index (length of testcase /2) to (length of testcase)
        sortedSecondHalf = mySort(testcase[int(len(testcase)/2):len(testcase)])

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

    # while first half and second half have not been merged
    while (f < lengthFirstHalf) or (s < lengthSecondHalf):

        # sortedFirstHalf and sortedSecondHalf not merged yet
        if (f < lengthFirstHalf) and (s < lengthSecondHalf):
            if (sortedFirstHalf[f] <= sortedSecondHalf[s]):
                # merge from first half
                SortedFullList.append(sortedFirstHalf[f])
                f = f+1
            else:
                # merge from second half
                SortedFullList.append(sortedSecondHalf[s])
                s = s+1
        # sortedFirstHalf merged
        elif (f >= lengthFirstHalf):
            SortedFullList.append(sortedSecondHalf[s])
            s = s+1
        # sortedSecondHalf merged
        elif (s >= lengthSecondHalf):
            SortedFullList.append(sortedFirstHalf[f])
            f = f+1



if __name__ == "__main__":
    #shared variables
    #testcase = [3,2,1]
    #testcase = [7,6,1]
    #testcase = []
    #testcase = [2]
    #testcase = [3,8,5,7,7,4,1,3,2]
    #testcase = [8,5,7,7,4,1,3,2]
    testcase =  [12, -1, 7, 7, 3, 50, 6, 8]
    print("test case is: ", testcase)
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
    
    print("first half is: ", sortedFirstHalf)
    print("second half is: ", sortedSecondHalf)

    #as a simple test, printing the final sorted list
    print("The final sorted list is ", SortedFullList)
