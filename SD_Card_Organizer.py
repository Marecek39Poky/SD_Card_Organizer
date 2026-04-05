# Imports some needed utilities
import os
import shutil
from datetime import datetime
from pathlib import Path

# Sets the current date to a variable
date_today = datetime.now().strftime("%Y-%m-%d")

# Asks the user which directory to organize
input_dir_to_organize = input("Which directory would you like to organize?")

# Cleans the user input
dir_to_organize = input_dir_to_organize.replace("\\", "/").replace('"', "").strip()

# Verification of the directory to organize
print("📁 Directory:", dir_to_organize)

dir_contents = os.listdir(dir_to_organize)

print("📄 Contents:")
print(dir_contents)

confirm_directory = input("Is this the right directory? (Y/N): ")

new_folder_name_from_user = input("Create a name for the new organized directory: ")

# Creates new directories
desktop_dir = Path.home() / "Desktop"
new_folder_name = f"{date_today} {new_folder_name_from_user}"
new_folder_path = desktop_dir / new_folder_name

(new_folder_path).mkdir(parents=False, exist_ok=False)
(new_folder_path / "Photos").mkdir(parents=False, exist_ok=False)
(new_folder_path / "Videos").mkdir(parents=False, exist_ok=False)
(new_folder_path / "Videos/Shots").mkdir(parents=False, exist_ok=False)
(new_folder_path / "Videos/Proxy").mkdir(parents=False, exist_ok=False)
print(f"Successfully created folders in {new_folder_path}")

# Functions to copy from different manufacturers structures
def sony_sdcard_copy():
    sony_path_shots = Path(dir_to_organize) / "PRIVATE/M4ROOT/CLIP"
    sony_path_proxy = Path(dir_to_organize) / "PRIVATE/M4ROOT/SUB"
    sony_path_photos = Path(dir_to_organize) / "DCIM"

    if sony_path_shots.exists():
        print("Copying original shots...")
        for file in sony_path_shots.glob("*.MP4"):
            shutil.copy2(file, new_folder_path / "Videos/Shots" / file.name)
            print(f" Success: {file.name}")
    else:
        print("No original shots found.")
    if sony_path_proxy.exists():
        print("Copying proxy shots...")
        for file in sony_path_proxy.glob("*.MP4"):
            shutil.copy2(file, new_folder_path / "Videos/Proxy" / file.name)
            print(f" Success: {file.name}")
    else:
        print("No proxy shots found.")
    if sony_path_photos.exists():
        print("Copying RAW photos...")
        for photo in sony_path_photos.rglob("*.ARW"):
            shutil.copy2(photo, new_folder_path / "Photos" / photo.name)
            print(f" Success: {photo.name}")
    else:
        print("No RAW photos found.")

# Calls functions
if confirm_directory.lower() == "y":
    print("Copying starting...")
    sony_sdcard_copy()
else:
    print("Program aborted by user. Exiting...")
    exit()