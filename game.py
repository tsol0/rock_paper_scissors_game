import random

def validate_integer():
    number = 1
    valid_number = False
    while valid_number != True:
        number = input("please enter valid number")
        if number.isnumeric():
            valid_number = True
        
    return number


def validate_tool(tools):
    
    while valid_tool not in tools:
        selected_tool = input('please enter either rock, paper or scissors')
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
        # score = [3,]
        player_tool = validate_tool(tools)
        comp_player_tool = random_tool(tools)
        
        player_score, comp_score = compare_tools(player_tool, comp_player_tool, tools)
        
        if  rounds == 1:
            pass
        


        