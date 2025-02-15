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
        "study": [
            "The scent of old paper and leather fills the air.",
            "You hear the scratching of quills on parchment, though no one is there.",
            "Dust motes dance in the shafts of light, thick as fog."
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
        if sanity_level < 50: # Sanity-dependent descriptions
            print(f"Your mind, already strained, interprets the sounds as {chosen_event.lower()}... or is it something worse? Your senses are no longer reliable.")
        else:
            print(chosen_event)
        print()
        modify_sanity(-2) # Events slightly reduce sanity


def mansion_gates():
    print("The imposing wrought iron gates, adorned with snarling gargoyles, are now firmly shut and locked.  The only visible path leads towards the mansion's main entrance, a looming maw of shadow and stone. To your left, a barely discernible garden path vanishes into the swirling mist, promising an unknown route.")
    random_event("mansion_gates")
    choices = ["Brave the main path to the mansion entrance.", "Venture into the obscured garden path."]
    if "brass_key" in player_inventory:
        choices.append("Use the brass key on the gates and attempt to escape.") # Option to use key if in inventory
    choice = make_choice("Which path do you choose to explore?", choices)

    if choice == 0:
        mansion_entrance()
    elif choice == 1:
        garden_path()
    elif choice == 2 and "brass_key" in player_inventory: # Escape with brass key
        escape_ending_gates()
    else:
        print("Invalid choice.")
        mansion_gates() # Go back to gates if invalid choice


def escape_ending_gates():
    print("\nYou insert the brass key into the lock of the iron gates. With a satisfying click, the tumblers turn, and the heavy gates swing open, revealing the moonlit path beyond the estate. You step out of Blackwood Mansion, leaving its horrors behind. The brass key, found in the greenhouse, was your salvation.")
    print("Escape Ending: Freedom at the Gates.")
    trapped_ending_mansion_bound() # After basic escape, check for trapped ending condition

def trapped_ending_mansion_bound(): # Placeholder function for trapped ending
    print ("\nIt seems escape is not truly possible. Blackwood Mansion remains, a haunting presence in your memory, forever altering your perception of reality.")
    print ("Trapped Ending: Mansion Bound.")


def mansion_entrance():
    print("You tread the overgrown gravel path towards the mansion's imposing oak doors. They stand slightly ajar, an unsettling invitation into the unknown depths of Blackwood.  The silence is broken only by the mournful sigh of the wind whistling through broken panes in the upper windows.")
    random_event("mansion_entrance")
    choice = make_choice("Do you dare to:", ["Push open the doors and step inside.", "Hesitate, and try to peer through the narrow crack first."])
    if choice == 0:
        hallway()
    else:
        peer_crack()

def peer_crack():
    print("Pressing your face against the cold oak, you peer through the narrow crack. The hallway within is shrouded in gloom, stretching into impenetrable shadows. A massive grandfather clock stands sentinel against the far wall, its pendulum still, its silence heavy with foreboding.  You feel an unsettling presence within, a watchful gaze that seems to penetrate the very wood.")
    random_event("hallway")
    choice = make_choice("Despite the ominous feeling, do you still:", ["Steel your nerves and enter the mansion.", "Retreat and try the garden path once more, seeking another way in."])
    if choice == 0:
        hallway()
    else:
        garden_path()

def garden_path():
    print("You abandon the imposing entrance and venture onto the overgrown garden path. Twisted vines, thick as pythons, writhe across the crumbling stone, and sickly sweet blossoms, pale and luminous in the fading light, exude a cloying, unsettling perfume. The path winds deeper into the swirling mist, obscuring your vision and swallowing sound.")
    random_event("garden")
    choice = make_choice("Do you:", ["Follow the winding path further into the garden's depths.", "Give up on the garden and return to the mansion gates, determined to find another way in."])
    if choice == 0:
        garden_maze()
    else:
        mansion_gates()

def garden_maze():
    print("The garden path abruptly dissolves into a disorienting labyrinth of towering, overgrown hedges and crumbling statues, their stone faces eroded by time and weather into grotesque visages. You are utterly lost, the mansion swallowed by the dense foliage and swirling mist.  A chilling sense of disorientation washes over you, and the very air seems to hum with unseen energy.")
    random_event("garden")
    choice = make_choice("Do you:", ["Force your way through a particularly dense and imposing hedge, hoping it leads somewhere.", "Desperately try to retrace your steps, hoping to find your way back to the garden path entrance."])
    if choice == 0:
        greenhouse_entrance()
    else:
        mansion_gates()

def greenhouse_entrance():
    print("Pushing through the dense hedge, you stumble into a clearing. Before you stands a dilapidated greenhouse, its glass panes cracked and many missing entirely. Twisted metal supports groan under the weight of overgrown vines. A faint, sickly sweet floral scent hangs heavy in the air, even stronger than in the garden.")
    random_event("greenhouse_entrance")
    choice = make_choice("Do you:", ["Enter the dilapidated greenhouse.", "Explore the walled garden surrounding the greenhouse."])
    if choice == 0:
        greenhouse_interior()
    else:
        walled_garden()

def greenhouse_interior():
    print("You cautiously step inside the greenhouse. Shattered glass crunches underfoot.  The air is humid and stifling, thick with the cloying perfume of exotic, overgrown plants. Strange, luminous fungi sprout from damp corners, casting an eerie glow.  Rows of neglected potting tables are covered in decaying leaves and strange, alchemical-looking tools. A sense of unnatural growth and decay permeates the space.")
    random_event("greenhouse_interior")
    if MANSION_PURPOSE == "a secluded research lab focused on spiritual energies" and "greenhouse_notes_hint" not in lore_hints_found and random.random() < 0.7:
        print("On a potting table, amidst the decay, you find a water-damaged notebook. Its pages are filled with frantic scientific notes and unsettling sketches of hybrid plants and creatures.")
        choice = make_choice("Do you attempt to decipher the water-damaged notes?", ["Yes, try to read the notes.", "No, the greenhouse is too unsettling, leave the notes."])
        if choice == 0:
            print("\nYou carefully try to read the notes.  Words like 'hybridization,' 'mutation,' and 'accelerated growth' are legible, alongside disturbing sketches of plants with animalistic features.  The notes hint at dangerous experiments conducted within the greenhouse, focused on manipulating spiritual energies through plant life.") # Lore expanded
            lore_hints_found.add("greenhouse_notes_hint")
    if "brass_key" not in player_inventory and random.random() < 0.6:
        print("Tucked beneath a pile of decaying leaves on one of the potting tables, you discover a small, tarnished brass key.")
        player_inventory.append("brass_key")
        print("You added 'brass key' to your inventory.\n")

    choice = make_choice("What will you investigate within the greenhouse?", ["Examine the strange, luminous fungi growing in the corners.", "Search the neglected potting tables for anything else of interest.", "Leave the greenhouse and explore the walled garden."])
    if choice == 0:
        death_ending_greenhouse_fungi()
    elif choice == 1:
        survival_ending_greenhouse_tools()
    elif choice == 2:
        walled_garden()


def death_ending_greenhouse_fungi():
    print("\nDrawn by their eerie luminescence, you approach the strange fungi. As you lean closer to examine them, a cloud of phosphorescent spores erupts from their caps, directly into your face.")
    print("You inhale deeply, choking as the spores fill your lungs. A burning sensation spreads through your veins, followed by dizziness and nausea. The greenhouse spins around you, the luminous fungi now seeming to pulse with malevolent glee.")
    print("Your vision blurs, and you collapse onto the shattered glass floor, the cloying sweetness of the flowers now a suffocating shroud. The last thing you see is the pulsating glow of the fungi, consuming you in their unnatural light.")
    print("Death Ending: Greenhouse Fungi. Spore inhalation.")
    trapped_ending_mansion_bound() # Check for trapped ending condition after death


def survival_ending_greenhouse_tools():
    print("\You carefully search the neglected potting tables. Amongst the decaying leaves and alchemical tools, you find a sturdy-looking trowel and a pair of thick gardening gloves.")
    if "trowel" not in player_inventory:
        player_inventory.append("trowel")
        print("You added 'trowel' to your inventory.")
    if "gardening_gloves" not in player_inventory:
        player_inventory.append("gardening_gloves")
        print("You added 'gardening gloves' to your inventory.")
    print("Armed with the trowel and gloves, you feel slightly better equipped to face the mansion's mysteries. Perhaps these tools will be useful later.")
    greenhouse_interior() # Return to greenhouse after finding tools

def walled_garden():
    print("You step out into a walled garden adjacent to the greenhouse. High stone walls, covered in moss and ivy, enclose a space of overgrown beauty and subtle decay.  Twisted rose bushes, their thorns unnaturally long, climb the walls, and strange, night-blooming flowers emit a heavy, intoxicating scent.  A crumbling stone fountain stands dry in the center, its basin filled with dead leaves and stagnant water.  A sense of forgotten elegance and encroaching wildness hangs in the air.")
    random_event("garden")
    if "garden_tombstone_hint" not in lore_hints_found and random.random() < 0.6:
        print("Near the back wall, you notice a small, weathered tombstone, almost hidden beneath overgrown ivy. It bears a single name: 'Eleanor Blackwood' and a chillingly short lifespan.")

        riddle = "I whisper truths, unseen, unheard, in shadows deep, my essence stirred. I yearn for peace, a gentle hand, to break the curse upon this land. What am I?" # Riddle changed to hint at "Good" ending
        choices = ["Attempt to solve the riddle on the tombstone.", "Ignore the tombstone and explore the garden further."]
        choice = make_choice(f"The tombstone seems to have a riddle inscribed below the name. It reads: '{riddle}' Do you:", choices)

        if choice == 0:
            player_answer = input("Enter your answer to the riddle: ").lower()
            if solve_riddle(player_answer):
                print("\nCorrect! As you solve the riddle, a faint whisper seems to brush against your ear, '...help me...' You hear a faint grinding sound from behind the tombstone. Examining it closely, you discover a section of the stone is loose, revealing a hidden passage downwards!")
                servants_quarters_garden_passage() # Reveal passage upon riddle solve
                global ghost_helped
                ghost_helped = True # Player helped the ghost by solving riddle
                return  # Skip further walled garden choices as passage is now revealed
            else:
                print("\nIncorrect. The tombstone remains unchanged, but you feel a chill in the air, as if something is displeased.")
                modify_sanity(-5) # Sanity penalty for wrong answer

    # Continue with walled garden exploration choices if riddle not attempted or solved incorrectly
    choice = make_choice("What will you explore in the walled garden?", ["Examine the strange, night-blooming flowers more closely.", "Investigate the crumbling stone fountain in the center.", "Return to the greenhouse interior."])
    if choice == 0:
        death_ending_garden_flowers()
    elif choice == 1:
        servants_quarters_garden_passage()
    elif choice == 2:
        greenhouse_interior()


def solve_riddle(answer):
    correct_answers = ["a ghost", "ghost", "eleanor", "eleanor blackwood"] # Acceptable answers for the new riddle
    return answer in correct_answers


def death_ending_garden_flowers():
    print("\nThe night-blooming flowers, with their pale, luminous petals, exert a strange fascination. You lean in to inhale their intoxicating perfume, drawn by their otherworldly beauty.")
    print("As you breathe deeply, the cloying sweetness intensifies, becoming overwhelming. A wave of dizziness washes over you, and your limbs grow heavy and numb. The garden seems to tilt and sway.")
    print("The flowers' perfume is a potent, insidious poison. You collapse amongst the twisted rose bushes, their thorns tearing at your skin, the intoxicating scent filling your senses as your life fades away. The beautiful garden becomes your final resting place.")
    print("Death Ending: Garden Flowers. Poisoned by night-blooming blossoms.")
    trapped_ending_mansion_bound() # Check for trapped ending condition after death


def servants_quarters_garden_passage():
    print("Behind the tombstone, a narrow, hidden passage leads downwards, concealed and newly revealed. It smells damp and earthy, like a forgotten cellar.")
    random_event("servants_quarters")
    choice = make_choice("Do you:", ["Venture into the hidden passage beneath the tombstone.", "Decide against it and explore the walled garden further."])
    if choice == 0:
        servants_quarters_main_hall()
    else:
        walled_garden()


def servants_quarters_main_hall():
    print("You descend into a narrow, stone-lined passage that opens into a claustrophobic hallway. This must be the servant's quarters. The air is stale and cold, and the walls are damp and stained.  Small, identical wooden doors line both sides of the hallway, likely leading to cramped bedrooms.  A sense of oppressive confinement hangs heavy in the air.")
    random_event("servants_quarters")
    if "servants_quarters_laundry_note_hint" not in lore_hints_found and random.random() < 0.5:
        print("At the end of the hallway, a door hangs ajar, revealing a dimly lit laundry room.  Peeking inside, you see a crumpled note lying on a washbasin.")
        choice = make_choice("Do you enter the laundry room and examine the note?", ["Yes, enter the laundry and read the note.", "No, the servant's quarters feel too oppressive, avoid the laundry."])
        if choice == 0:
            print("\nYou enter the laundry room and pick up the crumpled note. It reads: 'Mistress is unwell... experiments changed her... locked away... cellar door is the only way...' The note is unsigned and soaked with what looks like tears.") # Note updated to fit new lore
            lore_hints_found.add("servants_quarters_laundry_note_hint")
    choice = make_choice("What do you explore in the servant's quarters?", ["Try opening one of the small wooden doors leading to a servant's bedroom.", "Investigate the dimly lit laundry room at the end of the hall.", "Return to the walled garden."])
    if choice == 0:
        servants_quarters_bedroom()
    elif choice == 1:
        servants_quarters_laundry()
    elif choice == 2:
        walled_garden()


def servants_quarters_bedroom():
    print("You cautiously open one of the small wooden doors and step into a servant's bedroom.  The room is spartan and bare, containing only a narrow cot, a rough wooden chest, and a small, cracked mirror on the wall.  Dust motes dance in the slivers of light filtering through cracks in the boarded-up window.  A sense of quiet despair lingers in the air.")
    random_event("servants_quarters")
    choice = make_choice("What do you examine in this desolate bedroom?", ["Open the rough wooden chest at the foot of the cot.", "Look at your reflection in the cracked mirror, despite the unease it inspires.", "Return to the servant's quarters hallway."])
    if choice == 0:
        escape_ending_servants_bedroom_chest()
    elif choice == 1:
        death_ending_servants_bedroom_mirror()
    elif choice == 2:
        servants_quarters_main_hall()

def escape_ending_servants_bedroom_chest(): # Escape Ending 1: Servant's Bedroom Chest
    print("\nYou open the rough wooden chest at the foot of the cot. Inside, amongst some faded linens, you find a hidden compartment containing a tarnished silver locket. It depicts a woman with sad eyes, clutching a strange, luminous flower.")
    if "silver_locket" not in player_inventory:
        player_inventory.append("silver_locket")
        print("You added 'silver locket' to your inventory.")
    print("The locket feels strangely warm to the touch. As you hold it, a faint whisper seems to brush against your ear, '...cellar door...' Could this locket be the key to escaping the mansion, perhaps related to the 'cellar door' mentioned in the laundry note?")
    print("Escape Ending: Silver Locket. Clue found in servant's bedroom chest.")
    servants_quarters_bedroom() # Return to bedroom after finding locket


def death_ending_servants_bedroom_mirror():
    print("\nDespite a sense of unease, you approach the cracked mirror and gaze into your reflection. For a moment, nothing seems amiss. But then, your reflection's eyes widen in silent horror, and its mouth opens in a soundless scream.")
    print("The cracked glass ripples like water, and a shadowy hand reaches out from within, grasping at you. You recoil in terror, stumbling back, but the icy grip tightens, pulling you towards the mirror's surface.")
    print("You are dragged into the mirror's depths, your screams swallowed by the cold, dark glass. Your reflection now stares out, a vacant, haunted look in its eyes, forever trapped within the mirror of the servant's bedroom.")
    print("Death Ending: Servant's Mirror. Trapped within reflection.")
    trapped_ending_mansion_bound() # Check for trapped ending condition after death


def servants_quarters_laundry():
    print("You enter the laundry room.  The air is thick with the damp, musty smell of mildew and stale detergent.  Large copper tubs stand rusting in the center of the room, and rows of empty clotheslines stretch across the ceiling.  A heavy mangle sits against one wall, its iron rollers cold and still.  The room feels heavy with the echoes of endless, thankless labor.")
    random_event("servants_quarters")
    choice = make_choice("What will you search for in the laundry room?", ["Examine the heavy mangle, wondering how it works.", "Search behind the large copper tubs, hoping for a hidden passage.", "Return to the servant's quarters hallway."])
    if choice == 0:
        death_ending_servants_laundry_mangle()
    elif choice == 1:
        scullery_laundry_passage()
    elif choice == 2:
        servants_quarters_main_hall()


def death_ending_servants_laundry_mangle():
    print("\nIntrigued by the heavy mangle, you approach it and begin to examine its cold iron rollers. Curiosity overcoming caution, you reach out and touch the rollers, wondering if they still move.")
    print("Suddenly, with a groaning lurch, the mangle springs to life! The heavy rollers begin to turn, faster and faster, grinding and crushing anything caught within their grasp. You try to pull your hand back, but it's too late.")
    print("Your arm is dragged into the mangle, the crushing force agonizing. You scream in pain and terror as the relentless machine grinds bone and flesh, your lifeblood staining the cold iron. The mangle, a tool of mundane labor, becomes your instrument of death.")
    print("Death Ending: Laundry Mangle. Crushed by the machine.")
    trapped_ending_mansion_bound() # Check for trapped ending condition after death


def scullery_laundry_passage():
    print("Behind one of the large copper tubs, you discover a loose stone in the wall.  Prying it out, you reveal a narrow, low passage leading further into the depths of the servant's quarters.  The air from within smells even damper and colder, like raw earth and stagnant water.")
    random_event("servants_quarters")
    choice = make_choice("Do you:", ["Crawl through the passage, venturing deeper into the unknown.", "Decide against it and return to the laundry room, searching for another exit."])
    if choice == 0:
        scullery()
    elif choice == 1:
        servants_quarters_laundry()


def scullery():
    print("You emerge from the low passage into a cramped, dimly lit scullery.  Stone walls drip with condensation, and the air is thick with the smell of mildew and rotting food scraps.  A large, stone sink dominates one wall, stained and encrusted with grime.  Shelves are lined with chipped and cracked dishes, and overturned buckets and brushes litter the floor.  The atmosphere is even more oppressive and claustrophobic than the rest of the servant's quarters.")
    random_event("scullery")
    if "scullery_symbol_hint" not in lore_hints_found and random.random() < 0.4:
        print("Scratched into the stone wall beside the sink, you notice a recurring symbol – a spiral within a triangle, similar to those you saw in the basement passage, if you explored there.")
        lore_hints_found.add("scullery_symbol_hint")
    choice = make_choice("What do you investigate in this grim scullery?", ["Examine the grimy stone sink more closely.", "Search behind the shelves of cracked dishes, hoping for another passage.", "Return to the laundry room."])
    if choice == 0:
        death_ending_scullery_sink()
    elif choice == 1:
        kitchen_scullery_passage()
    elif choice == 2:
        servants_quarters_laundry()


def death_ending_scullery_sink():
    print("\nYou approach the grimy stone sink, its porcelain stained and cracked.  As you peer into the murky depths, a pair of luminous red eyes suddenly opens beneath the water, staring back at you with malevolent hunger.")
    print("A slimy, skeletal hand erupts from the drain, reaching for you with surprising speed. You recoil in horror, but the grip is too fast, too strong.  The hand drags you down towards the sink, the stench of stagnant water filling your nostrils as you are submerged.")
    print("You struggle and gasp for air, but the unseen creature beneath the sink pulls you deeper into the drain, your screams muffled by the filth and water. The scullery sink, a place of mundane cleansing, becomes your watery grave.")
    print("Death Ending: Scullery Sink. Drowned by the sink's horror.")
    trapped_ending_mansion_bound() # Check for trapped ending condition after death


def kitchen_scullery_passage():
    print("Behind a section of shelves laden with cracked dishes, you discover a partially hidden doorway, almost concealed by shadow and grime.  It seems to lead back towards the main kitchens, offering a potential shortcut.")
    random_event("kitchen")
    choice = make_choice("Do you:", ["Go through the hidden doorway, hoping it leads to a safer area.", "Remain in the scullery and continue searching for other secrets here.", "Return to the laundry room."])
    if choice == 0:
        kitchen_main()
    elif choice == 1:
        scullery()
    elif choice == 2:
        servants_quarters_laundry()


def kitchen_main():
    print("You cautiously step through the hidden doorway and emerge into the mansion's main kitchens.  This is a large, cavernous space, dominated by a massive iron stove and long butcher blocks stained a disturbing dark color.  Copper pots hang from the ceiling, swaying slightly in a nonexistent breeze.  The air is heavy with the metallic tang of old blood and the pervasive smell of decay.  This place feels less oppressive than the scullery, but no less sinister.")
    random_event("kitchen")
    if "kitchen_cleaver_hint" not in lore_hints_found and random.random() < 0.5:
        print("On one of the butcher blocks, you notice a heavy meat cleaver, abandoned as if the cook was interrupted mid-task. Its blade gleams faintly in the dim light, and it feels strangely cold to the touch.")
        lore_hints_found.add("kitchen_cleaver_hint")
    choice = make_choice("What will you investigate in the mansion kitchens?", ["Examine the massive iron stove, wondering if it's still functional.", "Approach the butcher blocks and inspect them more closely.", "Return to the scullery."])
    if choice == 0:
        death_ending_kitchen_stove()
    elif choice == 1:
        basement_stairs_kitchen_passage()
    elif choice == 2:
        scullery()


def death_ending_kitchen_stove():
    print("\nThe massive iron stove, though cold and still, draws your attention. You approach it, noticing intricate carvings around its firebox door depicting grotesque figures writhing in flames.  Curiosity compels you to open the firebox.")
    print("As the heavy iron door creaks open, a blast of searing heat erupts from within, despite the stove being cold to the touch moments before.  Phantom flames lick out, engulfing you in an instant inferno.")
    print("You scream as the spectral flames burn, not with heat, but with an agonizing cold that chills you to the very bone. Your flesh chars and blackens, and your life force is consumed by the unnatural fire. The kitchen stove, meant for warmth and sustenance, becomes your crematorium.")
    print("Death Ending: Kitchen Stove. Burned by phantom flames.")
    trapped_ending_mansion_bound() # Check for trapped ending condition after death


def basement_stairs_kitchen_passage():
    print("You approach the long butcher blocks. They are stained with a dark, disturbing substance that looks chillingly like dried blood.  Inspecting the floor beneath the blocks, you discover a trapdoor, almost hidden beneath a layer of sawdust and grime. It seems to lead down into the mansion's cellars.")
    random_event("kitchen")
    choice = make_choice("Do you:", ["Open the trapdoor and descend into the cellars.", "Leave the trapdoor undisturbed and continue searching the kitchens."])
    if choice == 0:
        basement_stairs()
    elif choice == 1:
        kitchen_main()


def basement_stairs():
    print("You cautiously open the heavy trapdoor, revealing a steep, stone staircase descending into darkness.  The air rising from below is damp and cold, carrying the smell of mildew and earth.  The wooden steps are worn and slick with moisture, groaning ominously under your weight.  A sense of profound unease emanates from the cellar depths.")
    random_event("basement_stairs")
    choice = make_choice("Do you dare to:", ["Carefully descend the treacherous cellar stairs.", "Close the trapdoor and remain in the kitchens, seeking another path."])
    if choice == 0:
        basement_hall()
    elif choice == 1:
        kitchen_main()


def basement_hall():
    print("The cellar stairs deposit you into a long, low-ceilinged hallway.  The air here is heavy and cold, thick with the smell of damp earth and stagnant water.  Rough-hewn stone walls drip with condensation, and puddles collect on the uneven floor.  To your left and right, shadowed archways lead to other cellar chambers, their depths obscured by darkness.  A sense of ancient, subterranean dread permeates the space.")
    random_event("basement_hall")
    if "basement_symbol_hint" not in lore_hints_found and random.random() < 0.6:
        print("Scratched into the wall beside one of the archways, you notice a recurring symbol – a spiral within a triangle. It's unsettlingly familiar, though you can't quite place where you've seen it before.")
        lore_hints_found.add("basement_symbol_hint")
    choice = make_choice("Which shadowed archway will you explore in the cellar?", ["Venture into the archway to your left.", "Explore the archway to your right.", "Return up the cellar stairs to the kitchens."])
    if choice == 0:
        basement_storage()
    elif choice == 1:
        basement_ritual_chamber()
    elif choice == 2:
        kitchen_main()


def basement_storage():
    print("You step through the archway to your left and enter a large cellar storage chamber.  Rows of dusty wine racks line the walls, many bottles broken and their contents long evaporated.  Crates and barrels are stacked haphazardly, their contents unknown.  Cobwebs hang thick as curtains, obscuring the corners of the room.  The air is stale and smells faintly of vinegar and dust.  A sense of forgotten things and slow decay pervades the chamber.")
    random_event("basement_storage")
    if "basement_wine_label_hint" not in lore_hints_found and random.random() < 0.4:
        print("Examining a few of the less-decayed wine bottles, you notice a recurring label: 'Blackwood Estate – Vintage of Sorrow'. The name sends a shiver down your spine.")
        lore_hints_found.add("basement_wine_label_hint")
    choice = make_choice("What will you search for in this dusty storage cellar?", ["Rummage through the stacked crates and barrels, hoping to find something useful.", "Carefully examine the wine racks, looking for an intact bottle or a hidden compartment.", "Return to the cellar hallway."])
    if choice == 0:
        death_ending_basement_crates()
    elif choice == 1:
        escape_ending_basement_wine_bottle()
    elif choice == 2:
        basement_hall()


def death_ending_basement_crates():
    print("\nYou begin rummaging through the stacked crates and barrels, disturbing layers of dust and decay.  Many are filled with nothing but rotted burlap sacks and broken pottery.  As you reach into a particularly large crate, your hand brushes against something cold and metallic.")
    print("Suddenly, the crate begins to tremble violently. A low growl emanates from within, growing louder and more menacing.  The crate bursts open, and a monstrous, shadowy hound leaps out, its eyes burning with malevolent red light.")
    print("The cellar storage chamber becomes a hunting ground. The shadowy hound lunges, its spectral jaws snapping shut around your throat.  You fall to the dusty floor, your lifeblood draining away as the creature feasts upon your fear. The storage cellar becomes your tomb.")
    print("Death Ending: Basement Crates. Hunted by cellar hound.")
    trapped_ending_mansion_bound() # Check for trapped ending condition after death


def escape_ending_basement_wine_bottle(): # Escape Ending 2: Wine Bottle Message
    print("\nYou carefully examine the wine racks, running your fingers along the dusty bottles. Behind a loose section of wood, you discover a hidden compartment. Inside, there is no wine, but a single, intact bottle filled with a rolled-up parchment.")
    print("You uncork the bottle and carefully extract the parchment. It is a message, written in elegant script: '...ritual of binding... broken by light... find the source... purify with the locket...' This message seems to offer a glimmer of hope, a clue to escaping the mansion's curse.") # Message updated to fit "Good" ending and locket
    if "wine_bottle_message" not in player_inventory:
        player_inventory.append("wine_bottle_message")
        print("You added 'wine bottle message' to your inventory.")
    print("Escape Ending: Wine Bottle Message. Clue to cleansing ritual found.")
    basement_storage() # Return to storage cellar after finding message


def basement_ritual_chamber():
    print("You step through the archway to your right and enter a smaller, more ominous cellar chamber. This must be the ritual chamber.  A pentagram is etched into the stone floor, surrounded by strange symbols that seem to writhe in your vision.  Traces of burnt incense linger in the air, and the temperature plummets noticeably.  An altar of rough-hewn stone stands against the far wall, stained with dark, unidentifiable substances.  The air crackles with an unsettling energy, and a palpable sense of dread washes over you.")
    random_event("basement_ritual_chamber")
    if "basement_ritual_book_hint" not in lore_hints_found and random.random() < 0.7:
        print("On the altar, you find a heavy, leather-bound book. Its pages are filled with disturbing diagrams, incantations in a language you don't recognize, and detailed descriptions of dark rituals.  The book radiates a palpable aura of evil.")
        lore_hints_found.add("basement_ritual_book_hint")

    choices = ["Approach the stone altar and examine the ritual book more closely.", "Carefully study the pentagram and strange symbols etched into the floor.", "Retreat to the cellar hallway, this chamber feels too dangerous."]

    if "silver_locket" in player_inventory and ghost_helped: # "Good" ending path: Locket and Ghost Help
        choices.append("Attempt a cleansing ritual at the altar, using the silver locket.") # Add ritual option if locket and ghost_helped

    choice = make_choice("What will you investigate in this disturbing ritual chamber?", choices)

    if choice == 0:
        death_ending_basement_ritual_book()
    elif choice == 1:
        death_ending_basement_pentagram()
    elif choice == 2:
        basement_hall()
    elif choice == 3 and "silver_locket" in player_inventory and ghost_helped: # "Good" Ending Choice
        good_ending_ritual_altar() # "Good" ending ritual


def death_ending_basement_ritual_book():
    print("\nIgnoring the ominous feeling, you approach the stone altar and reach for the leather-bound ritual book. As your fingers brush against its cover, a jolt of icy energy surges through you, throwing you back against the stone wall.")
    print("The book levitates from the altar, its pages flipping open on their own to a disturbing illustration of a shadowy figure surrounded by writhing spirits.  The chamber air grows colder, and the whispers intensify, becoming a chorus of tormented voices.")
    print("The ritual book is a conduit for dark energy. The shadowy figure in the illustration reaches out, its spectral hand passing through the page and grasping your soul. You scream as your life force is ripped away, offered as a sacrifice to the entity bound within the ritual chamber. The altar becomes your deathbed.")
    print("Death Ending: Ritual Book. Soul consumed by dark entity.")
    trapped_ending_mansion_bound() # Check for trapped ending condition after death


def death_ending_basement_pentagram():
    print("\nDespite a prickling sense of dread, you step closer to examine the pentagram etched into the floor. The strange symbols around it seem to writhe and shift as you watch.  As you step directly onto the pentagram, the symbols flare with an eerie red light.")
    print("The chamber floor beneath you gives way, plunging you into a hidden pit filled with sharpened stakes. You fall, impaled upon the cruel points, your screams echoing in the darkness as your life drains away. The ritual chamber's pentagram becomes your trap.")
    print("Death Ending: Pentagram Pit. Impaled in hidden pit.")
    trapped_ending_mansion_bound() # Check for trapped ending condition after death


def good_ending_ritual_altar(): # "Good" Ending: Cleansing Ritual
    print("\nYou approach the stone altar, silver locket in hand. Remembering the wine bottle message – 'purify with the locket' – you hold the locket aloft above the altar.")
    print("As the locket shines with a soft, silver light, the altar symbols begin to glow with a warm, golden radiance. The whispers in the chamber subside, replaced by a sense of peace. The air feels lighter, cleansed of its oppressive energy.")
    print("The sorrowful angel in the chapel's stained-glass window appears in your mind's eye, its weeping eyes now filled with gratitude. '...released... thank you...' the ancient voice whispers, fading away.")
    print("A hidden door in the chamber wall silently opens, revealing a passage leading upwards, bathed in a soft, ethereal light. This must be the way to finally escape Blackwood Mansion, its curse lifted, the restless spirits finally at peace.")
    print("Good Ending: Cleansing Ritual. Spirits appeased, mansion freed.")
    escape_ending_mansion_freed() # Proceed to mansion freed escape ending


def escape_ending_mansion_freed(): # "Good" Escape Ending: Mansion Freed
    print("\nYou step through the hidden door and ascend a previously concealed staircase. It leads you back up into the mansion, emerging in the now-peaceful hallway. The oppressive atmosphere is gone, replaced by a sense of tranquility. Sunlight streams through the windows, illuminating dust motes dancing in the air, no longer ominous, but simply… dust.")
    print("You walk through the mansion, each room now silent and still, but free of malice. Reaching the main entrance, the heavy oak doors swing open willingly, revealing the sunlit grounds beyond.")
    print("You step out of Blackwood Mansion, leaving behind not horror, but peace. The curse is lifted, the spirits are at rest, and you have brought light back to this blighted place. You carry the silver locket, a reminder of the mansion's sorrow and your role in its liberation.")
    print("Escape Ending: Mansion Freed. Blackwood's curse is lifted.")
    true_escape_ending_mansion_freed() # Check for true escape ending condition

def true_escape_ending_mansion_freed(): # True Escape Ending: Mansion Freed and Ghost Helped
    if ghost_helped:
        print("\nBecause you helped Eleanor Blackwood's ghost by solving her riddle, you achieved the 'True Escape' ending. Eleanor's spirit is finally at peace, and Blackwood Mansion is free from its curse, thanks to your compassion and bravery.")
        print("True Escape Ending: Mansion Freed. Ghost helped, curse lifted.")
    else:
        trapped_ending_mansion_bound() # If ghost not helped, revert to standard trapped ending


def attic():
    print("You ascend the creaking grand staircase to the upper floors. You arrive at a shadowy landing. To your left, a narrow, dimly lit hallway stretches into darkness. Straight ahead, a heavy, oak door, identical to the one in the hallway below, stands slightly ajar. To your right, a smaller, less imposing wooden door is also slightly open.")
    random_event("landing")

    choice = make_choice("Which direction will you explore on the upper floors?", ["Venture down the narrow, dimly lit hallway to your left.", "Carefully open the heavy oak door straight ahead.", "Open the smaller wooden door to your right.", "Return down the grand staircase to the main hallway."])

    if choice == 0:
        attic_hallway()
    elif choice == 1:
        master_bedroom()
    elif choice == 2:
        dressing_room()
    elif choice == 3:
        hallway()

def attic_hallway():
    print("You venture down the narrow, dimly lit hallway. The air here is thick with dust and the smell of forgotten things.  Boarded-up windows cast slivers of light, illuminating dust motes dancing in the air like ghostly figures.  To your left and right, small, identical doors line the hallway, likely leading to storage rooms or more servant's quarters.  The oppressive atmosphere of the mansion seems to intensify on this upper floor.")
    random_event("attic")
    choice = make_choice("Which area of the attic hallway will you explore?", ["Try opening one of the small doors to your left.", "Try opening one of the small doors to your right.", "Return to the landing."])

    if choice == 0:
        attic_storage_left()
    elif choice == 1:
        attic_storage_right()
    elif choice == 2:
        landing()

def attic_storage_left(): # Example of left storage room
    print("You cautiously open one of the small doors to your left and step into a dusty attic storage room.  The room is crammed floor-to-ceiling with forgotten objects draped in white sheets - furniture, portraits, and other unknown shapes.  The air is thick with dust and the scent of mothballs.  Sunlight filtering through cracks in the boarded windows creates eerie patterns of light and shadow.")
    random_event("attic_storage")
    choice = make_choice("What will you investigate in this cluttered storage room?", ["Carefully pull back a white sheet, curious to see what's hidden beneath.", "Search amongst the shadowy corners of the room, hoping to find something of interest.", "Return to the attic hallway."])

    if choice == 0:
        death_ending_attic_sheet()
    elif choice == 1:
        escape_ending_attic_corner()
    elif choice == 2:
        attic_hallway()

def attic_storage_right(): # Example of right storage room - can mirror left or have different content
    print("You cautiously open one of the small doors to your right and step into another dusty attic storage room, similar to the one across the hall. This room, however, seems to contain more boxes and trunks rather than furniture.  The air is just as still and dusty, and the silence is heavy.")
    random_event("attic_storage")
    choice = make_choice("What will you investigate in this storage room?", ["Open one of the old boxes or trunks, curious about their contents.", "Examine the boarded-up windows more closely, hoping to find a way to open them.", "Return to the attic hallway."])

    if choice == 0:
        death_ending_attic_trunk()
    elif choice == 1:
        death_ending_attic_window()
    elif choice == 2:
        attic_hallway()

def death_ending_attic_sheet():
    print("\nDriven by curiosity, you reach out and pull back a white sheet covering a large object.  Beneath, you reveal a full-length mirror, its glass cloudy with age. As you uncover it, the mirror flashes with blinding white light.")
    print("When your vision clears, your reflection stares back at you, but its eyes are black voids, and a grotesque grin stretches across its face. It lunges out of the mirror, a shadowy doppelganger, and pins you to the floor.")
    print("The attic storage room becomes a prison. Your doppelganger, a creature of living shadow, slowly absorbs your life force, replacing you in the real world while you fade into nothingness within the mirror's depths. The sheet-covered mirror concealed not just an object, but a deadly trap.")
    print("Death Ending: Attic Mirror Sheet. Doppelganger consumes you.")
    trapped_ending_mansion_bound() # Check for trapped ending condition after death

def escape_ending_attic_corner(): # Escape Ending 3: Attic Corner Note
    print("\nYou cautiously search amongst the shadowy corners of the storage room. Behind a stack of dusty portraits, you find a loose floorboard.  Prying it open with your fingers, you discover a small, hidden compartment.")
    print("Inside, there's no treasure, but a small, folded note. You carefully unfold it. It reads: '...attic ritual room... cleanse with light... destroy the focus...' This note, though cryptic, seems to offer another clue, perhaps related to a 'Good' ending and a way to destroy the mansion's curse.") # Note updated to hint at "Good" ending
    if "attic_note_hint" not in lore_hints_found:
        lore_hints_found.add("attic_note_hint")
        print("You found a clue: 'attic ritual room, cleanse with light, destroy the focus'.\n")

    attic_storage_left() # Return to storage room after finding note

def death_ending_attic_trunk():
    print("\nYou decide to open one of the old trunks. The lock is rusted, but with some effort, you manage to force it open.  Inside, nestled amongst yellowed lace and moth-eaten velvet, you find a collection of antique dolls. Their porcelain faces stare up at you with unsettlingly lifelike eyes.")
    print("As you reach into the trunk, one of the dolls suddenly sits up, its porcelain head snapping into focus. Its eyes glow red, and it lets out a high-pitched, piercing shriek that fills the attic storage room.")
    print("The other dolls in the trunk animate, their porcelain limbs jerking and twitching. They swarm you, their tiny, but sharp porcelain hands and teeth tearing at your flesh. The attic storage room becomes a dollhouse of horrors, and you, their living plaything.")
    print("Death Ending: Attic Dolls. Toyed to death by possessed dolls.")
    trapped_ending_mansion_bound() # Check for trapped ending condition after death

def death_ending_attic_window():
    print("\nYou approach the boarded-up windows, hoping to find a way to pry them open and let in some light. The wood is old and rotten, but firmly nailed shut.  As you examine the boards, you notice strange symbols carved into the wood, glowing faintly in the dim light.")
    print("Ignoring a growing sense of unease, you touch one of the glowing symbols. The moment your fingers make contact, the boards splinter outwards with explosive force, showering you with shards of wood and glass. A blinding light erupts from outside the window, not sunlight, but something far more intense and malevolent.")
    print("The unnatural light burns your eyes and skin, searing your very soul. You scream in agony as your body is consumed by the otherworldly radiance. The attic window, a potential escape, becomes a gateway to annihilation.")
    print("Death Ending: Attic Window. Annihilated by unnatural light.")
    trapped_ending_mansion_bound() # Check for trapped ending condition after death


def master_bedroom():
    print("You carefully open the heavy oak door and step into what must have been the master bedroom.  Despite the decay, hints of past grandeur remain.  A massive four-poster bed dominates the room, draped in tattered velvet curtains.  A vanity table with a cracked mirror stands against one wall, and a cold fireplace is choked with dust and ashes.  A faint floral perfume lingers in the air, a ghostly echo of elegance.")
    random_event("master_bedroom")
    choice = make_choice("What will you investigate in the master bedroom?", ["Approach the four-poster bed and examine it more closely.", "Inspect the vanity table and its cracked mirror.", "Explore the doorway leading to an adjoining room.", "Return to the landing."])

    if choice == 0:
        death_ending_master_bed()
    elif choice == 1:
        bathroom_master_bedroom_passage()
    elif choice == 2:
        bathroom()
    elif choice == 3:
        landing()

def death_ending_master_bed():
    print("\nThe four-poster bed, with its heavy velvet curtains, seems to radiate an aura of oppressive stillness. You approach it cautiously and reach out to touch the tattered fabric.")
    print("As your fingers brush the velvet, the curtains suddenly billow inwards, as if caught in a sudden gust of wind, though there is no breeze.  Shadowy figures emerge from within the bed curtains, their forms indistinct and menacing.")
    print("The master bedroom becomes a stage for a nightmare. The shadowy figures, manifestations of the mansion's dark past, descend upon you, their touch like icy claws. You are dragged down onto the bed, suffocated by the velvet curtains and consumed by the darkness within. The grand bed becomes your deathbed.")
    print("Death Ending: Master Bed. Suffocated by shadowy figures.")
    trapped_ending_mansion_bound() # Check for trapped ending condition after death

def bathroom_master_bedroom_passage():
    print("You turn your attention to the vanity table. Its cracked mirror reflects a distorted image of the room, playing tricks on your eyes.  Examining the vanity more closely, you notice a small, porcelain jewelry box, slightly ajar.")
    choice = make_choice("Do you:", ["Open the porcelain jewelry box and see what's inside.", "Ignore the jewelry box and investigate the doorway to the adjoining room.", "Return to the master bedroom."])

    if choice == 0:
        rusty_key_bathroom_jewelry_box()
    elif choice == 1:
        bathroom()
    elif choice == 2:
        master_bedroom()

def rusty_key_bathroom_jewelry_box(): # Item Found: Rusty Key
    print("\nYou open the porcelain jewelry box. Inside, nestled on faded velvet, you find a rusty iron key. It looks old and worn, but potentially useful.")
    if "rusty_key" not in player_inventory:
        player_inventory.append("rusty_key")
        print("You added 'rusty key' to your inventory.")
    print("The rusty key might unlock something else in the mansion. You add it to your inventory.")
    master_bedroom() # Return to bedroom after finding key


def bathroom():
    print("You step through the doorway into an adjoining room - a master bathroom.  Cracked tiles line the walls, and a stained porcelain tub sits on clawed feet.  The air is damp and cold, smelling of mildew and stagnant water.  A leaky faucet drips incessantly into the tub, the sound echoing in the oppressive silence.  The room feels neglected and decaying, a place of forgotten luxury.")
    random_event("bathroom")
    choice = make_choice("What will you investigate in the master bathroom?", ["Examine the stained porcelain tub and the dripping faucet.", "Inspect the cracked tiles on the walls more closely.", "Return to the master bedroom."])

    if choice == 0:
        death_ending_bathroom_tub()
    elif choice == 1:
        dressing_room_bathroom_passage()
    elif choice == 2:
        master_bedroom()

def death_ending_bathroom_tub():
    print("\nYou approach the stained porcelain tub, the incessant dripping of the faucet echoing in the silence. As you peer into the murky water collected at the bottom, the dripping stops abruptly.")
    print("The water in the tub begins to churn and bubble, and a skeletal hand bursts forth from the depths, grasping at you with surprising speed.  You recoil in horror, but the hand is too fast, too strong.")
    print("The bathroom becomes a watery trap. The skeletal hand drags you down towards the tub, the stench of stagnant water filling your nostrils as you are submerged. You struggle and gasp, but the unseen creature beneath the water pulls you deeper, your screams muffled by the filth and water. The porcelain tub becomes your grave.")
    print("Death Ending: Bathroom Tub. Drowned by tub's horror.")
    trapped_ending_mansion_bound() # Check for trapped ending condition after death

def dressing_room_bathroom_passage():
    print("You turn your attention to the cracked tiles lining the bathroom walls.  Examining them closely, you notice that one section of tiles near the floor seems slightly loose.  Prying at them, you discover a hidden, narrow doorway concealed behind the tiles, leading to another room.")
    random_event("bathroom")
    choice = make_choice("Do you:", ["Venture through the hidden doorway behind the tiles.", "Ignore the hidden doorway and return to the master bedroom."])

    if choice == 0:
        dressing_room()
    elif choice == 1:
        master_bedroom()

def dressing_room():
    print("You step through the hidden doorway and emerge into a dressing room.  Mirrors line one wall, reflecting distorted images of the room and playing tricks on your eyes.  Empty衣架 sway gently in a nonexistent breeze, and the air is thick with the scent of mothballs and old fabric.  A sense of faded vanity and forgotten elegance hangs in the air.")
    random_event("dressing_room")
    choice = make_choice("What will you investigate in the dressing room?", ["Examine your reflection in the many mirrors, despite the unsettling feeling.", "Search through the empty衣架 and drawers, hoping to find something useful.", "Return to the bathroom."])

    if choice == 0:
        death_ending_dressing_mirror()
    elif choice == 1:
        escape_ending_dressing_drawers()
    elif choice == 2:
        bathroom()

def death_ending_dressing_mirror():
    print("\nDespite the unease, you approach the wall of mirrors and gaze at your reflection.  For a moment, nothing seems amiss. But then, your reflection's eyes widen in silent horror, and it frantically mouths the word 'behind you'.")
    print("You whirl around, but it's too late.  A shadowy figure lunges from behind, its touch like ice. The dressing room mirrors become portals, trapping you between reflections, as the shadowy figure claims your life. Your reflection now stares out from the mirror, a vacant, haunted look in its eyes, forever trapped within the dressing room.")
    print("Death Ending: Dressing Room Mirrors. Trapped between reflections.")
    trapped_ending_mansion_bound() # Check for trapped ending condition after death

def escape_ending_dressing_drawers(): # Escape Ending 4: Dressing Room Drawers
    print("\nYou begin searching through the empty衣架 and drawers.  Most are filled with nothing but dust and the lingering scent of old perfume.  In the bottom drawer of a vanity, however, you find a small, velvet pouch. Inside, there is no jewelry, but a single, tarnished silver locket.")
    if "silver_locket" not in player_inventory:
        player_inventory.append("silver_locket")
        print("You added 'silver locket' to your inventory.")
    print("The locket depicts a sorrowful angel with weeping eyes. It feels strangely cold to the touch, and yet, radiates a faint, ethereal light. Could this be significant, perhaps related to the mansion's curse or a way to break it?")
    print("Escape Ending: Silver Locket. Found in dressing room drawers.")
    dressing_room() # Return to dressing room after finding locket


# Start the game
creepy_intro()
mansion_gates()