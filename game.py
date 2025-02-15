import random

def creepy_intro():
    print("The rusted gates of Blackwood Mansion swing shut with a mournful clang, sealing you within the estate's suffocating embrace.  A chilling wind whispers through the ancient oaks, carrying the scent of damp earth and decay.")
    print("The mansion looms before you, a gothic monolith against the bruised purple of the twilight sky. Its darkened windows stare like vacant eyes, promising no solace, only secrets.")
    print("You came seeking answers, lured by local legends of a family tragedy and whispers of restless spirits. Now, trapped within its crumbling walls, the thrill of investigation has curdled into icy dread.")
    print("A palpable sense of unease settles upon you. The very stones of Blackwood Mansion seem to breathe with a dark sentience. Escape is paramount, but the mansion itself seems unwilling to release you.")
    print("Your heart pounds a frantic rhythm against your ribs. Will you unravel the mysteries of Blackwood Mansion and escape its grasp? Or will you become another forgotten soul lost within its shadowed halls?")
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
        "A sudden draft extinguishes your flickering candle, plunging you into momentary darkness.",
        "You hear a faint melody, like a ghostly piano playing a mournful tune from a distant room.",
        "The air grows heavy with the cloying sweetness of decaying lilies, though no flowers are in sight.",
        "Shadows stretch and distort on the walls, taking on vaguely human shapes before dissolving back into darkness.",
        "A floorboard creaks directly behind you, despite you being completely still.",
        "You catch a whiff of woodsmoke, though there's no fireplace lit and no sign of fire.",
        "A whisper, like dry leaves skittering across stone, seems to brush against your ear, too indistinct to decipher.",
        "The temperature plummets drastically, and you see your breath cloud in the frigid air.",
        "A portrait's eyes seem to follow you with unnerving intensity, a silent judgment in their painted gaze.",
        "You hear the distinct sound of children's laughter, abruptly cut short, echoing from the upper floors.",
        "Dust motes swirl around you in an unnatural vortex, forming fleeting, ghostly shapes.",
        "The faint scent of ozone fills the air, like the aftermath of a violent storm, though the sky outside is clear."
    ]
    if random.random() < 0.5: # Increased event frequency
        print(random.choice(events))
        print()

def mansion_gates():
    print("The imposing wrought iron gates, adorned with snarling gargoyles, are now firmly shut and locked.  The only visible path leads towards the mansion's main entrance, a looming maw of shadow and stone. To your left, a barely discernible garden path vanishes into the swirling mist, promising an unknown route.")
    random_event()
    choice = make_choice("Which path do you choose to explore?", ["Brave the main path to the mansion entrance.", "Venture into the obscured garden path."])
    if choice == 0:
        mansion_entrance()
    else:
        garden_path()

def mansion_entrance():
    print("You tread the overgrown gravel path towards the mansion's imposing oak doors. They stand slightly ajar, an unsettling invitation into the unknown depths of Blackwood.  The silence is broken only by the mournful sigh of the wind whistling through broken panes in the upper windows.")
    random_event()
    choice = make_choice("Do you dare to:", ["Push open the doors and step inside.", "Hesitate, and try to peer through the narrow crack first."])
    if choice == 0:
        hallway()
    else:
        peer_crack()

def peer_crack():
    print("Pressing your face against the cold oak, you peer through the narrow crack. The hallway within is shrouded in gloom, stretching into impenetrable shadows. A massive grandfather clock stands sentinel against the far wall, its pendulum still, its silence heavy with foreboding.  You feel an unsettling presence within, a watchful gaze that seems to penetrate the very wood.")
    random_event()
    choice = make_choice("Despite the ominous feeling, do you still:", ["Steel your nerves and enter the mansion.", "Retreat and try the garden path once more, seeking another way in."])
    if choice == 0:
        hallway()
    else:
        garden_path() # Go back to garden path choice

def garden_path():
    print("You abandon the imposing entrance and venture onto the overgrown garden path. Twisted vines, thick as pythons, writhe across the crumbling stone, and sickly sweet blossoms, pale and luminous in the fading light, exude a cloying, unsettling perfume. The path winds deeper into the swirling mist, obscuring your vision and swallowing sound.")
    random_event()
    choice = make_choice("Do you:", ["Follow the winding path further into the garden's depths.", "Give up on the garden and return to the mansion gates, determined to find another way in."])
    if choice == 0:
        garden_maze()
    else:
        mansion_gates() # Go back to mansion gates choice

