import numpy as np
import re

def main_v1():
    """
    Given a 2-dimensional array, collect the locations of special characters
    in the array and determine if there are any numbers within its proximity. 
        EX: for a special character at [x,y], check all [x+i, y+j] for any numbers  
    Once the numbers are located, take their sum as the solution
    """

    #Read in target file
    array = np.genfromtxt('/home/gpedrani/Public/Advent_of_Code/day_3/input.txt', delimiter=',', dtype=str)

    #identify characters which are not digits or periods
    x_dim, y_dim = array.shape
    mask = np.zeros([x_dim,y_dim])
    for i in range(0, x_dim):
        for j in range(0, y_dim):
            mask[i,j] = (re.search(r'\D',array[i,j]) != None and array[i,j] != ".")

    #identify numbers which are +/- 1 space away from speical characters
    hits = np.zeros([x_dim,y_dim])
    mask_rows = np.where(mask == 1)[0] 
    mask_cols = np.where(mask == 1)[1]
    index = len(mask_rows)
    for iter in range(0,index):

        #calculate all of the indcies that I need
        low_x = mask_rows[iter] - 1
        x     = mask_rows[iter] 
        up_x  = mask_rows[iter] + 1

        low_y = mask_cols[iter] - 1
        y     = mask_cols[iter] 
        up_y  = mask_cols[iter] + 1

        #check all permutations of index pairs for numbers
        for x_item in (low_x, x, up_x):
            for y_item in (low_y, y, up_y):
                hits[x_item, y_item] = (re.search(r'\d',array[x_item,y_item]) != None)
    
    #identify the numbers which contain part numbers 
    total_sum = 0
    hits_rows, hits_cols = np.where(hits == 1)[0], np.where(hits == 1)[1]
    index = len(hits_rows)
    for iter in range(0,index):

        row, col = hits_rows[iter], hits_cols[iter]

        #Compare previous row-col pair with current entry
        ##skip this entry if including it will create duplicate entries for solution
        if iter != 0:
            old_row, old_col = hits_rows[iter-1], hits_cols[iter-1] 
            if row == old_row and old_col == col - 1:
               number = 0
            else:
               number = process_array(row, col, array)
        elif iter == 0:
            number = process_array(row, col, array)
 
        #add current number to running total
        print(number)
        total_sum += number 


    print("The sum of all part numbers is: %s" % total_sum)


#Define Helper programs
def process_array(row: int, col: int, array: np.array) -> int: 
    """
    Parses an array for numbers consecutive numbers with Regex, and concatenates them into a single number. Takes in 
    an row, column, and array as input; returns a single number as output
    """

    #define starting digit, and iterable for sigfig counting 
    number   = int(array[row,col])
    n = 1
    max_row, max_col = array.shape

    # check edge case first (where a seed number can move forwards or backwards, choose left most
    ## digit and continue right as normal
    if (re.search(r'\d', array[row,col-1]) != None) and (re.search(r'\d', array[row,col+1]) != None):
        col = col-1
        number = int(array[row,col])
        while ((0 <= col <=max_col-1) and (re.search(r'\d', array[row,col+1]) != None)):
            number = number*10 + int(array[row,col+1])
            col += 1

    #Case 1: scroll through and add digits moving backwards
    elif ((1<=col<=max_col) and (re.search(r'\d', array[row,col-1]) != None)):
        while (re.search(r'\d', array[row,col-1]) != None):
            number = int(array[row,col-1])*10**n + number 
            col -= 1
            n   += 1
            if col <= 0:
                break

    #Case 2: scroll through and add digits moving forwards
    elif ((0<=col<=max_col-1) and re.search(r'\d', array[row,col+1]) != None):
        while ((re.search(r'\d', array[row,col+1]) != None)):
            number = number*10 + int(array[row,col+1])
            col += 1
            if col > 140:
                break
    
    return number

#run program
main_v1()
