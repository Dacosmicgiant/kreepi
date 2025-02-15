import random

# Lore variables - set the backstory elements here
BLACKWOOD_TRAGEDY = "a dark pact with an entity"
MANSION_PURPOSE = "a secluded research lab focused on spiritual energies"
HORROR_SOURCE = "restless spirits bound by a corrupted ritual"

lore_hints_found = set()
player_inventory = []
sanity_level = 100  # Initialize sanity level
ghost_helped = False # Track if the player helped the ghost for ending variations

def modify_sanity(amount):
    global sanity_level
    sanity_level += amount
    sanity_level = max(0, min(100, sanity_level)) # Keep sanity within 0-100 range
    if sanity_level <= 30:
        print("\nYour sanity is fraying. The mansion's horrors are taking their toll. Reality seems to blur at the edges.")
    elif sanity_level <= 60:
        print("\nYour unease grows. The oppressive atmosphere of Blackwood Mansion is starting to affect your mind.")

def creepy_intro():
    print("The rusted gates of Blackwood Mansion swing shut with a mournful clang, sealing you within the estate's suffocating embrace.  A chilling wind whispers through the ancient oaks, carrying the scent of damp earth and decay.")
    print("The mansion looms before you, a gothic monolith against the bruised purple of the twilight sky. Its darkened windows stare like vacant eyes, promising no solace, only secrets.")
    print(f"Local legends whisper of {BLACKWOOD_TRAGEDY} that befell the Blackwood family within these walls. Some say the mansion was originally {MANSION_PURPOSE}, a place now tainted by darkness.")
    print(f"You came seeking answers, lured by these tales and whispers of {HORROR_SOURCE}. Now, trapped within its crumbling walls, the thrill of investigation has curdled into icy dread.")
    print("A palpable sense of unease settles upon you. The very stones of Blackwood Mansion seem to breathe with a dark sentience. Escape is paramount, but the mansion itself seems unwilling to release you.")
    print("Your heart pounds a frantic rhythm against your ribs. Will you unravel the mysteries of Blackwood Mansion and escape its grasp? Or will you become another forgotten soul lost within its shadowed halls?")
    print()