def garden_maze():
    print("The garden path abruptly dissolves into a disorienting labyrinth of towering, overgrown hedges and crumbling statues, their stone faces eroded by time and weather into grotesque visages. You are utterly lost, the mansion swallowed by the dense foliage and swirling mist.  A chilling sense of disorientation washes over you, and the very air seems to hum with unseen energy.")
    random_event()
    choice = make_choice("Do you:", ["Force your way through a particularly dense and imposing hedge, hoping it leads somewhere.", "Desperately try to retrace your steps, hoping to find your way back to the garden path entrance."])
    if choice == 0:
        library() # New location from garden
    else:
        mansion_gates() # Go back to mansion gates choice

def hallway():
    print("You find yourself in the main hallway. The air hangs heavy, thick with the scent of dust, decay, and something else... something faintly metallic and unsettling. To your left, a grand staircase, its once-ornate wood now splintered and groaning, ascends into the oppressive darkness above. Straight ahead, a shadowed archway promises deeper mysteries within the house. To your right, a heavy oak door, intricately carved with scenes of hunting hounds and stags, stands slightly ajar, emitting a sliver of light.")
    random_event()
    choice = make_choice("Which direction will you take to explore Blackwood Mansion?", ["Ascend the creaking staircase to the upper floors.", "Venture through the shadowed archway deeper into the mansion.", "Carefully open the oak door to your right."])
    if choice == 0:
        attic()
    elif choice == 1:
        basement_hall() # Changed to basement hallway first
    else:
        dining_room() # New location - dining room

def dining_room():
    print("You cautiously push open the heavy oak door and step into what must have once been the grand dining room.  A long, mahogany table dominates the center of the room, draped in a moth-eaten, white linen cloth.  Dust-laden silverware and half-rotted place settings remain, as if the occupants simply vanished mid-meal.  A cold draft emanates from a massive, stone fireplace at the far end of the room, now choked with debris and cobwebs. The air is heavy with the lingering aroma of stale food and something faintly… gamey.")
    random_event()
    choice = make_choice("What will you investigate in this unsettling dining room?", ["Examine the long, laden dining table and its decaying feast.", "Approach the cold, cavernous fireplace and peer within."])
    if choice == 0:
        kitchen() # New location - kitchen from dining table
    else:
        hidden_passage_dining_room() # New location - hidden passage

def hidden_passage_dining_room():
    print("You approach the massive fireplace, its stones cold to the touch.  As you peer into the soot-blackened opening, you notice a section of the back wall seems slightly dislodged.  Upon closer inspection, you discover a cleverly concealed mechanism – a hidden lever disguised as a decorative ironwork flourish.")
    random_event()
    choice = make_choice("Do you dare to:", ["Pull the hidden lever, curious to see what it reveals.", "Leave the fireplace undisturbed and return to the dining table to investigate further."])
    if choice == 0:
        chapel_hidden_passage() # New location - chapel hidden passage
    else:
        dining_room() # Back to dining room choices

def chapel_hidden_passage():
    print("With a rusty groan, the lever yields. A section of the stone wall beside the fireplace grinds inwards, revealing a narrow, descending passage shrouded in absolute darkness. A gust of icy air rushes out, carrying the faint scent of incense and something else… something ancient and earthy.")
    random_event()
    choice = make_choice("Will you brave the unknown depths of this hidden passage?", ["Descend into the darkness, following the hidden passage.", "Decide against it and return to the dining room, seeking another path."])
    if choice == 0:
        chapel() # New location - chapel
    else:
        dining_room() # Back to dining room choices


def kitchen():
    print("You turn your attention to the long dining table, its surface laden with the remnants of a long-abandoned feast.  Rotting food clings to tarnished silver platters, attracting swarms of buzzing flies.  The stench is almost unbearable.  Amidst the decay, you notice a small, service door at the far end of the room, slightly ajar, likely leading to the kitchens.")
    random_event()
    choice = make_choice("Do you:", ["Brave the stench and carefully examine the decaying feast on the table for any clues.", "Head towards the service door and investigate the kitchens, hoping for a less nauseating environment."])
    if choice == 0:
        death_ending_dining_table() # Risky choice - table related death
    else:
        kitchen_main() # New location - kitchen main

def kitchen_main():
    print("You push open the service door and step into the mansion's kitchens.  The air is marginally less foul here, though still heavy with the smell of stale grease and damp stone.  Massive iron stoves stand cold and silent, their surfaces rusted with disuse.  Shelves are lined with cracked and empty jars, and overturned pots and pans litter the stone floor.  A sense of cold, utilitarian neglect permeates the space.")
    random_event()
    choice = make_choice("What will you search for in the desolate kitchens?", ["Rummage through the overturned pots and pans, hoping to find something useful.", "Investigate a large, walk-in pantry at the back of the kitchen, shrouded in shadow."])
    if choice == 0:
        escape_ending_kitchen_pots() # Lucky choice - escape from kitchen
    else:
        pantry() # New location - pantry


