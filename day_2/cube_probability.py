import re

def main():
    """
    Goal: Given an input with
        1) The number of games
        2) The number of red, blue, and green cubes (r,b,g)
        3) And some target population of cubes  (r_hat, b_hat, g_hat)
    Determine if a given game is possible, and add the game_id together to get solution 
    """

    #Read in target file
    file = open('/home/gpedrani/Public/Advent_of_Code/day_2/input.txt', 'r')
    lines = file.readlines()
    file.close()

    #Construct Target Dictionary
    Target = {"red" : 12, "green": 13,"blue": 14}

    #Parse through Games, rounds, and individual numbers 
    sum_of_games = 0

    for i, line in enumerate(lines):
        #because index starts at 0, and we need the sum of games for our solution, off set by +1
        game_id = i + 1  

        all_rounds = line.split(";") 
        impossible = False 

        for j, Round in enumerate(all_rounds):
            if j == 0:
                #Take the second element of the first (index j==0) round because it contains "Game #:"
                Round = Round.split(":")[1]

            entries = Round.split(",")

            for h, item in enumerate(entries):
                item = item.strip()  
                value, color = item.split(" ")
                value = int(value)
                if Target[color] < value:
                    impossible = True 
                    break
                
        #end of j-loop
        
        if impossible == False:
            print("Adding game_id: %s\n" % game_id)
            sum_of_games += game_id
        elif impossible == True:
            print("Game %s is not possible\n" % game_id)
        
    #end of i-loop

    return print("Sum of games: %s" % sum_of_games) 

def main_v2():
    """
    Goal: Given an input with
        1) The number of games
        2) The number of red, blue, and green cubes (r,b,g)
    Determine the minimum number of cubes needed for the given game to be possilbe.

    Then, calculate the "power" of the game (defined as: r * g * b), and add these powers to 
    generate the solution
    """

    #Read in target file
    file = open('/home/gpedrani/Public/Advent_of_Code/day_2/input.txt', 'r')
    lines = file.readlines()
    file.close()

    #Parse through Games, rounds, and individual numbers 
    sum_of_games = 0

    for i, line in enumerate(lines):
        #because index starts at 0, and we need the sum of games for our solution, off set by +1
        game_id = i + 1  

        all_rounds = line.split(";") 

        red_values   = []
        blue_values  = []
        green_values = []

        for j, Round in enumerate(all_rounds):
            if j == 0:
                #Take the second element of the first (index j==0) round because it contains "Game #:"
                Round = Round.split(":")[1]

            entries = Round.split(",")

            for h, item in enumerate(entries):
                item = item.strip()  
                value, color = item.split(" ")
                value = int(value)
                match color: 
                    case "red":
                        red_values.append(value)
                    case "blue":
                        blue_values.append(value)
                    case "green":
                        green_values.append(value)
                    case _:
                        pass
                
        #end of j-loop
        
        print("The values of all red entries are: %s" % red_values)
        print("The values of all green entries are: %s" % green_values)
        print("The values of all blue entries are: %s" % blue_values)

        min_red   = max(red_values)
        min_green = max(green_values) 
        min_blue  = max(blue_values)

        power = min_red * min_green * min_blue

        print("min values (r,g,b): %s, %s, %s >> Power: %s\n" % (min_red, min_green, min_blue, power))

        sum_of_games += power

    #end of i-loop

    return print("Sum of games: %s\n" % sum_of_games) 



#call fuction
main_v2()

