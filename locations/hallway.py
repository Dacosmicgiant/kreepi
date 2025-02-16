# locations/hallway.py
from blackwood_mansion_game.core import game_state, utils # Import game_state and utils
from blackwood_mansion_game.data import lore_data # Import lore data

def hallway():
    print("\nYou stand in the grand hallway. A massive grandfather clock dominates the space, its pendulum still.")
    print("Portraits line the walls, their eyes seeming to follow you. You notice one portrait in particular - a stern-faced man with piercing eyes, a plaque below reads 'Lord Alistair Blackwood'.")
    print("A grand staircase leads upward.")
    utils.random_event("hallway") # Use random_event from utils
    choices = [
        "Inspect the grandfather clock",
        "Examine the portraits",
        "Ascend the staircase",
        "Return to mansion entrance"
    ]
    if "silver_locket" in game_state.player_inventory and not game_state.clock_puzzle_solved: # Access game_state variables
        choices.insert(1, "Use silver locket on grandfather clock")

    choice = utils.make_choice("Choose your path:", choices) # Use make_choice from utils

    if choice == 0:
        if game_state.clock_puzzle_solved: # Access game_state variable
            from blackwood_mansion_game.locations import basement_stairs # Import location module locally to avoid circular import
            basement_stairs.basement_stairs()
        else:
            print("\nAs you approach the clock, its hands suddenly spin wildly! The clock face is covered in strange symbols, not numbers.")
            print("Perhaps there's a clue somewhere in the mansion to decipher these symbols...")
            hallway()
    elif choice == 1:
        from blackwood_mansion_game.locations import study # Import location module locally to avoid circular import
        study.study()
    elif choice == 2:
        from blackwood_mansion_game.locations import landing # Import location module locally to avoid circular import
        landing.landing()
    elif choice == 3:
        from blackwood_mansion_game.locations import mansion_entrance # Import location module locally to avoid circular import
        mansion_entrance.mansion_entrance()
    elif "silver_locket" in game_state.player_inventory and not game_state.clock_puzzle_solved and choice == 4: # Access game_state variables
        print("\nYou hold the silver locket to the grandfather clock. As it touches the clock face, the locket warms in your hand.")
        print("The clock symbols glow faintly, and you hear a soft click.")
        print("The clock face now displays numbers, and a small compartment opens below the clock face, revealing a rusty key.")
        game_state.player_inventory.append("rusty_key") # Access and modify game_state variable
        print("Added rusty key to inventory")
        game_state.clock_puzzle_solved = True # Access and modify game_state variable
        hallway()