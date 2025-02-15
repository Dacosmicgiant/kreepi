import random

# Lore variables - set the backstory elements here
BLACKWOOD_TRAGEDY = "a family murder-suicide"
MANSION_PURPOSE = "a secluded research lab"
HORROR_SOURCE = "a malevolent entity"

lore_hints_found = set()
player_inventory = []
sanity_level = 100  # Initialize sanity level

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
    if MANSION_PURPOSE == "a secluded research lab" and "greenhouse_notes_hint" not in lore_hints_found and random.random() < 0.7:
        print("On a potting table, amidst the decay, you find a water-damaged notebook. Its pages are filled with frantic scientific notes and unsettling sketches of hybrid plants and creatures.")
        choice = make_choice("Do you attempt to decipher the water-damaged notes?", ["Yes, try to read the notes.", "No, the greenhouse is too unsettling, leave the notes."])
        if choice == 0:
            print("\nYou carefully try to read the notes.  Words like 'hybridization,' 'mutation,' and 'accelerated growth' are legible, alongside disturbing sketches of plants with animalistic features.  The notes hint at dangerous experiments conducted within the greenhouse.")
            lore_hints_found.add("greenhouse_notes_hint")
    choice = make_choice("What will you investigate within the greenhouse?", ["Examine the strange, luminous fungi growing in the corners.", "Search the neglected potting tables for anything of interest."])
    if choice == 0:
        death_ending_greenhouse_fungi()
    else:
        survival_ending_greenhouse_tools()

def walled_garden():
    print("You step out into a walled garden adjacent to the greenhouse. High stone walls, covered in moss and ivy, enclose a space of overgrown beauty and subtle decay.  Twisted rose bushes, their thorns unnaturally long, climb the walls, and strange, night-blooming flowers emit a heavy, intoxicating scent.  A crumbling stone fountain stands dry in the center, its basin filled with dead leaves and stagnant water.  A sense of forgotten elegance and encroaching wildness hangs in the air.")
    random_event("garden")
    if "garden_tombstone_hint" not in lore_hints_found and random.random() < 0.6:
        print("Near the back wall, you notice a small, weathered tombstone, almost hidden beneath overgrown ivy. It bears a single name: 'Eleanor Blackwood' and a chillingly short lifespan.")

        riddle = "I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I?"
        choices = ["Attempt to solve the riddle on the tombstone.", "Ignore the tombstone and explore the garden further."]
        choice = make_choice(f"The tombstone seems to have a riddle inscribed below the name. It reads: '{riddle}' Do you:", choices)

        if choice == 0:
            player_answer = input("Enter your answer to the riddle: ").lower()
            if solve_riddle(player_answer):
                print("\nCorrect! As you solve the riddle, you hear a faint grinding sound from behind the tombstone. Examining it closely, you discover a section of the stone is loose, revealing a hidden passage downwards!")
                servants_quarters_garden_passage() # Reveal passage upon riddle solve
                return # Skip further walled garden choices as passage is now revealed
            else:
                print("\nIncorrect. The tombstone remains unchanged, but you feel a chill in the air, as if something is displeased.")
                modify_sanity(-5) # Sanity penalty for wrong answer

    # Continue with walled garden exploration choices if riddle not attempted or solved incorrectly
    choice = make_choice("What will you explore in the walled garden?", ["Examine the strange, night-blooming flowers more closely.", "Investigate the crumbling stone fountain in the center."])
    if choice == 0:
        death_ending_garden_flowers()
    else:
        servants_quarters_garden_passage()


def solve_riddle(answer):
    correct_answers = ["a map", "map"] # Acceptable answers for the riddle
    return answer in correct_answers


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
            print("\nYou enter the laundry room and pick up the crumpled note. It reads: 'Mistress is unwell... experiments changed her... locked away... cellar door is the only way...' The note is unsigned and soaked with what looks like tears.")
            lore_hints_found.add("servants_quarters_laundry_note_hint")
    choice = make_choice("What do you explore in the servant's quarters?", ["Try opening one of the small wooden doors leading to a servant's bedroom.", "Investigate the dimly lit laundry room at the end of the hall."])
    if choice == 0:
        servants_quarters_bedroom()
    else:
        servants_quarters_laundry()


def servants_quarters_bedroom():
    print("You cautiously open one of the small wooden doors and step into a servant's bedroom.  The room is spartan and bare, containing only a narrow cot, a rough wooden chest, and a small, cracked mirror on the wall.  Dust motes dance in the slivers of light filtering through cracks in the boarded-up window.  A sense of quiet despair lingers in the air.")
    random_event("servants_quarters")
    choice = make_choice("What do you examine in this desolate bedroom?", ["Open the rough wooden chest at the foot of the cot.", "Look at your reflection in the cracked mirror, despite the unease it inspires."])
    if choice == 0:
        escape_ending_servants_bedroom_chest()
    else:
        death_ending_servants_bedroom_mirror()

