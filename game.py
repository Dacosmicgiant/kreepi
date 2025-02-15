import random

def creepy_intro():
    print("The wrought iron gates of Blackwood Mansion groan shut behind you, the click echoing like a death knell.")
    print("A chilling mist clings to the overgrown grounds, and the mansion looms before you, a silhouette against the bruised twilight sky.")
    print("You came seeking answers, drawn by whispers of forgotten tragedies, but now, trapped within its decaying walls, you only seek escape.")
    print("A sense of dread washes over you. The air itself feels heavy, pregnant with secrets and sorrow.")
    print("Your heart hammers against your ribs. Will you uncover the mansion's dark secrets? Or become another ghost within its walls?")
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
        "A cold gust of wind rattles the windows, though there's no breeze outside.",
        "You hear a faint, mournful sigh carried on the stagnant air.",
        "Shadows flicker in your peripheral vision, dancing like unseen figures.",
        "The scent of decay and dust intensifies, making your stomach churn.",
        "A floorboard groans above you, as if something is pacing in the empty rooms.",
        "You catch a glimpse of movement in a darkened corner, but it vanishes when you look directly.",
        "A whisper brushes your ear, too indistinct to understand, yet chillingly close.",
        "The temperature plummets, and you see your breath mist in the air.",
        "A portrait on the wall seems to watch you, its eyes following your every move."
    ]
    if random.random() < 0.4: # Increased chance of event
        print(random.choice(events))
        print()

def mansion_gates():
    print("You stand before the imposing mansion gates, now firmly shut. The path ahead leads to the main entrance, but to your left, a shadowed garden path disappears into the mist.")
    random_event()
    choice = make_choice("Which way do you proceed?", ["Approach the mansion entrance.", "Explore the garden path."])
    if choice == 0:
        mansion_entrance()
    else:
        garden_path()

def mansion_entrance():
    print("You cautiously approach the mansion's heavy oak doors. They are slightly ajar, a silent invitation or a grim warning.")
    random_event()
    choice = make_choice("Do you:", ["Push open the doors and enter.", "Try to peer through the crack before entering."])
    if choice == 0:
        hallway()
    else:
        peer_crack()

def peer_crack():
    print("Peering through the crack, you see a dimly lit hallway, stretching into shadow. A grandfather clock stands silent, its hands frozen. You sense a presence within, waiting.")
    random_event()
    choice = make_choice("Do you still:", ["Enter the mansion.", "Turn back and try the garden path again."])
    if choice == 0:
        hallway()
    else:
        garden_path() # Go back to garden path choice

def garden_path():
    print("You venture onto the overgrown garden path. Twisted vines claw at the crumbling stone, and sickly sweet flowers emit a cloying perfume. The path winds deeper into the mist-shrouded garden.")
    random_event()
    choice = make_choice("Do you:", ["Follow the path deeper into the garden.", "Return to the mansion gates and try the entrance."])
    if choice == 0:
        garden_maze()
    else:
        mansion_entrance() # Go back to mansion entrance choice

def garden_maze():
    print("The garden path becomes a disorienting maze of overgrown hedges and decaying statues. You feel lost, the mansion hidden from view. Strange shapes seem to shift in the mist.")
    random_event()
    choice = make_choice("Do you:", ["Push through a particularly dense hedge.", "Try to retrace your steps back to the garden path entrance."])
    if choice == 0:
        library() # New location from garden
    else:
        mansion_gates() # Go back to mansion gates choice

def hallway():
    print("You are now in the main hallway. The air is heavy with the scent of dust and age. To your left, a grand but creaking staircase ascends into darkness. Straight ahead, a shadowy doorway hints at a deeper part of the house. To your right, a heavy oak door is slightly ajar.")
    random_event()
    choice = make_choice("Which direction do you explore?", ["Ascend the staircase.", "Go through the shadowy doorway.", "Open the oak door to the right."])
    if choice == 0:
        attic()
    elif choice == 1:
        basement_hall() # Changed to basement hallway first
    else:
        library() # New location from hallway

def basement_hall():
    print("You step through the shadowy doorway and find yourself in a narrow basement hallway. The air is cold and damp, and the stone walls weep with moisture. The dripping sound echoes loudly.")
    random_event()
    choice = make_choice("Do you:", ["Follow the hallway deeper into the darkness.", "Investigate a side passage dimly lit by a flickering candle."])
    if choice == 0:
        basement_chamber() # Deeper basement
    else:
        basement_side_passage() # Side passage