def pantry():
    print("You cautiously approach the walk-in pantry, its heavy wooden door hanging slightly open, casting a rectangle of impenetrable darkness into the already dim kitchen.  The air emanating from within is noticeably colder, carrying a faint, earthy smell, like damp cellars and something… else. Something vaguely… animalistic.")
    random_event()
    choice = make_choice("Do you dare to:", ["Venture into the shadowed depths of the pantry.", "Decide against it and return to the main hallway, seeking a different path."])
    if choice == 0:
        death_ending_pantry() # Risky choice - pantry death
    else:
        hallway() # Back to hallway choices


def basement_hall():
    print("You step through the shadowed archway from the main hallway and find yourself in a narrow basement hallway. The air is frigid and damp, the stone walls slick with moisture.  The incessant dripping of water echoes loudly in the oppressive silence.  The hallway stretches into darkness, promising only deeper descent.")
    random_event()
    choice = make_choice("Do you:", ["Follow the hallway further into the oppressive darkness.", "Investigate a side passage, barely illuminated by a single, guttering candle stuck in a wall sconce."])
    if choice == 0:
        basement_chamber() # Deeper basement
    else:
        basement_side_passage() # Side passage

def basement_side_passage():
    print("You cautiously enter the side passage. The flickering candlelight throws grotesque, dancing shadows on the rough-hewn walls, revealing unsettling symbols etched into the stone – spirals, triangles, and strange, unidentifiable glyphs.  The air grows noticeably colder, and you feel an unnerving prickling sensation on your skin, as if unseen eyes are watching you.")
    random_event()
    choice = make_choice("Do you:", ["Brave the unsettling atmosphere and examine the strange symbols more closely.", "Quickly retreat back to the relative safety of the basement hallway, unnerved by the passage."])
    if choice == 0:
        death_ending_basement_symbols() # Risky choice - symbol related death
    else:
        basement_hall() # Back to basement hallway

def basement_chamber():
    print("The basement hallway abruptly opens into a vast, circular chamber.  A chilling draft swirls around you, carrying the scent of damp earth and stagnant water. In the chamber's center, a dark, still pool of water reflects the faint light filtering down from above, like a black mirror into another world. An unsettling silence reigns, broken only by the echoing drips and the faint, rhythmic thumping sound emanating from the pool’s depths.")
    random_event()
    choice = make_choice("Do you dare to:", ["Approach the dark pool and peer into its mysterious depths, despite the ominous feeling it evokes.", "Cautiously search the perimeter of the chamber for another exit, avoiding the unsettling pool."])
    if choice == 0:
        death_ending_pool() # Very risky choice - pool related death
    else:
        escape_ending_basement() # Chance of escape in basement

def library():
    print("You push open the heavy oak door and step into the grand library. Towering bookshelves, crafted from dark, polished wood, stretch to the vaulted ceiling, crammed with countless ancient, leather-bound volumes.  Dust motes dance in the faint shafts of light filtering through stained-glass windows depicting somber, biblical scenes.  The air is still and silent, heavy with the scent of aged paper and forgotten knowledge. A large, ornate mahogany desk sits imposingly in the center of the room, its surface covered in scattered papers and strange artifacts.")
    random_event()
    choice = make_choice("What will you focus your search on in this vast library?", ["Begin Browse the towering bookshelves, hoping to find a hidden book or a vital clue.", "Approach the ornate desk in the center of the room and examine its scattered contents."])
    if choice == 0:
        survival_ending_library_book() # Lucky choice - book leads to survival
    else:
        attic_from_library() # Misdirection - desk leads to attic

def attic_from_library():
    print("You decide to investigate the ornate desk. Amongst the scattered papers and strange instruments, you find a hidden mechanism – a small, almost invisible button concealed beneath a loose inkwell.  Driven by curiosity, you press it.")
    print("With a soft click, a section of the library wall slides silently open, revealing a narrow, hidden staircase spiraling upwards.  The air from above smells even dustier and more stagnant than the library itself.")
    random_event()
    choice = make_choice("Will you:", ["Ascend the hidden staircase, venturing into the unknown upper reaches of the mansion.", "Decide against the hidden passage and return to the bookshelves, continuing your search in the library."])
    if choice == 0:
        attic() # New location - attic from library
    else:
        library() # Back to library choices