def servants_quarters_laundry():
    print("You enter the laundry room.  The air is thick with the damp, musty smell of mildew and stale detergent.  Large copper tubs stand rusting in the center of the room, and rows of empty clotheslines stretch across the ceiling.  A heavy mangle sits against one wall, its iron rollers cold and still.  The room feels heavy with the echoes of endless, thankless labor.")
    random_event("servants_quarters")
    choice = make_choice("What will you search for in the laundry room?", ["Examine the heavy mangle, wondering how it works.", "Search behind the large copper tubs, hoping for a hidden passage."])
    if choice == 0:
        death_ending_servants_laundry_mangle()
    else:
        scullery_laundry_passage()


def scullery_laundry_passage():
    print("Behind one of the large copper tubs, you discover a loose stone in the wall.  Prying it out, you reveal a narrow, low passage leading further into the depths of the servant's quarters.  The air from within smells even damper and colder, like raw earth and stagnant water.")
    random_event("servants_quarters")
    choice = make_choice("Do you:", ["Crawl through the passage, venturing deeper into the unknown.", "Decide against it and return to the laundry room, searching for another exit."])
    if choice == 0:
        scullery()
    else:
        servants_quarters_laundry()


def scullery():
    print("You emerge from the low passage into a cramped, dimly lit scullery.  Stone walls drip with condensation, and the air is thick with the smell of mildew and rotting food scraps.  A large, stone sink dominates one wall, stained and encrusted with grime.  Shelves are lined with chipped and cracked dishes, and overturned buckets and brushes litter the floor.  The atmosphere is even more oppressive and claustrophobic than the rest of the servant's quarters.")
    random_event("scullery")
    if "scullery_symbol_hint" not in lore_hints_found and random.random() < 0.4:
        print("Scratched into the stone wall beside the sink, you notice a recurring symbol – a spiral within a triangle, similar to those you saw in the basement passage, if you explored there.")
        lore_hints_found.add("scullery_symbol_hint")
    choice = make_choice("What do you investigate in this grim scullery?", ["Examine the grimy stone sink more closely.", "Search behind the shelves of cracked dishes, hoping for another passage."])
    if choice == 0:
        death_ending_scullery_sink()
    else:
        kitchen_scullery_passage()


def kitchen_scullery_passage():
    print("Behind a section of shelves laden with cracked dishes, you discover a partially hidden doorway, almost concealed by shadow and grime.  It seems to lead back towards the main kitchens, offering a potential shortcut.")
    random_event("kitchen")
    choice = make_choice("Do you:", ["Go through the hidden doorway, hoping it leads to a safer area.", "Remain in the scullery and continue searching for other secrets here."])
    if choice == 0:
        kitchen_main()
    else:
        scullery()


def hallway():
    print("You find yourself in the main hallway. The air hangs heavy, thick with the scent of dust, decay, and something else... something faintly metallic and unsettling. To your left, a grand staircase, its once-ornate wood now splintered and groaning, ascends into the oppressive darkness above. Straight ahead, a shadowed archway promises deeper mysteries within the house. To your right, a heavy oak door, intricately carved with scenes of hunting hounds and stags, stands slightly ajar, emitting a sliver of light.")
    random_event("hallway")
    if "hallway_portrait_hint" not in lore_hints_found and random.random() < 0.6:
        print("A large, imposing portrait dominates the wall at the end of the hallway. It depicts a stern-faced man in formal attire, presumably a Blackwood ancestor. His eyes seem to follow you as you move.")
        lore_hints_found.add("hallway_portrait_hint")
    choice = make_choice("Which direction will you take to explore Blackwood Mansion?", ["Ascend the creaking staircase to the upper floors.", "Venture through the shadowed archway deeper into the mansion.", "Carefully open the oak door to your right."])
    if choice == 0:
        attic()
    elif choice == 1:
        basement_hall()
    else:
        dining_room()

def dining_room():
    print("You cautiously push open the heavy oak door and enter what must have once been the grand dining room.  A long, mahogany table dominates the center of the room, draped in a moth-eaten, white linen cloth.  Dust-laden silverware and half-rotted place settings remain, as if the occupants simply vanished mid-meal.  A cold draft emanates from a massive, stone fireplace at the far end of the room, now choked with debris and cobwebs. The air is heavy with the lingering aroma of stale food and something faintly… gamey.")
    random_event("dining_room")
    if "dining_room_note_hint" not in lore_hints_found and random.random() < 0.5:
        print("On the table, amidst the decaying food, you spot a slightly less decayed piece of paper. It seems to be a hastily scribbled note.")
        choice = make_choice("Do you try to read the note?", ["Yes, carefully examine the note.", "No, the stench is too much, leave it be."])
        if choice == 0:
            print("\nYou carefully pick up the note. It reads, in faded ink: '...cannot contain it... experiments... gone too far... beware the cellar...' The rest is illegible.")
            lore_hints_found.add("dining_room_note_hint")
    choice = make_choice("What will you investigate in this unsettling dining room?", ["Examine the long, laden dining table and its decaying feast.", "Approach the cold, cavernous fireplace and peer within."])
    if choice == 0:
        kitchen()
    else:
        hidden_passage_dining_room()

