import random

# Lore variables - set the backstory elements here
BLACKWOOD_TRAGEDY = "the unspeakable Blackwood Tragedy of 1892"
MANSION_PURPOSE = "originally built as a lavish family estate, but secretly served as a research lab"
HORROR_SOURCE = "restless spirits, twisted by a failed ritual, and perhaps something darker"

# Blackwood Family Backstory
BLACKWOOD_FAMILY_LORE = {
    "Lord Alistair Blackwood": "The patriarch, obsessed with occult studies and rumored to have made a dark pact.",
    "Lady Elara Blackwood": "Alistair's wife, known for her beauty and rumored to possess psychic sensitivities. She vanished during the Tragedy.",
    "Their Son, Edwin Blackwood": "A sickly child, often confined to his room. Some say he was the focus of his father's experiments.",
    "The Loyal Servant, Mr. Grimshaw": "The stern and ever-present butler, fiercely loyal to the Blackwood family, even in their darkest hours."
}

SPIRIT_MOTIVATIONS = [
    "vengeance for a terrible betrayal",
    "a desperate plea for release from torment",
    "to guard a hidden secret at all costs",
    "to lure others into the mansion's darkness",
    "a mournful longing for what was lost"
]

LORE_RIDDLE_GRANDFATHER_CLOCK = "I have a face but no eyes, hands but no arms, and tell tales but have no voice. What am I?"
LORE_RIDDLE_ANSWER_GRANDFATHER_CLOCK = "A clock"

