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
    array = np.genfromtxt('/home/gpedrani/Public/Advent_of_Code/day_3/test.txt', delimiter=',', dtype=str)

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
        n = 1 
        row, col = hits_rows[iter], hits_cols[iter]
        number   = int(array[row,col])
       
        #scroll through and add digits moving backwards
        if (re.search(r'\d', array[row,col-1]) != None):
            while (re.search(r'\d', array[row,col-1]) != None):
                number = int(array[row,col-1])*10**n + number 
                col -= 1
                n   += 1
        #scroll through and add digits moving forwards
        elif (re.search(r'\d', array[row,col+1]) != None):
            while (re.search(r'\d', array[row,col+1]) != None):
                number = number*10 + int(array[row,col+1])
                col += 1
        
        print(row, col, number)
 
        #add current number to running total
        total_sum += number 


    print("The sum of all part numbers is: %s" % total_sum)



main_v1()