def hidden_passage_dining_room():
    print("You approach the massive fireplace, its stones cold to the touch.  As you peer into the soot-blackened opening, you notice a section of the back wall seems slightly dislodged.  Upon closer inspection, you discover a cleverly concealed mechanism – a hidden lever disguised as a decorative ironwork flourish.")
    random_event("dining_room")
    choices = ["Pull the hidden lever, curious to see what it reveals.", "Leave the fireplace undisturbed and return to the dining table to investigate further."]
    if "rusty_key" in player_inventory:
        choices.append("Use the rusty key on the lever mechanism.") # Option to use rusty key

    choice = make_choice("Do you dare to:", choices)

    if choice == 0:
        chapel_hidden_passage()
    elif choice == 1:
        dining_room()
    elif choice == 2 and "rusty_key" in player_inventory: # Use rusty key on lever
        print("\nYou insert the rusty key into a small, almost invisible keyhole near the lever. With a click, the mechanism engages!")
        chapel_hidden_passage() # Key unlocks passage directly
    else:
        print("Invalid choice.")
        hidden_passage_dining_room() # Go back to hidden passage choices

def chapel_hidden_passage():
    print("With a rusty groan, the lever yields. A section of the stone wall beside the fireplace grinds inwards, revealing a narrow, descending passage shrouded in absolute darkness. A gust of icy air rushes out, carrying the faint scent of incense and something else… something ancient and earthy.")
    random_event("chapel")
    choice = make_choice("Will you brave the unknown depths of this hidden passage?", ["Descend into the darkness, following the hidden passage.", "Decide against it and return to the dining room, seeking another path."])
    if choice == 0:
        chapel()
    else:
        dining_room()


def chapel():
    print("You emerge into a small, hidden chapel.  Faint light filters through a stained-glass window depicting a sorrowful angel with weeping eyes.  The air is heavy with the scent of incense and damp stone.  A single, overturned pew lies on the cold stone floor, and an altar at the far end is draped in black cloth.  A sense of forgotten devotion and lingering despair permeates the space.")
    random_event("chapel")
    if "chapel_diary_hint" not in lore_hints_found and random.random() < 0.7:
        print("On the altar, partially hidden beneath the black cloth, you find a small, leather-bound diary.")
        choice = make_choice("Do you examine the diary?", ["Yes, open and read the diary.", "No, leave it undisturbed, the chapel feels too unsettling."])
        if choice == 0:
            print("\nYou open the diary. The pages are brittle and filled with frantic handwriting. You read: '...rituals... for power... family demanded it... something answered... wrong... so wrong... now it haunts us all...' The last entry is abruptly cut off.")
            lore_hints_found.add("chapel_diary_hint")
    choice = make_choice("What do you do in this hidden chapel?", ["Examine the overturned pew, is anything hidden beneath it?", "Approach the altar and inspect it more closely."])
    if choice == 0:
        death_ending_chapel_pew()
    else:
        survival_ending_chapel_altar()


def kitchen():
    print("You turn your attention to the long dining table, its surface laden with the remnants of a long-abandoned feast.  Rotting food clings to tarnished silver platters, attracting swarms of buzzing flies.  The stench is almost unbearable.  Amidst the decay, you notice a small, service door at the far end of the room, slightly ajar, likely leading to the kitchens.")
    random_event("dining_room")
    choice = make_choice("Do you:", ["Brave the stench and carefully examine the decaying feast on the table for any clues.", "Head towards the service door and investigate the kitchens, hoping for a less nauseating environment."])
    if choice == 0:
        death_ending_dining_table()
    else:
        kitchen_main()

def kitchen_main():
    print("You push open the service door and step into the mansion's kitchens.  The air is marginally less foul here, though still heavy with the smell of stale grease and damp stone.  Massive iron stoves stand cold and silent, their surfaces rusted with disuse.  Shelves are lined with cracked and empty jars, and overturned pots and pans litter the stone floor.  A sense of cold, utilitarian neglect permeates the space.")
    random_event("kitchen")
    choice = make_choice("What will you search for in the desolate kitchens?", ["Rummage through the overturned pots and pans, hoping to find something useful.", "Investigate a large, walk-in pantry at the back of the kitchen, shrouded in shadow.", "Notice a sturdy wooden door, possibly leading to the study."])
    if choice == 0:
        escape_ending_kitchen_pots()
    elif choice == 1:
        pantry()
    else:
        study_kitchen_door()


def study_kitchen_door():
    print("You approach the sturdy wooden door in the kitchen. It's surprisingly solid and well-maintained compared to the rest of the mansion.  A faint light seeps from beneath the door, and you hear the muffled sound of rustling paper.")
    random_event("kitchen")
    choice = make_choice("Do you:", ["Open the wooden door and enter the study.", "Decide against it and search the main kitchen area further."])
    if choice == 0:
        study()
    else:
        kitchen_main()


