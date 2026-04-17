#Unit 3
#Beginner

def practice_3_beginner():
    print("\n" + "=" * 50)
    print("EXERCISE 3.1: Pickle & Project Setup")
    print("=" * 50)
    
    import pickle
    import os

    # --- Part A: Pickle ---
    shopping_list = ["Apples", "Bananas", "Milk", "Bread"]

    with open("shopping.pkl", "wb") as f:
        pickle.dump(shopping_list, f)
    print("Shopping list pickled!")

    with open("shopping.pkl", "rb") as f:
        loaded_list = pickle.load(f)
    print(f"Loaded list: {loaded_list}")

    loaded_list.append("Eggs")
    loaded_list.append("Cheese")
    with open("shopping.pkl", "wb") as f:
        pickle.dump(loaded_list, f)
    print("Updated list saved")
    
    # --- Part B: Directory Structure ---

    project_name = "my_project"
    if not os.path.exists(project_name):
        os.mkdir(project_name)

    subdirs = ["src", "docs", "tests", "data"]
    for subdir in subdirs:
        path = os.path.join(project_name, subdir)
        os.makedirs(path, exist_ok=True)

    # Create README.md
    with open(os.path.join(project_name, "README.md"), "w") as f:
        f.write("# My Project\n\nProject description goes here.\n")

    # Create src/main.py
    with open(os.path.join(project_name, "src", "main.py"), "w") as f:
        f.write('def main():\n    print("Hello, World!")\n\nif __name__ == "__main__":\n    main()\n')

    # List project structure
    print("\nProject structure:")
    for root, dirs, files in os.walk(project_name):
        level = root.replace(project_name, "").count(os.sep)
        indent = "  " * level
        print(f"{indent}{os.path.basename(root)}/")
        for file in files:
            print(f"  {indent}{file}")

practice_3_beginner()




#Intermediate

def practice_3_intermediate():
    print("\n" + "=" * 50)
    print("EXERCISE 3.2: File Organizer")
    print("=" * 50)

    import os
    import shutil

    messy_folder = "messy_files"

    # --- Setup: Create messy folder with test files ---
    os.makedirs(messy_folder, exist_ok=True)

    test_files = [
        "document.txt", "image.jpg", "photo.png",
        "report.pdf", "script.py", "data.csv",
        "music.mp3", "video.mp4", "archive.zip"
    ]

    for filename in test_files:
        filepath = os.path.join(messy_folder, filename)
        with open(filepath, "w") as f:
            f.write(f"Test file: {filename}")

    print(f"Created {len(test_files)} test files in '{messy_folder}'")

    # Category mapping
    organized = {
        "documents": [".txt", ".pdf", ".doc"],
        "images":    [".jpg", ".png", ".gif"],
        "code":      [".py", ".js", ".html"],
        "data":      [".csv", ".json", ".xml"],
        "media":     [".mp3", ".mp4", ".avi"],
        "archives":  [".zip", ".tar", ".rar"]
    }

    # --- Create organized folders ---
    for category in organized:
        path = os.path.join(messy_folder, category)
        os.makedirs(path, exist_ok=True)

    # --- Organize files ---
    moved = 0
    for filename in os.listdir(messy_folder):
        filepath = os.path.join(messy_folder, filename)

        # Skip directories
        if os.path.isdir(filepath):
            continue

        ext = os.path.splitext(filename)[1].lower()  # e.g. ".jpg"

        # Find matching category
        destination_folder = None
        for category, extensions in organized.items():
            if ext in extensions:
                destination_folder = category
                break

        if destination_folder:
            dest_path = os.path.join(messy_folder, destination_folder, filename)
            shutil.move(filepath, dest_path)
            print(f"  Moved '{filename}' → {destination_folder}/")
            moved += 1
        else:
            print(f"  No category found for '{filename}', left in place.")

    print(f"\nTotal files moved: {moved}")

    # --- Show organized structure ---
    print("\nOrganized structure:")
    for root, dirs, files in os.walk(messy_folder):
        level = root.replace(messy_folder, "").count(os.sep)
        indent = "  " * level
        print(f"{indent}{os.path.basename(root)}/")
        for file in files:
            print(f"  {indent}{file}")

practice_3_intermediate()




#Advanced