def basement_side_passage():
    print("You cautiously enter the side passage. The flickering candle casts long, dancing shadows on the walls, revealing strange symbols etched into the stone. The air grows colder, and you feel a prickling sensation on your skin.")
    random_event()
    choice = make_choice("Do you:", ["Examine the strange symbols more closely.", "Quickly retreat back to the basement hallway."])
    if choice == 0:
        death_ending_basement_symbols() # Risky choice - symbol related death
    else:
        basement_hall() # Back to basement hallway

def basement_chamber():
    print("The basement hallway opens into a large, circular chamber. In the center, a dark pool of water reflects the faint light from above. An unsettling silence hangs in the air, broken only by the occasional drip.")
    random_event()
    choice = make_choice("Do you:", ["Peer into the dark pool.", "Search the edges of the chamber for another exit."])
    if choice == 0:
        death_ending_pool() # Very risky choice - pool related death
    else:
        escape_ending_basement() # Chance of escape in basement

def library():
    print("You push open the heavy oak door and enter a grand library. Bookshelves stretch to the high ceiling, filled with ancient, leather-bound volumes. Dust motes dance in the faint light filtering through stained-glass windows. A sense of forgotten knowledge permeates the room.")
    random_event()
    choice = make_choice("Do you:", ["Browse the bookshelves for a hidden book or clue.", "Examine a large, ornate desk in the center of the room."])
    if choice == 0:
        survival_ending_library_book() # Lucky choice - book leads to survival
    else:
        attic() # Misdirection - desk leads to attic

def attic():
    print("You climb the rickety staircase to the dusty attic. Moonlight spills through cracks in the boarded-up windows, illuminating cobwebs thick as shrouds and forgotten furniture draped in white sheets. The air is stifling and smells of decay.")
    random_event()
    choice = make_choice("Do you:", ["Investigate a large, shadowed corner.", "Look for a way out through the boarded windows."])
    if choice == 0:
        death_ending_attic_corner() # Risky choice - corner leads to death
    else:
        escape_ending_attic_window() # Chance of escape from attic

def survival_ending_library_book():
    print("\nYou carefully examine the bookshelves and discover a hidden compartment behind a loose book. Inside, you find a tarnished silver key and a faded map.")
    print("The map reveals a secret passage behind the library fireplace. You use the key, find the passage, and emerge outside, blinking in the fresh air. You survived Blackwood Mansion, carrying its secrets with you.")
    print("Survival Ending: The Scholar's Escape.")

def escape_ending_basement():
    print("\nYou diligently search the chamber walls and discover a crumbling section hidden behind a tapestry. You pull it away to reveal a narrow, damp tunnel.")
    print("You squeeze through the tunnel, crawling for what feels like an eternity, until you finally emerge into the night, far from the mansion's oppressive presence. You escaped the basement's depths!")
    print("Escape Ending: The Tunnel Run.")

def escape_ending_attic_window():
    print("\nYou cautiously approach the boarded windows and find one section that is weaker than the rest. With a surge of adrenaline, you kick it open, creating a narrow escape route.")
    print("You climb out onto the roof and carefully make your way down, leaving Blackwood Mansion behind, silhouetted against the moon. You escaped the attic's clutches!")
    print("Escape Ending: The Rooftop Descent.")

def death_ending_basement_symbols():
    print("\nAs you trace the strange symbols, the candle flame flares violently, then extinguishes. The passage plunges into absolute darkness, and a chilling voice whispers in your ear, 'You should not have looked.'")
    print("Something unseen grasps you from the darkness, and your screams echo unheard in the silent mansion. Your curiosity becomes your doom. ")
    print("Death Ending: Symbol's Curse.")

def death_ending_pool():
    print("\nYou lean closer to the dark pool, peering into its depths. Suddenly, a cold hand erupts from the water, seizing your arm and dragging you down into the icy blackness.")
    print("You struggle, but the unseen force is too strong. The dark water closes over your head, silencing your cries. The pool claims another soul.")
    print("Death Ending: Drowned in Darkness.")

def death_ending_attic_corner():
    print("\nYou cautiously approach the shadowed corner, your heart pounding. As you reach out to touch the wall, something lunges from the darkness – a grotesque, shadowy figure with glowing red eyes.")
    print("It shrieks, a sound that tears at your sanity, and its icy claws tear into you. You collapse, your lifeblood draining away in the dust of the attic. The shadow claims you.")
    print("Death Ending: Shadow's Embrace.")


def play_game():
    creepy_intro()
    mansion_gates() # Start at the gates

if __name__ == "__main__":
    play_game()