def study():
    print("You open the sturdy wooden door and step into the study.  In stark contrast to the rest of the mansion, this room is relatively well-preserved, though still dusty and dimly lit by a single oil lamp flickering on a large desk.  Bookshelves line the walls, filled with volumes on arcane subjects, scientific equipment sits on tables, and charts and diagrams cover the walls.  The air is thick with the smell of old paper, ink, and a faint, metallic tang, reminiscent of the hallway.")
    random_event("study")
    if MANSION_PURPOSE == "a secluded research lab" and "study_research_notes_hint" not in lore_hints_found and random.random() < 0.8:
        print("On the large desk, illuminated by the oil lamp, you find a stack of research notes. They detail experiments in 'bio-energetics,' 'spiritual resonance,' and 'entity containment.' The notes become increasingly frantic and disturbing towards the end, hinting at a catastrophic breakthrough.")
        lore_hints_found.add("study_research_notes_hint")
    choice = make_choice("What will you examine in the study?", ["Browse the bookshelves filled with arcane volumes.", "Investigate the scientific equipment scattered around the room.", "Search behind the bookshelves, looking for a hidden passage."])
    if choice == 0:
        death_ending_study_bookshelves()
    elif choice == 1:
        survival_ending_study_equipment()
    else:
        hidden_study()


def hidden_study():
    print("You push open the hidden staircase and emerge into a hidden, smaller study, even more secluded than the first.  This room is in disarray, papers scattered everywhere, equipment overturned, and a sense of frantic abandonment.  A single, bare lightbulb flickers erratically from the ceiling, casting harsh, distorted shadows.")
    random_event("study")
    if MANSION_PURPOSE == "a secluded research lab" and "hidden_study_ritual_text_hint" not in lore_hints_found and random.random() < 0.7:
        print("On a overturned table, you find a heavy, leather-bound book open to a page filled with unsettling diagrams and ritualistic text in a language you don't recognize.  Symbols similar to those in the basement and scullery are prominent.")
        lore_hints_found.add("hidden_study_ritual_text_hint")
    choice = make_choice("What will you investigate in this hidden study?", ["Attempt to decipher the ritualistic text in the book.", "Search through the scattered papers on the floor, hoping for a clue."])
    if choice == 0:
        ritual_room_study_passage()
    else:
        escape_ending_hidden_study_papers()

def ritual_room_study_passage():
    print("As you attempt to decipher the strange text, you notice a faint tremor in the floor beneath you.  The flickering lightbulb swings wildly, and a low hum fills the air, growing steadily louder.  Suddenly, a section of the floor beneath the overturned table gives way, revealing a dark, descending staircase.  The humming intensifies, seeming to emanate from below.")
    random_event("ritual_room")
    choice = make_choice("Do you dare to:", ["Descend the newly revealed staircase, following the humming sound.", "Quickly retreat from the hidden study, sensing great danger."])
    if choice == 0:
        ritual_room()
    else:
        study()


def ritual_room():
    print("You descend into a large, subterranean chamber – the ritual room. The air is thick with the smell of ozone, incense, and something ancient and cold, like the breath of a tomb.  Strange symbols are etched into the stone walls, glowing faintly with an inner light.  In the center of the room, a raised stone platform serves as an altar, upon which strange artifacts are arranged – bones, crystals, and metallic instruments humming with energy.  The humming sound from above is deafening here, vibrating through your very bones.  A palpable sense of dark power and barely contained energy fills the chamber.")
    random_event("ritual_room")
    if HORROR_SOURCE == "malevolent entity":
        print("You feel an overwhelming presence here, a sense of ancient malice focused on this chamber. The air crackles with unseen energy, and the shadows seem to writhe and pulse with a life of their own.")
    elif HORROR_SOURCE == "restless ghosts":
        print("Spectral figures flicker around the edges of the chamber, their mournful whispers echoing in the humming silence.  They seem drawn to this place, trapped by the rituals performed here.")
    elif HORROR_SOURCE == "psychological manifestation":
        print("The symbols on the walls seem to shift and writhe before your eyes, and the artifacts on the altar pulse with a disturbing, organic rhythm.  Your own fears and anxieties seem to coalesce and amplify in this oppressive space.")

    choice = make_choice("What will you do in this terrifying ritual room?", ["Approach the altar and examine the strange artifacts.", "Search the walls for another exit, desperate to escape this place."])
    if choice == 0:
        final_ending_ritual_altar()
    else:
        escape_ending_ritual_chamber_exit()


def pantry():
    print("You cautiously approach the walk-in pantry, its heavy wooden door hanging slightly open, casting a rectangle of impenetrable darkness into the already dim kitchen.  The air emanating from within is noticeably colder, carrying a faint, earthy smell, like damp cellars and something… else. Something vaguely… animalistic.")
    random_event("pantry")
    choice = make_choice("Do you dare to:", ["Venture into the shadowed depths of the pantry.", "Decide against it and return to the main hallway, seeking a different path."])
    if choice == 0:
        death_ending_pantry()
    else:
        hallway()


