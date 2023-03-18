# moveallfilestoroot
This program/script moves all files within the subdirectories of a specified root folder to the root folder itself. It uses the os and shutil modules to traverse the subdirectories and move the files.
# Move Files to Root Folder Script

This Python script moves all files within the subdirectories of a specified root folder to the root folder itself. It uses the `os` and `shutil` modules to traverse the subdirectories and move the files.

## Installation

To use this script, you will need to have Python installed on your computer. You can download Python from the [official website](https://www.python.org/downloads/).

You will also need to have the `os` and `shutil` modules installed. These modules are included with Python by default, so you do not need to install them separately.

## Usage

1. Clone or download this repository to your computer.
2. Open a terminal or command prompt window and navigate to the root folder of the cloned/downloaded repository.
3. Run the script by entering the following command: `python move_files_to_root.py`
4. When prompted, enter the directory path of the root folder you wish to use.
5. The script will then move all files within the subdirectories of the specified root folder to the root folder itself. If there are any files in the root folder with the same name as files being moved from the subdirectories, the script will overwrite them.

Note: It's important to use this script with caution, as it has the potential to overwrite existing files if not used properly.

## Use Case

Use Case
Do you have a folder full of subfolders containing files that you want to move to one main folder? For example, let's say you have a folder named "Pictures" that contains subfolders for each year, and each year folder contains subfolders for each month. If you want to move all your pictures to one main folder, this Python script can help!

Using the script is easy:

Download the script from this repository and save it to your computer.
Open a terminal or command prompt window and navigate to the folder where you saved the script.
Run the script by entering the following command: python move_files_to_root.py
When prompted, enter the directory path of the main folder you want to move the files to (in this case, the "Pictures" folder).
The script will move all the files from the subfolders into the main folder, overwriting any files with the same name in the main folder.
Note: It's important to be careful when using this script, as it has the potential to overwrite existing files in the main folder if they have the same name as files being moved from the subfolders. It's recommended that you backup any important files before running the script or modify the script to rename any files that have the same name as existing files in the main folder.

For the example we used above, the script would move all the files from the subfolders (e.g. "Pictures/2019/January/pic1.jpg", "Pictures/2019/February/pic2.jpg", etc.) to the "Pictures" folder. Once the script is done running, all the pictures will be in one place and it will be much easier to view and organize them.

### Code

```python
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

