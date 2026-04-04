import os
import shutil
from datetime import datetime
from pathlib import Path

date_today = datetime.now().strftime("%Y-%m-%d")

# Asks the user which directory to organize
input_dir_to_organize = input("Type which directory to organize: ")

dir_to_organize = input_dir_to_organize.replace("\\", "/").replace('"', "").strip()

print("📁 Directory:", dir_to_organize)

dir_contents = os.listdir(dir_to_organize)

print("📄 Contents:")
print(dir_contents)

confirm_directory = input("Is this the right directory? (Y/N): ")

new_folder_name_from_user = input("Type name for the new organized directory: ")

desktop_dir = Path.home() / "Desktop"
new_folder_name = f"{date_today} {new_folder_name_from_user}"
new_folder_path = desktop_dir / new_folder_name

(new_folder_path).mkdir(parents=False, exist_ok=False)
(new_folder_path / "Photos").mkdir(parents=False, exist_ok=False)
(new_folder_path / "Videos").mkdir(parents=False, exist_ok=False)
(new_folder_path / "Videos/Shots").mkdir(parents=False, exist_ok=False)
(new_folder_path / "Videos/Proxy").mkdir(parents=False, exist_ok=False)
print(f"Sucessfully creted folders in {new_folder_path}")

def sony_sdcard_copy():
    path_shots = Path(dir_to_organize) / "PRIVATE/M4ROOT/CLIP"
    path_proxy = Path(dir_to_organize) / "PRIVATE/M4ROOT/SUB"
    path_photos = Path(dir_to_organize) / "DCIM"

    if path_shots.exists():
        print("Copying original shots...")
        for file in path_shots.glob("*.MP4"):
            shutil.copy2(file, new_folder_path / "Videos/Shots" / file.name)
            print(f" OK: {file.name}")
    else:
        print("No original shots found.")
    if path_proxy.exists():
        print("Copying proxy shots...")
        for file in path_proxy.glob("*.MP4"):
            shutil.copy2(file, new_folder_path / "Videos/Proxy" / file.name)
            print(f" OK: {file.name}")
    else:
        print("No proxy shots found.")
    if path_photos.exists():
        print("Copying raw photos...")
        for photo in path_photos.rglob("*.ARW"):
            shutil.copy2(photo, new_folder_path / "Photos" / photo.name)
            print(f" OK: {photo.name}")
    else:
        print("No raw photos found.")

if confirm_directory.lower() == "y":
    print("Copying starting...")
    sony_sdcard_copy()
else:
    print("Program aborted by user. Exiting...")
    exit()