def attic():
    print("You ascend the hidden staircase and emerge into the dusty, oppressive attic.  Moonlight, weak and spectral, filters through cracks in the boarded-up windows, barely illuminating the vast, cluttered space. Cobwebs hang thick as shrouds, draping forgotten furniture and casting eerie shadows. The air is stifling, thick with dust and the cloying sweetness of decay. The silence is broken only by the frantic scurrying of unseen creatures in the rafters above.")
    random_event()
    choice = make_choice("What will you investigate in this unsettling attic?", ["Cautiously approach a large, shadowed corner, shrouded in deeper darkness and filled with an unnerving stillness.", "Desperately search for a way out through the boarded windows, hoping for a glimpse of the outside world."])
    if choice == 0:
        death_ending_attic_corner() # Risky choice - corner leads to death
    else:
        escape_ending_attic_window() # Chance of escape from attic

def survival_ending_library_book():
    print("\nDriven by intuition, you meticulously examine the towering bookshelves.  Behind a particularly worn, leather-bound volume titled 'Bestiary of Shadowed Creatures,' you discover a hidden compartment, barely visible in the dim light. Inside, nestled on faded velvet, you find a tarnished silver key, intricately engraved with the Blackwood family crest, and a brittle, yellowed map.")
    print("The map, though fragile with age, clearly depicts a secret passage concealed behind the library fireplace. You carefully replace the book, then move to the fireplace. Using the silver key on a nearly invisible lock hidden within the stonework, a section of the wall swings inwards, revealing the passage. You slip through, descending into cool, fresh air.  You emerge outside, blinking in the moonlight, leaving Blackwood Mansion and its haunting secrets behind, forever etched in your memory. You have survived.")
    print("Survival Ending: The Scholar's Escape.")

def escape_ending_basement():
    print("\nDriven by a desperate hope, you meticulously search the cold, damp chamber walls, your fingers tracing the rough-hewn stone. Behind a loose, water-stained tapestry depicting a faded hunting scene, you discover a crumbling section of wall, almost hidden in the shadows.  You pull the tapestry aside to reveal a narrow, damp tunnel, barely wide enough to squeeze through.")
    print("Ignoring the claustrophobic dread, you squeeze through the tunnel, crawling blindly for what feels like an eternity through the earth and stone.  Finally, you emerge into the cool night air, collapsing onto soft earth, far from the mansion's oppressive presence. You have escaped the basement's suffocating depths!")
    print("Escape Ending: The Tunnel Run.")

def escape_ending_attic_window():
    print("\nDriven by a desperate need for escape, you cautiously approach the boarded windows, your heart pounding with a mixture of hope and fear.  Examining the aged wood, you discover one section near the corner that is noticeably weaker, the boards thinner and more brittle than the rest. Summoning a surge of adrenaline, you kick out with all your force, splintering the wood and creating a narrow, jagged escape route.")
    print("Ignoring the sharp edges, you climb out onto the steeply pitched roof, the wind whipping at your face.  Carefully, painstakingly, you make your way down the treacherous slope, clinging to crumbling gargoyles and moss-covered shingles.  You slide and scramble down the last section, dropping to the overgrown grounds below, leaving Blackwood Mansion silhouetted against the cold moon.  You have escaped the attic's chilling clutches!")
    print("Escape Ending: The Rooftop Descent.")

def escape_ending_kitchen_pots():
    print("\Driven by a hunch, you begin rummaging through the overturned pots and pans scattered across the kitchen floor.  Beneath a heavy, cast-iron cauldron, you discover a loose flagstone.  Prying it up with trembling hands, you reveal a narrow, earthen passage leading downwards.  A faint breath of fresh air wafts upwards, carrying the scent of soil and freedom.")
    print("Without hesitation, you squeeze into the passage and slide down a short, earthen slope.  You emerge into the cool night air, blinking against the sudden brightness of the moon, a safe distance from Blackwood Mansion. You have escaped through the kitchens!")
    print("Escape Ending: Kitchen Passage.")


def death_ending_basement_symbols():
    print("\nCompelled by a morbid curiosity, you lean closer to the wall and begin tracing the strange symbols etched into the stone. As your fingers brush against the cold glyphs, the guttering candle flame flares violently, casting grotesque shadows that writhe and coalesce into monstrous shapes, then abruptly extinguishes, plunging the passage into absolute, suffocating darkness.  A chilling voice, devoid of warmth or life, whispers directly into your ear, 'Curiosity… can be fatal.'")
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


def play_game():
    creepy_intro()
    mansion_gates() # Start at the gates

if __name__ == "__main__":
    play_game()