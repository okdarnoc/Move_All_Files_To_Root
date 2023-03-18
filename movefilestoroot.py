import os
import shutil

# Prompt user for root folder location
root_folder = input("Enter the directory of the root folder(Example: C:\MP3) \n 請輸入檔案路徑(例子:C:\MP3:) \n")

# Traverse root folder and its subdirectories
for subdir, dirs, files in os.walk(root_folder):
    for file in files:
        old_path = os.path.join(subdir, file)
        new_path = os.path.join(root_folder, file)
        shutil.move(old_path, new_path)

# Ask user if there are any additional directories to move
while True:
    additional_dir = input("Enter another directory to move (or type 'done' to exit): 請輸入另一個檔案路徑 (或輸入 'done' 完成")
    if additional_dir.lower() == "done":
        break
    else:
        for subdir, dirs, files in os.walk(additional_dir):
            for file in files:
                old_path = os.path.join(subdir, file)
                new_path = os.path.join(root_folder, file)
                shutil.move(old_path, new_path)
