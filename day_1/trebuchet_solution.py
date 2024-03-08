import re #for regular expressions 

#main code block 
def main(debug=0):
    """
    Solution steps:
        Import the text file
        Read file line by line
        Pick out the numbers from line, store in an list 
        Pick out the [0] and [-1] items of the list 
        Concatonate to get the value for the line
        Add to a running total
        Continue until last line
        Print out result
    """

    #Open file, and read in lines
    file = open('/home/gpedrani/Public/Advent_of_Code/day_1/input.txt', 'r')
    lines = file.readlines()
    file.close()

    #initialize running sum
    running_sum = 0

    for index, line in enumerate(lines):
        digits = re.findall("[0-9]",line)
        num = digits[0] + digits[-1]
        running_sum += int(num)
        if debug == 1:
            print("Running Sum: %s" % running_sum)
            print("Current Number: %s" % num)
        
    return print("Final Total: %s" % running_sum)

def main_v2(debug=0):

    #Open file, and read in lines
    file = open('/home/gpedrani/Public/Advent_of_Code/day_1/input.txt', 'r')
    lines = file.readlines()
    file.close()

    #initialize running sum
    running_sum = 0

    #Dictionary of matching text to numbers
    num_dictionary = {"one": "o1one", "two": "t2two", "three": "t3three",
                      "four": "f4four", "five": "f5five", "six": "s6six", "seven": "s7seven",
                      "eight": "e8eight", "nine": "n9nine"}

    for index, line in enumerate(lines):
        #replace all keys with their digits coutnerparts
        for key in num_dictionary: 
            if key == "one":
                new_line = re.sub(key, num_dictionary[key], line)
            else:
                new_line = re.sub(key, num_dictionary[key], new_line)

        #Process new string as in the first solution
        digits = re.findall("[0-9]", new_line)
        num = digits[0] + digits[-1]
        running_sum += int(num)
        if debug == 1:
            print("old line: %s" % line)
            print("new line: %s" % new_line)
            print("Running Sum: %s" % running_sum)
            print("Current Number: %s" % num)
        
    return print("Final Total: %s" % running_sum)



#Call function
main_v2(debug=1)