def basement_hall():
    print("You step through the shadowed archway from the main hallway and find yourself in a narrow basement hallway. The air is frigid and damp, the stone walls slick with moisture.  The incessant dripping of water echoes loudly in the oppressive silence.  The hallway stretches into darkness, promising only deeper descent.")
    random_event("basement_hall")
    choice = make_choice("Do you:", ["Follow the hallway further into the oppressive darkness.", "Investigate a side passage, barely illuminated by a single, guttering candle stuck in a wall sconce."])
    if choice == 0:
        basement_chamber()
    else:
        basement_side_passage()

def basement_side_passage():
    print("You cautiously enter the side passage. The flickering candlelight throws grotesque, dancing shadows on the rough-hewn walls, revealing unsettling symbols etched into the stone – spirals, triangles, and strange, unidentifiable glyphs.  The air grows noticeably colder, and you feel an unnerving prickling sensation on your skin, as if unseen eyes are watching you.")
    random_event("basement_hall")
    choice = make_choice("Do you:", ["Brave the unsettling atmosphere and examine the strange symbols more closely.", "Quickly retreat back to the relative safety of the basement hallway, unnerved by the passage."])
    if choice == 0:
        death_ending_basement_symbols()
    else:
        basement_hall()

def basement_chamber():
    print("The basement hallway abruptly opens into a vast, circular chamber.  A chilling draft swirls around you, carrying the scent of damp earth and stagnant water. In the chamber's center, a dark, still pool of water reflects the faint light filtering down from above, like a black mirror into another world. An unsettling silence reigns, broken only by the echoing drips and the faint, rhythmic thumping sound emanating from the pool’s depths.")
    random_event("basement_chamber")
    choice = make_choice("Do you dare to:", ["Approach the dark pool and peer into its mysterious depths, despite the ominous feeling it evokes.", "Cautiously search the perimeter of the chamber for another exit, avoiding the unsettling pool."])
    if choice == 0:
        death_ending_pool()
    else:
        escape_ending_basement()

def attic():
    print("You ascend the hidden staircase and emerge into the dusty, oppressive attic.  Moonlight, weak and spectral, filters through cracks in the boarded-up windows, barely illuminating the vast, cluttered space. Cobwebs hang thick as shrouds, draping forgotten furniture and casting eerie shadows. The air is stifling, thick with dust and the cloying sweetness of decay. The silence is broken only by the frantic scurrying of unseen creatures in the rafters above.")
    random_event("attic")
    if "attic_child_drawing_hint" not in lore_hints_found and random.random() < 0.4:
        print("Tucked away beneath a dust-covered rocking horse, you find a child's drawing. It depicts stick figures huddled around a dark shape with red eyes, and the word 'Monster' scrawled beneath in shaky handwriting.")
        lore_hints_found.add("attic_child_drawing_hint")
    choice = make_choice("What will you investigate in this unsettling attic?", ["Cautiously approach a large, shadowed corner, shrouded in deeper darkness and filled with an unnerving stillness.", "Desperately search for a way out through the boarded windows, hoping for a glimpse of the outside world."])
    if choice == 0:
        death_ending_attic_corner()
    else:
        escape_ending_attic_window()

def survival_ending_library_book():
    print("\nDriven by intuition, you meticulously examine the towering bookshelves.  Behind a particularly worn, leather-bound volume titled 'Bestiary of Shadowed Creatures,' you discover a hidden compartment, barely visible in the dim light. Inside, nestled on faded velvet, you find a tarnished silver key, intricately engraved with the Blackwood family crest, and a brittle, yellowed map.")
    print("The map, though fragile with age, clearly depicts a secret passage concealed behind the library fireplace. You carefully replace the book, then move to the fireplace. Using the silver key on a nearly invisible lock hidden within the stonework, a section of the wall swings inwards, revealing the passage. You slip through, descending into cool, fresh air.  You emerge outside, blinking in the moonlight, leaving Blackwood Mansion and its haunting secrets behind, forever etched in your memory. You have survived.")
    print("Survival Ending: The Scholar's Escape.")

def survival_ending_greenhouse_tools():
    print("\nIgnoring the unsettling fungi, you focus your search on the neglected potting tables. Amongst rusted tools and dried-up seed packets, you discover a sturdy pair of gardening shears with surprisingly sharp blades.  And more importantly, a small, tarnished BRASS KEY tucked within the handle of the shears.")
    print("Remembering the locked gates, you realize this key might be your escape. You clutch the key tightly and decide to head back towards the mansion entrance, hoping to find a way to the gates.")
    player_inventory.append("brass_key")
    print("Armed with a potential escape tool, you feel a surge of hope. You decide to return to the mansion entrance and see if the key will work on the gates.")
    mansion_gates()

