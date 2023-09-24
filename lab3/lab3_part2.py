#student name:   Sophie Lin
#student number: 70196886

import multiprocessing

def bitwiseANDlist(myList: list):
    """
        custom function to bitwise AND all elements in myList
        every item in myList must be 0 or 1
    """
    result = 1
    for item in myList:
        result &= item
    return result

def checkColumn(puzzle: list, column: int):
    """ 
        param puzzle: a list of lists containing the puzzle 
        param column: the column to check (a value between 0 to 8)

        This function checks the indicated column of the puzzle, and 
        prints whether it is valid or not. 
        
        As usual, this function must not mutate puzzle 
    """
    # list of 0s
    check = [0] * len(puzzle) 
    for i in range(len(puzzle)):
        #print(puzzle[i][column])
        check[puzzle[i][column] - 1] = 1
    #print(check)
    #print(f"{bitwiseANDlist(check)}")
    if (bitwiseANDlist(check) == 1):
        validStr = ""
    else:
        validStr = " not"
    print(f"Column {column}{validStr} valid")


def checkRow(puzzle: list, row: int):
    """ 
        param puzzle: a list of lists containing the puzzle 
        param row: the row to check (a value between 0 to 8)

        This function checks the indicated row of the puzzle, and 
        prints whether it is valid or not. 
        
        As usual, this function must not mutate puzzle 
    """
    check = [0] * len(puzzle) 
    for i in range(len(puzzle[row])):
        check[puzzle[row][i] - 1] = 1
    #print(check)
    if (bitwiseANDlist(check) == 1):
        validStr = ""
    else:
        validStr = " not"
    print(f"Row {row}{validStr} valid")


def checkSubgrid(puzzle: list, subgrid: int):
    """ 
        param puzzle: a list of lists containing the puzzle 
        param subgrid: the subgrid to check (a value between 0 to 8)
        Subgrid numbering order:    0 1 2
                                    3 4 5
                                    6 7 8
        where each subgrid itself is a 3x3 portion of the original list
        
        This function checks the indicated subgrid of the puzzle, and 
        prints whether it is valid or not. 
        
        As usual, this function must not mutate puzzle 
    """
    subgridRows = [ [0, 1, 2],
                    [0, 1, 2],
                    [0, 1, 2],
                    [3, 4, 5],
                    [3, 4, 5],
                    [3, 4, 5],
                    [6, 7, 8],
                    [6, 7, 8],
                    [6, 7, 8]
                  ]
    subgridCols = [ [0, 1, 2],
                    [3, 4, 5],
                    [6, 7, 8],
                    [0, 1, 2],
                    [3, 4, 5],
                    [6, 7, 8],
                    [0, 1, 2],
                    [3, 4, 5],
                    [6, 7, 8]
                  ]
    check = [0] * len(puzzle)
    for row in subgridRows[subgrid]:
        for col in subgridCols[subgrid]:
            check[puzzle[row][col] - 1] = 1
    if (bitwiseANDlist(check) == 1):
        validStr = ""
    else:
        validStr = " not"
    print(f"Subgrid {subgrid}{validStr} valid")

if __name__ == "__main__":
    # all valid
    test1 = [ [6, 2, 4, 5, 3, 9, 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5],
              [1, 4, 3, 8, 6, 5, 7, 2, 9],
              [9, 5, 8, 2, 4, 7, 3, 6, 1],
              [7, 6, 2, 3, 9, 1, 4, 5, 8],
              [3, 7, 1, 9, 5, 6, 8, 4, 2],
              [4, 9, 6, 1, 8, 2, 5, 7, 3],
              [2, 8, 5, 4, 7, 3, 9, 1, 6]
            ]

    # all cols not valid
    test2 = [ [6, 2, 4, 5, 3, 9, 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5],
              [6, 2, 4, 5, 3, 9, 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5],
              [6, 2, 4, 5, 3, 9, 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5]
            ]

    # all cols not valid
    # subgrids 2, 4, 6 not valid
    test3 = [ [6, 2, 4, 5, 3, 9, 1, 9, 7], # row not valid
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5],
              [6, 2, 4, 5, 3, 9, 1, 8, 7],
              [5, 1, 9, 5, 2, 8, 6, 3, 4], # row not valid
              [8, 3, 7, 6, 1, 4, 2, 9, 5],
              [6, 2, 4, 5, 3, 9, 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4], 
              [1, 3, 7, 6, 1, 4, 2, 9, 5]  # row not valid
            ]

    # cols 1, 7 not valid
    # rows 2, 8 not valid
    # subgrids 2, 3, 5 ,8 not valid
    test4 = [ [6, 2, 4, 5, 3, 9, 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 9, 9, 5],
              [1, 2, 3, 8, 6, 5, 7, 4, 9],
              [9, 5, 8, 2, 4, 7, 3, 6, 1],
              [7, 6, 2, 3, 9, 1, 4, 5, 8],
              [3, 7, 1, 9, 5, 6, 8, 4, 2],
              [4, 9, 6, 1, 8, 2, 5, 7, 3],
              [2, 8, 5, 4, 7, 3, 2, 1, 6]
            ]

    
    testcase = test2   #modify here for other testcases
    SIZE = 9

    # list containing all the proesses
    processes = []

    # create and start all the processes
    for col in range(SIZE):  #checking all columns
        p = multiprocessing.Process(target=checkColumn, args=(testcase, col))
        p.start()
        processes.append(p)
    for row in range(SIZE):  #checking all rows
        p = multiprocessing.Process(target=checkRow, args=(testcase, row))
        p.start()
        processes.append(p)
    for subgrid in range(SIZE):   #checking all subgrids
        p = multiprocessing.Process(target=checkSubgrid, args=(testcase, subgrid))
        p.start()
        processes.append(p)

    # call join() on all the processes
    for process in processes:
        process.join()
