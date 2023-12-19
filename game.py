import random

def validate_integer():
    number = ""
    valid_number = False
    while valid_number != True:
        number = input("Please enter valid number")
        if number.isnumeric():
            valid_number = True
    return number


def validate_tool(tools):
    while valid_tool not in tools:
        selected_tool = input('Please enter either rock, paper or scissors')
        selected_tool = selected_tool.lower()
        if selected_tool in tools:
            valid_tool = True
        return selected_tool

def random_tool(tools):
    num = random.randint(0,2)  # 3 possible outcomes so we need numbers 0-2
    tool = tools[num]
    return tool

def compare_tools(player_tool, comp_player_tool, tools):
        if (player_tool == comp_player_tool):
            pass
        elif (player_tool == tools[0]) and (comp_player_tool == tools[1]):
            comp_score += 1
        elif (player_tool == tools[1]) and (comp_player_tool == tools[2]):
            comp_score += 1
        elif (player_tool == tools[2]) and (comp_player_tool == tools[0]):
            comp_score += 1
            
        elif (player_tool == tools[0]) and (comp_player_tool == tools[2]):
            player_score += 1
        elif (player_tool == tools[1]) and (comp_player_tool == tools[1]):
            player_score += 1
        elif (player_tool == tools[2]) and (comp_player_tool == tools[0]):
            player_score += 1
        
        return player_score, comp_score
    
            
def game():
    number = validate_integer()
    rounds = number
    winner_found = False
    player_score = 0
    comp_score = 0
    

    while winner_found != False:
        tools = ['rock', 'paper', 'scissors']
        player_tool = validate_tool(tools)
        comp_player_tool = random_tool(tools)
        
        player_score, comp_score = compare_tools(player_tool, comp_player_tool, tools)
        
        if  rounds == 1:
            winner_found = True
            
            if player_score > comp_score:
                print("Player won!")
            else:
                print("Computer won")
        else:
            # if rounds is 3 than one of the player needs to win 2 out 3 to win 
            # if rounds is 5 than a player needs to win 3 out of 5 to win
            pass 

if __name__ == "__main__":
    game()
    
                
        


        