def survival_ending_chapel_altar():
    print("\nYou approach the altar and carefully examine the black cloth. As you lift a corner, you discover a small, silver locket hidden beneath.  It's cold to the touch and engraved with the Blackwood family crest.")
    print("As you touch the locket, a faint warmth spreads through you, and the oppressive atmosphere of the chapel seems to lighten slightly. You feel a sense of… protection? Perhaps this locket holds some significance. You decide to keep it.")
    player_inventory.append("silver_locket")
    print("You feel a renewed sense of purpose.  Perhaps this locket can aid you in your escape. You decide to return to the hallway and explore other areas of the mansion.")
    hallway()

def survival_ending_study_equipment():
    print("\nYou decide to investigate the strange scientific equipment scattered around the study.  On a table cluttered with beakers and wires, you find a complex-looking device with a series of dials and a small, glowing crystal at its center.  Intrigued, you cautiously examine it.")
    print("As you touch the crystal, the device hums to life, emitting a beam of focused energy.  The beam strikes the wall behind the desk, and with a crackling sound, a section of the wall dissolves, revealing a hidden doorway leading outwards, into the night!")
    print("You quickly step through the doorway, emerging into the cool night air, leaving the study and Blackwood Mansion behind. You have escaped using the mansion's own strange technology!")
    print("Survival Ending: Scientific Escape.")

def escape_ending_basement():
    print("\nDriven by a desperate hope, you meticulously search the cold, damp chamber walls, your fingers tracing the rough-hewn stone. Behind a loose, water-stained tapestry depicting a faded hunting scene, you discover a crumbling section of wall, almost hidden in the shadows.  You pull the tapestry aside to reveal a narrow, damp tunnel, barely wide enough to squeeze through.")
    print("Ignoring the claustrophobic dread, you squeeze through the tunnel, crawling blindly for what feels like an eternity through earth and stone.  Finally, you emerge into the cool night air, collapsing onto soft earth, far from the mansion's oppressive presence. You have escaped the basement's suffocating depths!")
    print("Escape Ending: The Tunnel Run.")

def escape_ending_attic_window():
    print("\nDriven by a desperate need for escape, you cautiously approach the boarded windows, your heart pounding with a mixture of hope and fear.  Examining the aged wood, you discover one section near the corner that is noticeably weaker, the boards thinner and more brittle than the rest. Summoning a surge of adrenaline, you kick out with all your force, splintering the wood and creating a narrow, jagged escape route.")
    print("Ignoring the sharp edges, you climb out onto the steeply pitched roof, the wind whipping at your face.  Carefully, painstakingly, you make your way down the treacherous slope, clinging to crumbling gargoyles and moss-covered shingles.  You slide and scramble down the last section, dropping to the overgrown grounds below, leaving Blackwood Mansion silhouetted against the cold moon.  You have escaped the attic's chilling clutches!")
    print("Escape Ending: The Rooftop Descent.")

def escape_ending_kitchen_pots():
    print("\Driven by a hunch, you begin rummaging through the overturned pots and pans scattered across the kitchen floor.  Beneath a heavy, cast-iron cauldron, you discover a loose flagstone.  Prying it up with trembling hands, you reveal a narrow, earthen passage leading downwards.  A faint breath of fresh air wafts upwards, carrying the scent of soil and freedom.")
    print("Without hesitation, you squeeze into the passage and slide down a short, earthen slope.  You emerge into the cool night air, blinking against the sudden brightness of the moon, a safe distance from Blackwood Mansion. You have escaped through the kitchens!")
    print("Escape Ending: Kitchen Passage.")

def escape_ending_hidden_study_papers():
    print("\nYou begin frantically searching through the scattered papers on the floor of the hidden study.  Amidst the chaos, you find a hastily drawn map of the mansion, seemingly sketched in charcoal.  It marks a hidden exit in the walled garden, near the fountain!")
    print("Remembering the walled garden from your earlier exploration, you realize this might be your best chance. You decide to retrace your steps back through the library and garden, eventually reaching the walled garden and the crumbling fountain.  There, just as the map indicated, you find a section of the wall that crumbles away easily, revealing an opening to the outside world. You escape Blackwood Mansion, guided by a hidden map!")
    print("Escape Ending: The Cartographer's Clue.")

def escape_ending_ritual_chamber_exit():
    print("\nOverwhelmed by the oppressive atmosphere of the ritual chamber, you desperately search the walls for any sign of escape.  Behind a tapestry depicting grotesque figures performing a dark ritual, you discover a narrow crack in the stone.  Working frantically, you widen the crack, revealing a rough-hewn tunnel leading upwards.")
    print("You scramble through the tunnel, climbing upwards through damp earth and rough stone.  Finally, you emerge into the night air, breathless and shaken, but free from the ritual chamber and the horrors of Blackwood Mansion. You have escaped the heart of darkness!")
    print("Escape Ending: Chamber Escape.")

def escape_ending_servants_bedroom_chest():
    print("\nYou open the rough wooden chest at the foot of the cot. Inside, amongst moth-eaten blankets and worn clothing, you find a small, rusty KEY and a tarnished SILVER WHISTLE.")
    print("You take both items, unsure of their purpose, but feeling they might be important.")
    player_inventory.extend(["rusty_key", "silver_whistle"])
    print("With new items in hand, you feel a glimmer of hope. You decide to explore the rest of the servant's quarters, searching for where these items might be useful.")
    servants_quarters_main_hall()


