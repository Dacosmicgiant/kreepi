# main.py
from blackwood_mansion_game.core import utils, game_state # Import utils and game_state
from blackwood_mansion_game.data import lore_data # Import lore data
from blackwood_mansion_game.locations import mansion_entrance # Import starting location

def creepy_intro():
    print("The rusted gates of Blackwood Mansion swing shut with a mournful clang, sealing you within the estate's suffocating embrace.  A chilling wind whispers through the ancient oaks, carrying the scent of damp earth and decay.")
    print("The mansion looms before you, a gothic monolith against the bruised purple of the twilight sky. Its darkened windows stare like vacant eyes, promising no solace, only secrets.")
    print(f"Local legends whisper of {lore_data.BLACKWOOD_TRAGEDY} that befell the Blackwood family within these walls. Some say the mansion was originally {lore_data.MANSION_PURPOSE}, a place now tainted by darkness.") # Access lore data
    print(f"You came seeking answers, lured by these tales and whispers of {lore_data.HORROR_SOURCE}. Now, trapped within its crumbling walls, the thrill of investigation has curdled into icy dread.") # Access lore data
    print("A palpable sense of unease settles upon you. The very stones of Blackwood Mansion seem to breathe with a dark sentience. Escape is paramount, but the mansion itself seems unwilling to release you.")
    print("Your heart pounds a frantic rhythm against your ribs. Will you unravel the mysteries of Blackwood Mansion and escape its grasp? Or will you become another forgotten soul lost within its shadowed halls?")
    print()

def trapped_ending_mansion_bound(): # Example ending function, place in main.py or a separate endings.py if you have many
    print("\nThe mansion's grasp tightens around you. You are lost forever within its walls...")
    print("Mansion Bound Ending")
    exit() # Or return to main menu, etc.

if __name__ == "__main__":
    creepy_intro()
    mansion_entrance.mansion_entrance() # Start the game at the mansion entrance