import random

def creepy_intro():
    print("You awaken in a dimly lit hallway. Dust and cobwebs coat every surface.")
    print("A chilling draft whispers through broken windows. You are trapped in Blackwood Mansion.")
    print("Your heart pounds. Escape seems impossible, but you must try. Or uncover the secrets within...")
    print()

def make_choice(prompt, choices):
    print(prompt)
    for i, choice in enumerate(choices):
        print(f"{i+1}. {choice}")
    while True:
        try:
            choice_index = int(input("Enter your choice: ")) - 1
            if 0 <= choice_index < len(choices):
                return choice_index
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def random_event():
    events = [
        "A sudden gust of wind slams a door shut nearby.",
        "You hear a faint whisper, but no one is there.",
        "The shadows seem to deepen and writhe.",
        "A floorboard creaks ominously under your feet.",
        "The temperature drops suddenly, sending shivers down your spine."
    ]
    if random.random() < 0.3: # 30% chance of event
        print(random.choice(events))
        print()

def hallway():
    print("You are in the main hallway. Two paths lie ahead.")
    random_event()
    choice = make_choice("Which way do you go?", ["Explore the creaking staircase.", "Venture into the shadowy basement door."])
    if choice == 0:
        attic()
    else:
        basement()

def basement():
    print("You descend into the cold, damp basement. The air is thick with mildew.")
    random_event()
    choice = make_choice("Do you:", ["Investigate the source of a dripping sound.", "Search for another way out."])
    if choice == 0:
        death_ending() # Risky choice
    else:
        escape_ending() # Smart choice

def attic():
    print("You climb the rickety staircase to the dusty attic. Moonlight filters through cracks in the roof.")
    random_event()
    choice = make_choice("Do you:", ["Examine the old trunk in the corner.", "Look out the window for signs of help."])
    if choice == 0:
        survival_ending() # Lucky choice
    else:
        death_ending() # Unlucky choice

def survival_ending():
    print("\nYou open the old trunk and find a hidden passage! It leads out of the mansion.")
    print("You escape Blackwood Mansion, forever haunted by its secrets, but alive.")
    print("Survival Ending.")

def escape_ending():
    print("\nYou frantically search and find a loose brick in the wall. Behind it, a narrow tunnel.")
    print("You crawl through, emerging outside, far from the cursed mansion. You escaped!")
    print("Escape Ending.")

def death_ending():
    print("\nAs you investigate, the floor gives way! You fall into darkness...")
    print("The mansion claims another victim. Your journey ends here.")
    print("Death Ending.")

def play_game():
    creepy_intro()
    hallway()

if __name__ == "__main__":
    play_game()