lore_hints_found = set()
player_inventory = []
sanity_level = 100  # Initialize sanity level
ghost_helped = False # Track if the player helped the ghost for ending variations
clock_puzzle_solved = False # Track if grandfather clock puzzle is solved

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
        ],
        "mansion_gates": [
            "The wind howls through the gates, sounding like mournful whispers.",
            "You feel an inexplicable sense of being watched from the mansion's darkened windows.",
            "The iron of the gates feels strangely cold to the touch, even for iron."
        ],
        "mansion_entrance": [
            "The foyer is colder than outside, a distinct chill that raises goosebumps.",
            "Dust motes hang heavy in the air, undisturbed for decades.",
            "You catch a faint whiff of incense, quickly masked by the pervasive smell of decay."
        ],
        "hallway": [
            "The pendulum of the grandfather clock is still, yet you swear you hear a faint ticking.",
            "The eyes in the portraits seem to follow you with unsettling intensity.",
            "A draft snakes through the hallway, carrying a whisper of unknown origin."
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
    global clock_puzzle_solved
    print("\nYou stand in the grand hallway. A massive grandfather clock dominates the space, its pendulum still.")
    print("Portraits line the walls, their eyes seeming to follow you. You notice one portrait in particular - a stern-faced man with piercing eyes, a plaque below reads 'Lord Alistair Blackwood'.") # Visual Lore Hint - Family Portrait
    print("A grand staircase leads upward.")
    random_event("hallway")
    choices = [
        "Inspect the grandfather clock",
        "Examine the portraits",
        "Ascend the staircase",
        "Return to mansion entrance"
    ]
    if "silver_locket" in player_inventory and not clock_puzzle_solved:
        choices.insert(1, "Use silver locket on grandfather clock") # Inventory Usage - Silver Locket on Clock

    choice = make_choice("Choose your path:", choices)

    if choice == 0:
        if clock_puzzle_solved:
            basement_stairs() # Clock is already solved, leads to basement
        else:
            print("\nAs you approach the clock, its hands suddenly spin wildly! The clock face is covered in strange symbols, not numbers.") # Puzzle Intro - Grandfather Clock Riddle
            print("Perhaps there's a clue somewhere in the mansion to decipher these symbols...")
            hallway() # Stay in hallway, puzzle not solved yet
    elif choice == 1:
        study()
    elif choice == 2:
        landing()
    elif choice == 3:
        mansion_entrance()
    elif "silver_locket" in player_inventory and not clock_puzzle_solved and choice == 4: # Inventory Choice - Silver Locket on Clock
        print("\nYou hold the silver locket to the grandfather clock. As it touches the clock face, the locket warms in your hand.")
        print("The clock symbols glow faintly, and you hear a soft click.")
        print("The clock face now displays numbers, and a small compartment opens below the clock face, revealing a rusty key.") # Puzzle Solved - Clock Riddle
        player_inventory.append("rusty_key")
        print("Added rusty key to inventory")
        clock_puzzle_solved = True
        hallway() # Stay in hallway, puzzle solved

def landing():
    print("\nYou reach the upper landing. Dust motes swirl in dim light streaming through cracked windows.")
    print("A faint, melancholic piano melody drifts up from downstairs. It seems to emanate from the hallway below.") # Auditory Lore Hint
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
    print("The air is thick with the scent of aged paper and something else... something faintly metallic, like old blood.") # Sensory Lore Hint
    print("On the desk, you see an open book of riddles. One riddle is circled: 'I have a face but no eyes, hands but no arms, and tell tales but have no voice. What am I?'") # Lore Hint - Riddle Book
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
    print("You spot a section of shelves that seems slightly askew, almost hidden in shadow.") # Visual Lore Hint - Hidden Section
    random_event("library")
    choices = [
        "Search for useful books",
        "Examine the windows",
        "Investigate the hidden shelf section", # New Choice - Interactive Lore Hint
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
    elif choice == 2: # Interactive Lore Hint Choice
        print("\nYou carefully examine the shelf section. It seems to be a false wall!")
        print("Behind it, you discover a small, dusty alcove.")
        print("Within the alcove, you find a tarnished silver locket. It's cold to the touch.") # Lore Item - Silver Locket
        if "silver_locket" not in player_inventory:
            player_inventory.append("silver_locket")
            print("Added silver locket to inventory")
            print("The locket feels strangely significant...") # Meaningful Lore Hint - Item Significance
        library() # Stay in library after finding locket
    elif choice == 3:
        study()

def master_bedroom():
    print("\nThe master bedroom contains a four-poster bed with tattered curtains. A vanity mirror reflects distorted images.")
    print("A woman's silk dress lies discarded on a chair, as if hastily cast aside. A faint, lingering perfume fills the air.") # Visual & Sensory Lore Hint - Lady Elara's presence
    random_event("master_bedroom")
    choices = [
        "Inspect the bed",
        "Check the vanity",
        "Examine the discarded dress", # New Choice - Interactive Lore Hint
        "Return to landing"
    ]
    if "silver_locket" in player_inventory:
        choices.insert(2, "Use silver locket on vanity mirror") # Inventory Usage - Silver Locket on Mirror

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
    elif choice == 2: # Interactive Lore Hint Choice
        print("\nYou pick up the silk dress. It's surprisingly cold and seems to whisper faintly as you touch it.")
        print("You find a small, embroidered handkerchief tucked into a pocket. The initials 'E.B.' are stitched into the corner.") # Lore Item & Hint - Lady Elara's Handkerchief
        if "elara_handkerchief" not in player_inventory:
            player_inventory.append("elara_handkerchief")
            print("Added Elara's handkerchief to inventory")
            print("The initials 'E.B.' seem familiar...") # Meaningful Lore Hint - Player might recall Lady Elara's name from lore
        modify_sanity(-5) # Sanity decrease for interacting with potentially haunted item
        master_bedroom()
    elif "silver_locket" in player_inventory and choice == 3: # Inventory Choice - Silver Locket on Mirror
        print("\nYou hold the silver locket up to the vanity mirror. The distorted reflection seems to ripple.")
        print("For a moment, you see a clear image in the mirror - a beautiful woman with sad eyes, reaching out as if pleading for help.") # Lore Reveal - Lady Elara's Spirit
        print("Then, the reflection shatters back into distortion. You feel a wave of sorrow and longing wash over you.")
        modify_sanity(-10) # Sanity decrease for witnessing ghostly image
        master_bedroom()
    elif choice == 4:
        landing()

def bathroom():
    print("\nThe bathroom features a clawfoot tub and cracked mirror. Rust stains mar the porcelain fixtures.")
    print("Water drips steadily from the faucet into the stained tub, each drop echoing in the oppressive silence.")
    random_event("bathroom")
    choices = [
        "Examine the mirror",
        "Inspect razor on sink",
        "Return to landing"
    ]
    if "elara_handkerchief" in player_inventory:
        choices.insert(1, "Use Elara's handkerchief on mirror") # Inventory Usage - Handkerchief on Mirror

    choice = make_choice("What will you investigate?", choices)

    if choice == 0:
        print("\nYour reflection reaches out and pulls you into the glass...")
        print("Death Ending: Mirror Prison")
        trapped_ending_mansion_bound()
    elif choice == 1:
        attic_stairs()
    elif choice == 2:
        landing()
    elif "elara_handkerchief" in player_inventory and choice == 3: # Inventory Choice - Handkerchief on Mirror
        print("\nYou gently wipe the cracked mirror with Elara's handkerchief.")
        print("The grime clears, and for a moment, the reflection seems clearer than before. You notice faint etchings on the mirror's surface, previously hidden by the grime.") # Environmental Puzzle - Etchings revealed
        print("The etchings seem to be symbols... perhaps they form a word or phrase?") # Puzzle Hint - Etchings are symbols
        lore_hints_found.add("etchings_on_mirror") # Track lore hint for future use
        bathroom() # Stay in bathroom

def attic_stairs():
    print("\nA hidden staircase leads up to the attic. The wooden steps creak dangerously under your weight.")
    print("You hear a faint scratching sound from above, like nails on wood, growing louder as you ascend.") # Auditory Lore Hint - Sound from Attic
    random_event("attic")
    choices = [
        "Continue upward (risky)",
        "Return to bathroom"
    ]
    choice = make_choice("Will you proceed?", choices)

    if choice == 0:
        if sanity_level <= 40: # Skill Check - Sanity Level
            print("\nYour footing is unsteady, your mind clouded by fear. You misstep on the creaking stairs...")
            print("You stumble, losing your balance, and fall back down the stairs with a sickening thud.")
            print("You are injured and disoriented.")
            modify_sanity(-10) # Sanity and slight "damage" (sanity loss) for failure
            bathroom() # Return to bathroom after fall
        else:
            print("\nYou carefully ascend the creaking attic stairs...")
            attic() # Success - Proceed to attic
    else:
        bathroom()

def attic():
    print("\nThe dusty attic contains old furniture covered in sheets. Cold wind whistles through broken windows.")
    print("In the center of the room, you see a trunk slightly ajar. A faint, sickly sweet smell emanates from it.") # Visual & Sensory Lore Hint - Trunk and Smell
    random_event("attic")
    choices = [
        "Search storage trunks",
        "Approach the window",
        "Return downstairs"
    ]
    if "ritual_dagger" in player_inventory:
        choices.insert(1, "Use ritual dagger on trunk") # Inventory Usage - Ritual Dagger on Trunk

    choice = make_choice("What will you do?", choices)

    if choice == 0:
        print("\nYou find a ritual dagger wrapped in ancient cloth!") # Original item find - now redundant, but keep for now
        player_inventory.append("ritual_dagger") # Still add dagger if player somehow chooses this first
        print("Added ritual dagger to inventory")
        attic()
    elif choice == 1 and "ritual_dagger" in player_inventory: # Inventory Choice - Ritual Dagger on Trunk
        print("\nYou cautiously approach the trunk and use the ritual dagger to pry it open.")
        print("The trunk bursts open with a snap! Inside, you find a collection of disturbing occult artifacts and a blood-stained diary.") # Item Find - Occult Artifacts & Diary (Lore)
        player_inventory.append("occult_diary") # Lore Item - Occult Diary
        print("Added occult diary to inventory")
        print("The diary seems to contain Lord Blackwood's unsettling research notes...") # Meaningful Lore Hint - Diary content
        modify_sanity(-8) # Sanity loss for opening disturbing trunk
        attic()
    elif choice == 2:
        print("\nA sudden gust blows you out through the broken window...")
        print("Death Ending: Final Fall")
        trapped_ending_mansion_bound()
    elif choice == 3:
        attic_stairs()

def basement_stairs():
    print("\nStairs descend into the darkness of the basement. A cold, damp air rises from below.")
    print("You hear a faint, rhythmic dripping sound echoing from the basement depths.")
    random_event("basement_stairs")
    choices = [
        "Descend into basement",
        "Return to hallway"
    ]
    choice = make_choice("Will you go down?", choices)

    if choice == 0:
        basement_hall()
    else:
        hallway()

def basement_hall():
    print("\nYou are in a damp basement hall. Stone walls surround you, and the air is heavy with mildew.")
    print("To the north, you see a storage area. To the east, a heavy wooden door bound with iron.")
    random_event("basement_hall")
    choices = [
        "Explore storage area (north)",
        "Investigate iron-bound door (east)",
        "Return to basement stairs"
    ]
    choice = make_choice("Where to now?", choices)

    if choice == 0:
        basement_storage()
    elif choice == 1:
        basement_ritual_chamber_door() # New location - door to ritual chamber
    elif choice == 2:
        basement_stairs()

def basement_storage():
    print("\nThe basement storage room is filled with dusty shelves and forgotten crates. The smell of old wine is strong here.")
    print("Cobwebs hang like macabre decorations, and shadows dance in every corner.")
    random_event("basement_storage")
    choices = [
        "Search the shelves",
        "Examine the crates",
        "Return to basement hall"
    ]
    choice = make_choice("What will you search?", choices)

    if choice == 0:
        print("\nYou find a bottle of old wine, still sealed. It looks incredibly aged... and possibly tainted.") # Item - Old Wine (maybe for later use or sanity effect?)
        player_inventory.append("old_wine")
        print("Added old wine to inventory")
        basement_storage()
    elif choice == 1:
        print("\nYou find a dusty, leather-bound book in one of the crates. It seems to be a journal.") # Lore Item - Journal
        print("Upon opening it, you see the handwriting is frantic and disturbed. The last entry reads: '...the ritual...gone wrong...they are still here...trapped...'") # Lore Hint - Ritual Gone Wrong
        player_inventory.append("basement_journal")
        print("Added basement journal to inventory")
        modify_sanity(-3) # Sanity loss for reading disturbing journal
        basement_storage()
    elif choice == 2:
        basement_hall()

def basement_ritual_chamber_door():
    print("\nYou stand before a heavy wooden door bound with iron. It is firmly shut.")
    print("Strange symbols are etched into the iron bands, radiating a faint chill.")
    random_event("basement_hall") # Use basement hall events as it's adjacent
    choices = [
        "Try to open the door",
        "Examine the symbols",
        "Return to basement hall"
    ]
    if "rusty_key" in player_inventory:
        choices.insert(1, "Use rusty key on door") # Inventory Usage - Rusty Key on Door

    choice = make_choice("What do you do?", choices)

    if choice == 0:
        print("\nYou try the handle, but the door remains stubbornly locked.")
        basement_ritual_chamber_door() # Stay at door
    elif choice == 1:
        print("\nYou examine the symbols. They are unsettling and vaguely familiar, like something from a forbidden text.")
        print("One symbol in particular catches your eye - it resembles a stylized clock face, but twisted and broken.") # Puzzle Hint - Clock Symbol
        basement_ritual_chamber_door() # Stay at door
    elif choice == 2:
        basement_hall()
    elif "rusty_key" in player_inventory and choice == 3: # Inventory Choice - Rusty Key on Door
        print("\nYou insert the rusty key into the lock. It grinds and protests, but finally turns with a loud CLICK.")
        print("The heavy iron-bound door creaks open, revealing a dimly lit chamber beyond...") # Door Unlocked - Ritual Chamber Access
        basement_ritual_chamber() # Proceed to ritual chamber

def basement_ritual_chamber():
    print("\nYou enter a circular chamber. Strange symbols cover the stone floor and walls. An altar stands in the center, stained with dark residue.")
    print("The air crackles with an unnatural energy. This must be the ritual chamber mentioned in the legends...")
    random_event("basement_ritual_chamber")
    choices = [
        "Examine the altar",
        "Investigate the wall symbols",
        "Return to basement hall"
    ]
    if "ritual_dagger" in player_inventory:
        choices.insert(1, "Use ritual dagger on altar") # Inventory Usage - Ritual Dagger on Altar

    choice = make_choice("What will you investigate?", choices)

    if choice == 0:
        print("\nThe altar is cold and radiates a disturbing energy. The dark stains seem to pulse faintly.")
        basement_ritual_chamber() # Stay in chamber
    elif choice == 1:
        print("\nThe wall symbols are complex and unsettling. They seem to writhe in your vision as you stare at them.")
        modify_sanity(-5) # Sanity loss for examining disturbing symbols
        basement_ritual_chamber() # Stay in chamber
    elif choice == 2:
        basement_hall()
    elif "ritual_dagger" in player_inventory and choice == 3: # Inventory Choice - Ritual Dagger on Altar
        print("\nYou raise the ritual dagger and plunge it into the center of the altar.")
        print("As the dagger pierces the altar, a shockwave of energy erupts from the chamber! The symbols glow intensely, then fade.")
        print("A chorus of whispers fills the air, no longer malevolent, but... grateful?") # Potential Ghost Interaction - Ritual Dagger Use
        print("You feel a sense of release, as if a great weight has been lifted from the mansion.")
        modify_sanity(10) # Sanity gain for potentially positive action
        global ghost_helped
        ghost_helped = True # Set ghost_helped flag for ending variation
        # Future: Could trigger a path to a "good" ending here
        basement_ritual_chamber() # Stay in chamber for now

def trapped_ending_mansion_bound():
    print("\nThe mansion's dark energy prevents true escape. Though you leave physically, its horrors haunt you forever.")
    print("TRAPPED ENDING: Mansion Bound")
    play_again()

def play_again():
    choice = input("\nPlay again? (y/n): ").lower()
    if choice == 'y':
        global sanity_level, player_inventory, lore_hints_found, ghost_helped, clock_puzzle_solved
        sanity_level = 100
        player_inventory = []
        lore_hints_found = set()
        ghost_helped = False
        clock_puzzle_solved = False # Reset clock puzzle state
        creepy_intro()
        mansion_gates()
    else:
        print("Thanks for playing!")

def mansion_gates():
    print("\nThe rusted iron gates stand before you, leading to the decaying mansion.")
    print("Carved into the gate is a crest - a stylized 'B' intertwined with thorny vines. You recognize it as the Blackwood family crest.") # Visual Lore Hint - Family Crest
    random_event("mansion_gates")
    choices = ["Enter through main gates", "Search perimeter"]
    if "silver_key" in player_inventory:
        choices.append("Use silver key on gate lock")

    choice = make_choice("Choose your approach:", choices)

    if choice == 0:
        mansion_entrance()
    elif choice == 1:
        print("\nYou decide to search the perimeter of the gates.  You discover a loose stone in the wall nearby.") # Branching Path - Search Perimeter
        print("Behind it is a small, hidden niche. Inside, you find a tarnished silver locket.") # Item Find - Silver Locket (alternative path)
        if "silver_locket" not in player_inventory:
            player_inventory.append("silver_locket")
            print("Added silver locket to inventory (found near gates)")
        else:
            print("The niche is empty, you already found the locket.") # Avoid duplicate locket find
        mansion_gates() # Return to gates after searching perimeter
    elif choice == 2 and "silver_key" in player_inventory:
        print("\nThe silver key fits perfectly in the ancient lock!")
        print("ESCAPE ENDING: Freedom Through Perseverance")
        play_again()

def mansion_entrance():
    print("\nThe massive oak doors creak open to reveal a grand but decaying foyer.")
    print("Above the doorway, barely visible in the gloom, is an inscription in Latin: 'Luctor et Emergo' - 'I struggle and emerge'.") # Visual Lore Hint - Latin Inscription
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