def make_choice(prompt, choices):
    print(prompt)
    for i, choice in enumerate(choices):
        print(f"{i+1}. {choice}")
    if player_inventory:
        print("\nInventory:")
        for item in player_inventory:
            print(f"- {item}")
    while True:
        try:
            choice_index = int(input("Enter your choice: ")) - 1
            if 0 <= choice_index < len(choices):
                return choice_index
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def random_event(location):
    sound_events = [
        "The faint sound of dragging chains echoes from somewhere deeper within the mansion.",
        "A single, high-pitched note rings out, abruptly cutting through the silence.",
        "You hear a muffled sob, like a child weeping softly in another room.",
        "A low, guttural growl rumbles from the shadows, sending shivers down your spine.",
        "The distinct sound of shattering glass echoes from upstairs, followed by eerie silence.",
        "A faint whisper, too indistinct to understand, seems to brush against your ear.",
        "You hear the creak of footsteps on the floorboards above, though you know you are alone.",
        "A melancholic piano melody drifts from a distant room, mournful and unsettling.",
        "The grandfather clock in the hallway chimes an uneven number of times, its tone strangely distorted."
    ]
    sensory_events = [
        "The air suddenly thickens, heavy with the metallic tang of blood.",
        "You feel a cold breath on the back of your neck, raising goosebumps despite the clammy air.",
        "A cloying, sweet smell of decay overwhelms you, making your stomach churn.",
        "The temperature plummets drastically, and you see your breath cloud in the frigid air.",
        "You feel a prickling sensation on your skin, as if unseen eyes are watching you intently.",
        "The scent of ozone fills the air, like the aftermath of a violent storm, despite the clear sky.",
        "A wave of nausea washes over you, accompanied by a sudden, sharp headache.",
        "You taste a metallic bitterness in your mouth, though you haven't eaten anything.",
        "The air grows heavy with the scent of incense and something ancient, like dust and tombs."
    ]
    visual_events = [
        "Portraits on the wall seem to subtly shift their expressions, their painted eyes following you.",
        "Shadows lengthen and twist into impossible shapes, dancing in your peripheral vision.",
        "Faint, ghostly figures flicker at the edge of your vision, then vanish when you focus.",
        "A mirror's reflection momentarily distorts, showing a glimpse of something monstrous before returning to normal.",
        "Dust motes swirl around you in unnatural vortexes, forming fleeting, ghostly shapes.",
        "A flickering light source casts grotesque, dancing shadows that mimic human forms.",
        "You catch a glimpse of movement in a darkened corner, but when you look directly, nothing is there.",
        "The wallpaper seems to subtly writhe and shift, patterns changing and reforming before your eyes.",
        "Outside the window, the trees seem to twist into clawing shapes against the bruised twilight sky."
    ]
    dynamic_events = {
        "basement_hall": [
            "Water drips incessantly from the ceiling, echoing loudly in the silence.",
            "You hear the faint sound of rushing water from deeper within the basement.",
            "Dampness clings to the stone walls, and puddles of stagnant water collect on the floor."
        ],
        "attic": [
            "Dust motes dance in the weak light filtering through cracks, thick as fog.",
            "You hear the scurrying of unseen creatures in the rafters above.",
            "A gust of wind rattles the boarded-up windows, sending a shiver of cold air through the attic."
        ],
        "garden": [
            "The mist thickens suddenly, obscuring your vision and dampening sound.",
            "The sickly sweet scent of the garden's strange blossoms intensifies, becoming cloying.",
            "You hear the rustling of unseen things moving within the overgrown hedges."
        ],
        "chapel": [
            "The scent of incense suddenly intensifies, becoming almost overpowering.",
            "Faint chanting seems to emanate from the altar, too low to decipher words.",
            "The stained-glass window casts distorted, unsettling patterns of light across the chapel floor."
        ],
        "servants_quarters": [
            "The air grows colder and more oppressive, the claustrophobia intensifying.",
            "You hear a faint, rhythmic scrubbing sound, like someone endlessly cleaning in another room.",
            "A whisper of resentment seems to linger in the air, the echoes of forgotten servants."
        ],
        "scullery": [
            "The dripping of water in the scullery echoes like a metronome counting down to something.",
            "The smell of rot and mildew intensifies, making your stomach churn.",
            "You hear the faint clatter of unseen dishes shifting on the shelves."
        ],
        "study": [
            "The rustling of paper seems to come from the bookshelves, as if unseen hands are turning pages.",
            "The oil lamp on the desk flickers wildly, casting long, distorted shadows across the room.",
            "You hear a faint scratching sound, like quill on parchment, from somewhere within the study."
        ],
        "greenhouse_interior": [
            "The air grows even more humid and stifling, making it hard to breathe.",
            "The luminous fungi pulse with a brighter, more unsettling glow.",
            "You hear the rustling of overgrown plants, as if they are shifting and moving on their own."
        ],
        "dining_room": [
            "The stench of stale food intensifies, becoming truly nauseating.",
            "Buzzing flies seem to swarm louder around the decaying feast.",
            "You hear the faint clinking of silverware, as if a ghostly dinner party is about to begin."
        ],
        "kitchen": [
            "The metallic tang of old blood mixes with the smell of decay.",
            "You hear the skittering of rats behind the walls.",
            "A meat cleaver lies abandoned on a butcher block, its blade gleaming faintly in the dim light."
        ],
        "basement_stairs": [
            "The air grows heavy with the smell of damp earth and mildew.",
            "You hear the faint dripping of water echoing from below.",
            "The wooden steps groan ominously under your weight."
        ],
        "basement_storage": [
            "The scent of old wine and dust fills the air.",
            "You hear the rustling of unseen things in the shadows.",
            "Cobwebs hang thick as curtains, obscuring the corners of the room."
        ],
        "basement_ritual_chamber": [
            "The air crackles with a palpable, unsettling energy.",
            "You smell incense and ozone, a strange and disturbing combination.",
            "Faint whispers seem to emanate from the very stones of the chamber."
        ],
        "library": [
            "The scent of aged paper and leather is overpowering.",
            "You hear the rustling of pages turning in the silence.",
            "The towering shelves seem to lean in, pressing down on you."
        ],
        "master_bedroom": [
            "A faint floral perfume lingers in the dusty air, a ghost of elegance.",
            "You hear the soft rustle of silk, like a dress brushing against the floor.",
            "The four-poster bed dominates the room, casting long, eerie shadows."
        ],
        "bathroom": [
            "The air is damp and cold, smelling of mildew and stagnant water.",
            "You hear the drip, drip, drip of a leaky faucet, echoing in the silence.",
            "Cracked tiles and a stained porcelain tub create a sense of decay."
        ],
        "dressing_room": [
            "The scent of mothballs and old fabric hangs heavy in the air.",
            "You hear the faint creaking of hangers on the empty衣架.",
            "Mirrors reflect distorted images of the room, playing tricks on your eyes."
        ],
        "landing": [
            "The silence here is almost deafening, amplifying every creak and groan of the house.",
            "You feel exposed and watched in this open space.",
            "Shadows stretch long and distorted from the corners of the landing."
        ],
        "attic_storage": [
            "The air is thick with dust and the smell of forgotten things.",
            "You hear the scurrying of rats in the rafters.",
            "Sunlight filtering through cracks in the boarded windows creates eerie light patterns."
        ],
        "attic_ritual_room": [
            "The oppressive atmosphere intensifies, making it hard to breathe.",
            "You smell burnt herbs and something acrid, like battery acid.",
            "Strange symbols are chalked on the floor, radiating a faint, unsettling energy."
        ]
    }

    chosen_event = None

    if location in dynamic_events and random.random() < 0.6:
        chosen_event = random.choice(dynamic_events[location])
    elif random.random() < 0.5:
        event_type = random.choice(["sound", "sensory", "visual"])
        if event_type == "sound":
            chosen_event = random.choice(sound_events)
        elif event_type == "sensory":
            chosen_event = random.choice(sensory_events)
        elif event_type == "visual":
            chosen_event = random.choice(visual_events)
    else:
        chosen_event = random.choice(sound_events + sensory_events + visual_events)

    if chosen_event:
        if sanity_level < 50:
            print(f"Your mind, already strained, interprets the sounds as {chosen_event.lower()}... or is it something worse? Your senses are no longer reliable.")
        else:
            print(chosen_event)
        print()
        modify_sanity(-2)

