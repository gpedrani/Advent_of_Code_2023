import re

def lottery():
    """
    Reads in a string of numbers and characters that has three parts:
        - the game and game number
        - the list of numbers to check
        - the list of winning numbers
        ex: card 1: 1 2 3 4 5 | 6 7 8 9 10

    For each game, we check how many of our numbers are found in the list of winning numbers and calculate a score:
        score = 2^(n-1) ; where n is the number of matches
    """

    file = open('/home/gpedrani/Public/Advent_of_Code/day_4/input.txt', 'r')
    lines = file.readlines()
    file.close()

    game_totals = []
    for line in lines:
        #game = re.search("Card \d+:",line)
        mg_numbers = re.search("(?<=:).*?(?=\|)",line)
        mg_winners = re.search("(?<=\|).*?(?=\n)",line)

        #convert match groups into itterables
        my_numbers = re.findall(r"\d+", mg_numbers.group())
        winning_numbers = re.findall(r"\d+", mg_winners.group())
        
        my_numbers = list(map(int, my_numbers))
        winning_numbers = list(map(int,winning_numbers))

        #calcuate game's score
        n = 0
        for number in my_numbers:
            if number in winning_numbers:
                n += 1 

        if n == 0:
            score = 0 
        else:
            score = 2**(n-1)
        game_totals.append(score)


    total = sum(game_totals)

    print(f"The total points scored is: {total}")

    return 

#--------------------------------------------------------------------------------------------------------------------    

def lottery_v2():
    """
    Reads in a string of numbers and characters that has three parts:
        - the game and game number
        - the list of numbers to check
        - the list of winning numbers
        ex: card 1: 1 2 3 4 5 | 6 7 8 9 10

    For each card, we take the total numbers matched from part one and collect the next n number of games
        ie: if card 1 has 4 matches, we would collect copies of cards 2,3,4 and 5  

    We want to return the total number of cards we've collected after processing every card, and their results!
    """

    file = open('/home/gpedrani/Public/Advent_of_Code/day_4/input.txt', 'r')
    lines = file.readlines()
    file.close()

    #find the last possible card/game and initialize a dictionary formated {card#: # of cards obtained}
    lg_game = re.search("Card\s+\d+:",lines[-1])
    max_dict_size = re.findall(r"\d+", lg_game.group())
    game_dict = {}
    for i in range(1,int(max_dict_size[0])+1,1):
        game_dict[i] = 1
    
    #calculate the card level matches
    for line in lines:
        mg_game = re.search("Card\s+\d+:",line)
        mg_numbers = re.search("(?<=:).*?(?=\|)",line)
        mg_winners = re.search("(?<=\|).*?(?=\n)",line)

        #convert match groups into itterables
        init_card  = re.findall(r"\d+", mg_game.group())
        int_card = int(init_card[0])
        my_numbers = re.findall(r"\d+", mg_numbers.group())
        winning_numbers = re.findall(r"\d+", mg_winners.group())
        
        my_numbers = list(map(int, my_numbers))
        winning_numbers = list(map(int,winning_numbers))
    
        #calcuate card's matches 
        n = 0
        for number in my_numbers:
            if number in winning_numbers:
                n += 1 

        #adjust the number of cards in our dictionary 
        if n != 0:
            for j in range(0,game_dict[int_card]):
                for i in range(int_card+1, int_card+n,1):
                    game_dict[i] += 1


    #calculate the total number of scratch cards collected
    total = sum(game_dict.values())

    print(total)
    
    return 
#-------------------------------------------------------------------------------------------------------------------------

#Function call
lottery_v2()




