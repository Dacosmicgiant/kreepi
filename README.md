### A text based horror game

blackwood_mansion_game/
├── core/
│ ├── game_state.py # Manages player inventory, sanity, and game flags
│ ├── utils.py # Utility functions (make_choice, modify_sanity)
├── data/
│ ├── lore_data.py # Lore variables, family backstory, riddles
│ ├── events_data.py # Random events (sound, sensory, visual, dynamic)
├── locations/
│ ├── **init**.py # Makes 'locations' a Python package
│ ├── hallway.py
│ ├── landing.py
│ ├── study.py
│ ├── library.py
│ ├── master_bedroom.py
│ ├── bathroom.py
│ ├── attic_stairs.py
│ ├── attic.py
│ ├── basement_stairs.py
│ ├── basement_hall.py
│ ├── basement_storage.py
│ ├── basement_ritual_chamber_door.py
│ ├── basement_ritual_chamber.py
│ ├── mansion_entrance.py
├── main.py # Main game script (entry point, game loop, intro)
