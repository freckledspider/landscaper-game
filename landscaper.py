# Landscaper

# Start game with
game_state = {"money": 0, "tool": 0}

# Tools in the shop
tools = [
    {"name": "Teeth", "profit": 1, "price": 0},
    {"name": "Scissors", "profit": 5, "price": 5},
    {"name": "Push Lawnmower", "profit": 25, "price": 50},
    {"name": "Electric Lawnmower", "profit": 100, "price": 250},
    {"name": "Landscaping Team", "profit": 250, "price": 500}
]

# User Choices
user_choices = {
    "1": "[1] Mow Lawn",
    "2": "[2] Check Stats",
    "3": "[3] Upgrade Tool",
    "4": "[4] Quit"
}

# Display user choices
def display_user_choices():
    print("\nWhat would you like to do?")
    for key, value in user_choices.items():
        print(value)

# [1] Option to mow the lawn with tool
def mow_lawn(game_state):
    current_tool = tools[game_state["tool"]]
    game_state["money"] += current_tool["profit"]
    print(f"\nYou used {current_tool['name']} to mow the lawn and earned ${current_tool['profit']}")

# [2] Check stats function
def check_stats(game_state):
    current_tool = tools[game_state["tool"]]
    print(f"\nMoney: ${game_state['money']}")
    print(f"Tool: {current_tool['name']}")

# [3] Upgrade tool function
def upgrade_tool(game_state):
    current_tool = tools[game_state["tool"]]
    if game_state["money"] >= current_tool["price"]:
        game_state["money"] -= current_tool["price"]
        game_state["tool"] += 1
        print(f"\nYou upgraded to {tools[game_state['tool']]['name']}")
    else:
        print("\nYou don't have enough money to upgrade your tool.")
    
# [4] Quit game function
def quit_game():
    print("\nYou quit the game.")
    exit()

# Game choices and functions
def game():
    while True:
        display_user_choices()
        user_choice = input("\nEnter your choice: ")
        if user_choice == "1":
            mow_lawn(game_state)
        elif user_choice == "2":
            check_stats(game_state)
        elif user_choice == "3":
            upgrade_tool(game_state)
        elif user_choice == "4":
            quit_game()
        else:
            print("\nPlease select from menu.")

# Run game
game()