import pickle
import os
import shutil
from datetime import datetime
from pathlib import Path

class GameState:
    def __init__(self):
        self.player_name = ""
        self.level = 1
        self.score = 0
        self.inventory = []
        self.position = (0, 0)

    def __str__(self):
        return f"{self.player_name} - Level {self.level}, Score: {self.score}"


def practice_3_advanced():
    print("\n" + "=" * 50)
    print("EXERCISE 3.3: Game Save System")
    print("=" * 50)

    # --- TODO 2: Create and populate a game state ---
    game = GameState()
    game.player_name = "Hero"
    game.level = 5
    game.score = 1250
    game.inventory = ["Sword", "Shield", "Potion"]
    game.position = (10, 25)

    # --- TODO 3: Create saves directory and save game with pickle ---
    saves_dir = "saves"
    os.makedirs(saves_dir, exist_ok=True)

    save_path = os.path.join(saves_dir, "savegame.pkl")
    with open(save_path, "wb") as f:
        pickle.dump(game, f)
    print(f"Game saved to '{save_path}'")

    # --- TODO 4: Load and verify saved game ---
    with open(save_path, "rb") as f:
        loaded_game = pickle.load(f)

    print("\nLoaded game state:")
    print(f"  Player:    {loaded_game.player_name}")
    print(f"  Level:     {loaded_game.level}")
    print(f"  Score:     {loaded_game.score}")
    print(f"  Inventory: {loaded_game.inventory}")
    print(f"  Position:  {loaded_game.position}")

    # --- TODO 5: Multiple save slots ---
    def save_game(game_state, slot_number):
        """Save game to a specific slot"""
        slot_path = os.path.join(saves_dir, f"slot_{slot_number}.pkl")
        with open(slot_path, "wb") as f:
            pickle.dump(game_state, f)
        print(f"  Saved to slot {slot_number}: '{slot_path}'")

    print("\nSaving to multiple slots:")
    for slot in range(1, 4):
        game.score += 100
        game.level += 1
        save_game(game, slot)

    # --- TODO 6: List all save files ---
    print("\nAll save files:")
    for filename in sorted(os.listdir(saves_dir)):
        filepath = os.path.join(saves_dir, filename)
        size = os.path.getsize(filepath)
        modified = datetime.fromtimestamp(os.path.getmtime(filepath))
        print(f"  {filename:25s}  {size} bytes  (modified: {modified:%Y-%m-%d %H:%M:%S})")

    # --- TODO 7: Backup function ---
    def create_backup(source_dir, backup_dir="backups"):
        """Create timestamped backup of source directory"""
        os.makedirs(backup_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        backup_path = os.path.join(backup_dir, f"backup_{timestamp}")
        shutil.copytree(source_dir, backup_path)
        print(f"Backup created: '{backup_path}'")
        return backup_path

    backup_path = create_backup(saves_dir)

    # --- TODO 8: Verify backup ---
    def verify_backup(source, backup):
        """Check all files in source are also in backup"""
        source_files = set(os.listdir(source))
        backup_files = set(os.listdir(backup))
        missing = source_files - backup_files

        if not missing:
            print(f"Backup verified — all {len(source_files)} files present.")
            return True
        else:
            print(f"Backup incomplete! Missing files: {missing}")
            return False

    verify_backup(saves_dir, backup_path)

    # --- TODO 9: Cleanup old backups ---
    def cleanup_old_backups(backup_dir, keep_count=3):
        """Keep only the most recent N backups"""
        if not os.path.exists(backup_dir):
            print("No backup directory found.")
            return

        backups = sorted(
            [os.path.join(backup_dir, d) for d in os.listdir(backup_dir)],
            key=os.path.getmtime
        )

        to_delete = backups[:-keep_count] if len(backups) > keep_count else []

        if not to_delete:
            print(f"No cleanup needed — {len(backups)} backup(s) exist (limit: {keep_count}).")
        else:
            for old_backup in to_delete:
                shutil.rmtree(old_backup)
                print(f"  Deleted old backup: '{old_backup}'")
            print(f"Kept {keep_count} most recent backup(s).")

    create_backup(saves_dir)
    create_backup(saves_dir)
    print("\nRunning cleanup (keep 2):")
    cleanup_old_backups("backups", keep_count=2)


practice_3_advanced()