def final_ending_ritual_altar():
    print("\Summoning a strange mix of fear and morbid curiosity, you approach the altar in the center of the ritual chamber.  The artifacts arranged upon it hum with an unsettling energy, and the symbols on the walls seem to pulse in response as you draw closer.")
    if "silver_locket" in player_inventory:
        print("\nAs you reach the altar, you instinctively hold out the silver locket you found in the chapel.  The locket begins to glow with a soft, white light, and the humming in the chamber intensifies, but now with a different quality – a resonance, rather than a threat.")
        print("The symbols on the walls flare brightly, and a wave of energy washes over you, emanating from the altar and the locket in your hand.  The oppressive atmosphere of the chamber begins to dissipate, replaced by a sense of… peace?")
        print("The malevolent presence you felt throughout the mansion seems to recede, the shadows lose their depth, and the air becomes lighter.  You feel a profound sense of release, as if the mansion itself is sighing in relief.")
        print("True Ending: The Cleansing.")
    else:
        print("\nAs you reach the altar, the humming intensifies to a deafening roar. The artifacts begin to vibrate violently, and the symbols on the walls blaze with malevolent energy.  The air crackles and distorts around you, and the sense of dread becomes overwhelming.")
        print("Suddenly, the chamber floor beneath you cracks open, and you plunge into an abyss of pure darkness.  Screaming, you fall into the unknown depths, the ritual chamber above swallowing your cries.  You have succumbed to the power of the ritual, becoming another sacrifice to the darkness that Blackwood Mansion conceals.")
        print("Death Ending: Ritual Sacrifice.")


def death_ending_basement_symbols():
    print("\nCompelled by a morbid curiosity, you lean closer to the wall and begin tracing the strange symbols etched into the stone. As your fingers brush against the cold glyphs, the guttering candle flame flares violently, casting grotesque shadows that writhe and coalesce into monstrous shapes, then abruptly extinguishes, plunging the passage into absolute, suffocating darkness.  A chilling voice, devoid of warmth or life, whispers directly into your ear, 'Knowledge… has its price.'")
    print("Something unseen, something cold and impossibly strong, grasps you from the impenetrable darkness.  A silent scream tears through your throat, unheard in the echoing silence of the mansion.  Your reckless curiosity has become your agonizing doom. ")
    print("Death Ending: Symbol's Curse.")

def death_ending_pool():
    print("\nDespite the overwhelming sense of dread, a morbid fascination draws you to the edge of the dark pool.  You lean closer, peering into its still, black depths, trying to discern what lies beneath the surface. Suddenly, with shocking speed, a frigid, skeletal hand erupts from the water, its grip like iron, seizing your wrist and dragging you inexorably downwards into the icy blackness.")
    print("You claw at the slick stone edges, desperate for purchase, but the unseen force is implacable.  The dark water closes over your head, swallowing your panicked cries and extinguishing the last vestiges of light.  The pool, a gateway to something ancient and malevolent, claims another soul for its silent depths.")
    print("Death Ending: Drowned in Darkness.")

def death_ending_attic_corner():
    print("\nIgnoring the prickling unease, you cautiously approach the shadowed corner, your heart hammering a frantic tattoo against your ribs. As you reach out a trembling hand to touch the cold wall, something lunges from the impenetrable darkness with terrifying speed and ferocity – a grotesque, shadowy figure, vaguely humanoid yet horribly distorted, its eyes burning with malevolent red light.")
    print("It shrieks, a sound that tears at your sanity, a discordant symphony of pain and rage, and its icy claws, sharp as shards of glass, tear into your flesh. You stumble back, a strangled cry escaping your lips, as your lifeblood drains away onto the dusty floorboards of the attic.  The shadow, a guardian of forgotten horrors, claims you as its own.")
    print("Death Ending: Shadow's Embrace.")

def death_ending_dining_table():
    print("\nIgnoring the overwhelming stench, you steel yourself and approach the decaying feast laid out on the long dining table.  As you reach out to examine a particularly grotesque dish – a half-eaten bird, its feathers matted with congealed blood – the room plunges into absolute darkness.  A chorus of guttural whispers erupts around you, too indistinct to understand, yet filled with palpable malice.  From the shadows, skeletal hands reach out, grasping and tearing.")
    print("You scream, a sound swallowed by the darkness and the chorus of whispers, as the unseen horrors of the dining room descend upon you, tearing you apart amidst the decaying remnants of a cursed feast. Your morbid curiosity has become your final, agonizing meal.")
    print("Death Ending: Feast of the Damned.")

