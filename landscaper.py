# Landscaper

# Start game with
game_state = {"money": 0, "tool": 0}

# Tools in the shop
tools = [
    {"name": "Teeth", "profit": 1, "price": 0}
    {"name": "Scissors", "profit": 5, "price": 5}
    {"name": "Push Lawnmower", "profit": 25, "price": 50}
    {"name": "Electric Lawnmower", "profit": 100, "price": 250}
    {"name": "Landscaping Team", "profit": 250, "price": 500}
]

# Mow lawn with teeth for $1 Each
while(True):
    user_choice = input("[1] Mow Lawn with Teeth [2] Check Money [Q] Quit")
    
    if(user_choice == "1"):
        money + 1
    
    if(user_choice == "2"):
        print(money)
        
    if(user_choice == "Q"):
        break
    
# Buy Scissors
    
    if(money > 5):
        user_choice = input("[1] Mow Lawn with Teeth [2] Check Money [3] Buy Scissor for $5 [Q] Quit")
    
    if(user_choice == "1"):
        money += 1
        
    if(user_choice == "3"):
        print(buy_scissors(money, 5))
        
    if(user_choice == "Q"):
        break