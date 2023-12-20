import random

    
            
def game():
    tools = ['rock', 'paper', 'scissors']
    rounds = validate_integer()
    winner_not_found = True
    player_score = 0
    comp_score = 0
    
    print(f"{rounds}")
    

    while winner_not_found:
        comp_player_tool = random_tool(tools)
        player_tool = validate_tool(tools)
        
        print(f"Player selected {player_tool} and Computer selected {comp_player_tool}")
        
        player_score, comp_score = compare_tools(player_tool, comp_player_tool, tools, comp_score, player_score)
        
        print(f"Player score is {player_score}")
        print(f"Computer score is {comp_score}")
        
        if  rounds == 1:
            print(f"{rounds}")
            winner_not_found = False
            
            if player_score > comp_score:
                print("Player won!")
            else:
                print("Computer won!")
        else:
            continue
            # if rounds is 3 than one of the player needs to win 2 out 3 to win 
            # if rounds is 5 than a player needs to win 3 out of 5 to win
            # pass 

def validate_integer():
    while True:
        user_input = input("Enter a numeric value: ")
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Invalid input. Please enter a numeric value.")


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

def compare_tools(player_tool, comp_player_tool, tools, comp_score, player_score):
        if (player_tool == comp_player_tool):
            print("draw")
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
    
if __name__ == "__main__":
    game()
    
                
        


        