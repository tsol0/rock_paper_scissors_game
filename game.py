import random

    
            
def game():
    tools = ['rock', 'paper', 'scissors']
    score_to_win = validate_integer()
    winner_found = False
    player_score = 0
    comp_score = 0
    

    while winner_found != True:
        comp_player_tool = random_tool(tools)
        
        player_tool = validate_tool(tools)
        
        print(f"Player selected {player_tool} and Computer selected {comp_player_tool}")
        
        player_score, comp_score = compare_tools(player_tool, comp_player_tool, tools, comp_score, player_score)
        
        print(f"Player score: {player_score} | Computer score: {comp_score}")
        
        
        winner_found = check_for_winner(player_score, comp_score, score_to_win)
    
    print("The game has ended")
    

def check_for_winner(player_score, comp_score, score_to_win):
    if player_score == score_to_win:
        print("Player wins!!")
        return True
    elif comp_score == score_to_win:
        print("Computer wins!!")
        return True
    return False
        

def validate_integer():
    while True:
        user_input = input("Enter the score a player needs to get to win: ")
        if user_input == "":
            return 1
        elif user_input.isdigit():
            return int(user_input)
        else:
            print("Invalid input. Please enter a valid number.")


def validate_tool(tools):
    while True:
        user_input = input("Enter a tool such as rock, paper or scissors: ")
        if user_input in tools:
            return user_input
        else:
            print("Invalid input")
        

def random_tool(tools):
    num = random.randint(0,2)  # 3 possible outcomes so we need numbers 0-2
    tool = tools[num]
    return tool


def compare_tools(player_tool, comp_tool, tools, comp_score, player_score):
        if (player_tool == comp_tool):
            print("draw")
            return player_score, comp_score
        # this is the order of tools in the list ['rock', 'paper', 'scissors']
        elif (player_tool == tools[0]) and (comp_tool == tools[1]):
            comp_score += 1
        elif (player_tool == tools[0]) and (comp_tool == tools[2]):
            player_score += 1
            
        elif (player_tool == tools[1]) and (comp_tool == tools[2]):
            comp_score += 1
        elif (player_tool == tools[1]) and (comp_tool == tools[0]):
            player_score += 1
            
        elif (player_tool == tools[2]) and (comp_tool == tools[0]):
            comp_score += 1
        elif (player_tool == tools[2]) and (comp_tool == tools[1]):
            player_score += 1
        
        return player_score, comp_score
   
    
if __name__ == "__main__":
    game()
    
                
        


        