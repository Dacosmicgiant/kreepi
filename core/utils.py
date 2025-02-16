# core/utils.py

import random
from blackwood_mansion_game.core import game_state  # Import game_state to access sanity_level

def modify_sanity(amount):
    game_state.sanity_level += amount
    game_state.sanity_level = max(0, min(100, game_state.sanity_level))
    if game_state.sanity_level <= 30:
        print("\nYour sanity is fraying. The mansion's horrors are taking their toll. Reality seems to blur at the edges.")
    elif game_state.sanity_level <= 60:
        print("\nYour unease grows. The oppressive atmosphere of Blackwood Mansion is starting to affect your mind.")

def make_choice(prompt, choices):
    print(prompt)
    for i, choice in enumerate(choices):
        print(f"{i+1}. {choice}")
    if game_state.player_inventory: # Access player_inventory from game_state
        print("\nInventory:")
        for item in game_state.player_inventory: # Access player_inventory from game_state
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
    from blackwood_mansion_game.data import events_data # Import events_data here to avoid circular import

    sound_events = events_data.sound_events
    sensory_events = events_data.sensory_events
    visual_events = events_data.visual_events
    dynamic_events = events_data.dynamic_events

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
        if game_state.sanity_level < 50: # Access sanity_level from game_state
            print(f"Your mind, already strained, interprets the sounds as {chosen_event.lower()}... or is it something worse? Your senses are no longer reliable.")
        else:
            print(chosen_event)
        print()
        modify_sanity(-2) # Use modify_sanity function from utils