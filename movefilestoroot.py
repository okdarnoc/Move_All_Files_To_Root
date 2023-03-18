import os
import shutil

# Prompt user for root folder location
root_folder = input("Enter the directory of the root folder (Example: C:\MP3):\n")

# Traverse root folder and its subdirectories
for subdir, dirs, files in os.walk(root_folder):
    for file in files:
        old_path = os.path.join(subdir, file)
        new_path = os.path.join(root_folder, file)
        if os.path.exists(new_path):
            # Rename the file to make it unique
            base, ext = os.path.splitext(file)
            i = 1
            while True:
                new_base = f"{base}_{i}"
                new_name = f"{new_base}{ext}"
                new_path = os.path.join(root_folder, new_name)
                if not os.path.exists(new_path):
                    break
                i += 1
            print(f"Renaming {file} to {new_name}")
        shutil.move(old_path, new_path)

# Ask user if there are any additional directories to move
while True:
    additional_dir = input("Enter another directory to move (or type 'done' to exit):\n")
    if additional_dir.lower() == "done":
        break
    else:
        for subdir, dirs, files in os.walk(additional_dir):
            for file in files:
                old_path = os.path.join(subdir, file)
                new_path = os.path.join(root_folder, file)
                if os.path.exists(new_path):
                    # Rename the file to make it unique
                    base, ext = os.path.splitext(file)
                    i = 1
                    while True:
                        new_base = f"{base}_{i}"
                        new_name = f"{new_base}{ext}"
                        new_path = os.path.join(root_folder, new_name)
                        if not os.path.exists(new_path):
                            break
                        i += 1
                    print(f"Renaming {file} to {new_name}")
                shutil.move(old_path, new_path)