# Core Location Functions
def hallway():
    print("\nYou stand in the grand hallway. A massive grandfather clock dominates the space, its pendulum still.")
    print("Portraits line the walls, their eyes seeming to follow you. A grand staircase leads upward.")
    random_event("hallway")
    choices = [
        "Inspect the grandfather clock",
        "Examine the portraits",
        "Ascend the staircase",
        "Return to mansion entrance"
    ]
    choice = make_choice("Choose your path:", choices)
    
    if choice == 0:
        print("\nAs you approach the clock, its hands suddenly spin wildly! The clock face opens like a gaping maw...")
        print("Death Ending: Consumed by the Clock")
        trapped_ending_mansion_bound()
    elif choice == 1:
        study()
    elif choice == 2:
        landing()
    elif choice == 3:
        mansion_entrance()

def landing():
    print("\nYou reach the upper landing. Dust motes swirl in dim light streaming through cracked windows.")
    print("Before you: a master bedroom door, bathroom entrance, and staircase leading back down.")
    random_event("landing")
    choices = [
        "Enter master bedroom",
        "Go to bathroom", 
        "Descend to hallway"
    ]
    choice = make_choice("Where will you go?", choices)
    
    if choice == 0:
        master_bedroom()
    elif choice == 1:
        bathroom()
    elif choice == 2:
        hallway()

def study():
    print("\nYou enter a dusty study filled with ancient tomes. A massive oak desk dominates the center of the room.")
    random_event("study")
    choices = [
        "Search the bookshelves",
        "Examine the desk",
        "Return to hallway"
    ]
    choice = make_choice("What will you investigate?", choices)
    
    if choice == 0:
        library()
    elif choice == 1:
        print("\nAs you open the desk drawer, a hidden needle pricks your finger...")
        print("Death Ending: Poisoned Secret")
        trapped_ending_mansion_bound()
    elif choice == 2:
        hallway()

def library():
    print("\nThe library contains floor-to-ceiling bookshelves filled with ancient volumes. Dust hangs thick in the air.")
    random_event("library")
    choices = [
        "Search for useful books",
        "Examine the windows",
        "Return to study"
    ]
    choice = make_choice("What will you do?", choices)
    
    if choice == 0:
        print("\nYou find a hidden compartment containing an old journal!")
        print("Escape Ending: Secret Passage Discovered")
        trapped_ending_mansion_bound()
    elif choice == 1:
        print("\nAs you peer through the grimy windows, shadowy hands burst through the glass...")
        print("Death Ending: Shattered Remains")
        trapped_ending_mansion_bound()
    elif choice == 2:
        study()

