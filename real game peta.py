import time
import random  #Import module para sa random at timer

def intro(): #intro ng game
    print("""
    ~~~~~~~~~~~~~~~~~~~ Boxing Game ~~~~~~~~~~~~~~~~~~~
██████╗   ██████╗  ██╗    ██╗ ██╗ ███╗   ██╗  ██████╗     █████╗   ██╗      ██╗      ███████╗ ██╗   ██╗
██╔══██╗ ██╔═══██╗  ██║  ██╔╝ ██║ ████╗  ██║ ██╔════╝    ██╔══██╗  ██║      ██║      ██╔════╝ ╚██╗ ██╔╝
██████╔╝ ██║   ██║   █████╔╝  ██║ ██╔██╗ ██║ ██║ ███╗    ███████║  ██║      ██║      █████╗    ╚████╔╝ 
██╔══██╗ ██║   ██║  ██╔═ ██╗  ██║ ██║╚██╗██║ ██║   ██║   ██╔══██║  ██║      ██║      ██╔══╝     ╚██╔╝  
██████ ║ ╚██████╔╝ ██║    ██╗ ██║ ██║ ╚████║ ╚██████╔╝   ██║  ██║  ███████╗ █████║   ███████╗    ██║   
╚══════╝  ╚═════╝  ╚═╝    ╚═╝ ╚═╝ ╚═╝  ╚═══╝  ╚═════╝    ╚═╝  ╚═╝  ╚══════╝ ╚════╝   ╚══════╝    ╚═╝   
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                             MAIN MENU
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                           [1] New Game
                           [2] Exit
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """)

def choicemo(): #choice ng player kung mag start ng game o mag exit
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                print("\nStarting a New Game...\n")
                return True  # Start the game
            elif choice == 2:
                print("You have exited the game. Goodbye!")
                return False  # Exit the game
            else:
                print("Invalid choice. Please select 1 or 2.")
        except (ValueError, KeyboardInterrupt):
            print("Invalid choice. Please select 1 or 2.")

def welcome_message():
    print("\nWelcome to the Boxing Game!")
    print("You will face a street boxer in a turn-based boxing match.")
    print("Choose your actions wisely before the timer runs out!\n")


def choose_action():
    print("Your turn! Choose your action:")
    print("1. Jab (Low damage, high chance of hitting)")
    print("2. Hook (Medium damage, moderate chance of hitting)")
    print("3. Uppercut (High damage, low chance of hitting)")
    print("You have 5 seconds to choose...\n")
    
    start_time = time.time()
    while time.time() - start_time < 5:         #dapat 5 seconds pero di gumagana
            try:
                action = input("Enter your choice (1, 2, or 3): ")
                if action in ["1", "2", "3"]:
                    return int(action)
            except (ValueError, KeyboardInterrupt):
                print("Invalid choice. Please select 1, 2, or 3.")
    print("\nTime's up! You missed your turn!")
    return None  # No action chosen


def perform_action(action, player_name):
    try:
        if action == 1:
            damage = random.randint(5, 10)
            chance = 0.9
            move = "Jab"
        elif action == 2:
            damage = random.randint(10, 20)
            chance = 0.7
            move = "Hook"
        elif action == 3:
            damage = random.randint(20, 30)
            chance = 0.5
            move = "Uppercut"
        else:
            return 0  # No damage if no action chosen
        
        if random.random() <= chance:
            print(f"{player_name} lands a {move}! It deals {damage} damage.\n")
            return damage
        else:
            print(f"{player_name} misses the {move}!\n")
            return 0
    except (ValueError, KeyboardInterrupt):
        print("Invalid choice. Please try again.")

def opponent_action():
    action = random.choice([1, 2, 3])
    return perform_action(action, "Opponent")

def display_health(player_health, opponent_health):
    print(f"Your Health: {player_health}")
    print(f"Opponent's Health: {opponent_health}\n")

def boxing_game():
    while True:
        intro()
        if not choicemo():
            break  # Exit the game if the player chooses to

        welcome_message()
        player_health = 100
        opponent_health = 100

        while player_health > 0 and opponent_health > 0:
            display_health(player_health, opponent_health)
            
            # Player's turn
            action = choose_action()
            if action is not None:
                opponent_health -= perform_action(action, "You")
            
            # Opponent's turn
            if opponent_health > 0:  # Only if opponent is still alive
                print("Opponent's turn!")
                player_health -= opponent_action()
            
            time.sleep(1)  # Pause for a moment before the next turn

        # End of game
        if player_health <= 0 and opponent_health <= 0:
            print("It's a draw! Both fighters are down!")
        elif player_health <= 0:
            print("You lose! Better luck next time.")
        else:
            print("Congratulations! You win!")
        print("\nReturning to the main menu...\n")

boxing_game()

### Key Change