def death_ending_pantry():
    print("\Taking a deep, shuddering breath, you steel yourself and step into the shadowed pantry.  The heavy wooden door creaks shut behind you with unnatural force, plunging you into near-total darkness.  The earthy, animalistic smell intensifies, becoming overpowering, and you hear a low growl echoing from the depths of the small space.  Suddenly, something brushes against your leg – something cold, wet, and scaled.")
    print("A monstrous shape, unseen in the darkness, lunges from the shadows, its hot, fetid breath washing over you.  Razor-sharp teeth sink into your flesh, and a searing pain explodes through your body.  Your screams are muffled by the darkness and the monstrous presence that devours you in the suffocating confines of the pantry.  Your ill-advised bravery has led you to a gruesome end.")
    print("Death Ending: Pantry Predator.")

def death_ending_greenhouse_fungi():
    print("\nYou cautiously approach the strange, luminous fungi growing in the corners of the greenhouse.  Mesmerized by their eerie glow, you reach out to touch one.  As your fingers brush against the soft, pulsating cap, a jolt of icy energy surges through your arm, paralyzing you.  The fungi begin to emit a cloud of phosphorescent spores, filling the air around you.")
    print("You gasp for breath as the spores fill your lungs, a burning cold spreading through your body.  Your vision blurs, and you collapse onto the shattered glass floor, your life force consumed by the unnatural fungi of the greenhouse. Your curiosity proves fatal in this garden of horrors.")
    print("Death Ending: Fungal Consumption.")

def death_ending_garden_flowers():
    print("\nYou cautiously approach the night-blooming flowers, drawn in by their intoxicating scent and strange beauty.  As you lean closer to inhale their perfume, the blossoms suddenly unfurl, revealing rows of needle-sharp thorns and pulsating, fleshy interiors.  The cloying scent intensifies, becoming sickeningly sweet, and you feel a wave of dizziness wash over you.")
    print("Thorns lash out, piercing your skin, and a viscous, pollen-like substance coats your face.  You stumble back, choking and gasping, as the flowers' toxins enter your bloodstream.  Your vision fades, the beautiful garden transforming into a swirling vortex of color and pain.  The garden's beauty becomes your deadly allure.")
    print("Death Ending: Floral Poison.")

def death_ending_servants_bedroom_mirror():
    print("\nDespite the unease, you approach the cracked mirror and gaze into your reflection.  The glass is cloudy and distorted, and your own image seems strangely… wrong, subtly altered and unsettling.  As you stare deeper, the reflection begins to shift and writhe, your features twisting into a grotesque mockery of yourself.")
    print("A cold dread washes over you as the reflection's eyes fixate on yours, burning with malevolent intent.  A spectral hand reaches out from the mirror's surface, passing through the glass and grasping your throat.  You gasp for air, your reflection now a monstrous, grinning visage, as your life is stolen by the haunted mirror of the servant's bedroom. Your vanity becomes your demise.")
    print("Death Ending: Mirror's Grasp.")

def death_ending_servants_laundry_mangle():
    print("\nYou cautiously approach the heavy mangle, its iron rollers radiating a chilling cold.  Intrigued by its mechanism, you reach out to touch the rollers.  Suddenly, with a deafening CLANG, the mangle springs to life, its heavy rollers snapping shut with terrifying force.")
    print("Your hand is caught in the unforgiving iron grip, bones shattering instantly.  You scream in agony, struggling to free yourself, but the mangle continues to grind and crush, pulling you further into its deadly embrace.  The laundry room's silent machinery becomes your instrument of torture and death.  Your curiosity becomes your mutilation.")
    print("Death Ending: Mangle's Crush.")

def death_ending_scullery_sink():
    print("\nYou lean over the grimy stone sink, peering into its depths, hoping to find a drain or hidden opening.  As you gaze into the stagnant water, the surface ripples unnaturally, and a pair of luminous, reptilian eyes open beneath the murky depths, staring back at you with cold, predatory hunger.")
    print("A serpentine form erupts from the sink with shocking speed, its jaws lined with rows of needle-sharp teeth snapping at your face.  You recoil in horror, but not fast enough.  The creature’s fangs sink into your flesh, injecting a potent venom.  You collapse onto the damp stone floor, your vision blurring, as the scullery sink reveals its hidden, monstrous inhabitant. Your investigation becomes your consumption.")
    print("Death Ending: Sink Serpent.")

def death_ending_study_bookshelves():
    print("\nYou begin Browse the towering bookshelves, running your fingers along the spines of ancient tomes.  As you reach for a particularly intriguing volume bound in human skin, the bookshelves around you begin to groan and shift.  The room suddenly plunges into near darkness, and the bookshelves begin to close in, walls of heavy wood and crushing knowledge.")
    print("You realize, with dawning horror, that you are trapped.  The bookshelves are moving, slowly but inexorably, squeezing the air from your lungs.  You struggle against the implacable wooden walls, but it's no use.  The library itself becomes your tomb, crushing you beneath the weight of forbidden lore. Your thirst for knowledge becomes your suffocation.")
    print("Death Ending: Bookcase Tomb.")


def play_game():
    creepy_intro()
    mansion_gates()

if __name__ == "__main__":
    play_game()