def master_bedroom():
    print("\nThe master bedroom contains a four-poster bed with tattered curtains. A vanity mirror reflects distorted images.")
    random_event("master_bedroom")
    choices = [
        "Inspect the bed",
        "Check the vanity",
        "Return to landing"
    ]
    choice = make_choice("What will you examine?", choices)
    
    if choice == 0:
        print("\nThe bed curtains suddenly wrap around you like burial shrouds...")
        print("Death Ending: Eternal Slumber")
        trapped_ending_mansion_bound()
    elif choice == 1:
        print("\nYou find a silver key hidden in the vanity!")
        player_inventory.append("silver_key")
        print("Added silver key to inventory")
        master_bedroom()
    elif choice == 2:
        landing()

def bathroom():
    print("\nThe bathroom features a clawfoot tub and cracked mirror. Rust stains mar the porcelain fixtures.")
    random_event("bathroom")
    choices = [
        "Examine the mirror",
        "Inspect razor on sink", 
        "Return to bedroom"
    ]
    choice = make_choice("What will you investigate?", choices)
    
    if choice == 0:
        print("\nYour reflection reaches out and pulls you into the glass...")
        print("Death Ending: Mirror Prison")
        trapped_ending_mansion_bound()
    elif choice == 1:
        attic_stairs()
    elif choice == 2:
        landing()

def attic_stairs():
    print("\nA hidden staircase leads up to the attic. The wooden steps creak dangerously under your weight.")
    random_event("attic")
    choices = [
        "Continue upward",
        "Return to bathroom"
    ]
    choice = make_choice("Will you proceed?", choices)
    
    if choice == 0:
        attic()
    else:
        bathroom()

def attic():
    print("\nThe dusty attic contains old furniture covered in sheets. Cold wind whistles through broken windows.")
    random_event("attic")
    choices = [
        "Search storage trunks",
        "Approach the window",
        "Return downstairs"
    ]
    choice = make_choice("What will you do?", choices)
    
    if choice == 0:
        print("\nYou find a ritual dagger wrapped in ancient cloth!")
        player_inventory.append("ritual_dagger")
        print("Added ritual dagger to inventory")
        attic()
    elif choice == 1:
        print("\nA sudden gust blows you out through the broken window...")
        print("Death Ending: Final Fall")
        trapped_ending_mansion_bound()
    elif choice == 2:
        attic_stairs()

def trapped_ending_mansion_bound():
    print("\nThe mansion's dark energy prevents true escape. Though you leave physically, its horrors haunt you forever.")
    print("TRAPPED ENDING: Mansion Bound")
    play_again()

def play_again():
    choice = input("\nPlay again? (y/n): ").lower()
    if choice == 'y':
        global sanity_level, player_inventory, lore_hints_found, ghost_helped
        sanity_level = 100
        player_inventory = []
        lore_hints_found = set()
        ghost_helped = False
        creepy_intro()
        mansion_gates()
    else:
        print("Thanks for playing!")

def mansion_gates():
    print("\nThe rusted iron gates stand before you, leading to the decaying mansion.")
    random_event("mansion_gates")
    choices = ["Enter through main gates", "Search perimeter"]
    if "silver_key" in player_inventory:
        choices.append("Use silver key on gate lock")
    
    choice = make_choice("Choose your approach:", choices)
    
    if choice == 0:
        mansion_entrance()
    elif choice == 1:
        print("\nYou find nothing but overgrown vegetation and crumbling walls.")
        mansion_gates()
    elif choice == 2 and "silver_key" in player_inventory:
        print("\nThe silver key fits perfectly in the ancient lock!")
        print("ESCAPE ENDING: Freedom Through Perseverance")
        play_again()

def mansion_entrance():
    print("\nThe massive oak doors creak open to reveal a grand but decaying foyer.")
    random_event("mansion_entrance")
    choices = [
        "Enter the hallway",
        "Retreat to gates"
    ]
    choice = make_choice("What will you do?", choices)
    
    if choice == 0:
        hallway()
    else:
        mansion_gates()

# Start the game
creepy_intro()
mansion_gates()