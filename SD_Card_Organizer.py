import os

# Asks the user which directory to organize
input_dir_to_organize = input("Type which directory to organize: ")

dir_to_organize = input_dir_to_organize.replace("\\", "/").replace('"', "").strip()

print("📁 Directory:", dir_to_organize)

dir_contents = os.listdir(dir_to_organize)

print("📄 Contents:")
print(dir_contents)

confirm_directory = input("Is this the right directory? (Y/N): ")

if confirm_directory.lower() == "y":
    print("Copying starting...")
else:
    print("Program aborted by user. Exiting...")
    exit()
