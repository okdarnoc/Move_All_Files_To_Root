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

This script can be useful in situations where you have a large number of files spread across multiple subdirectories and you want to consolidate them into a single directory. For example, you may have a folder containing multiple subfolders of images, and you want to move all the images into a single folder to make it easier to browse and organize them.
By using this script, you can quickly and easily move all the files within the subdirectories to the root folder, without having to manually copy and paste each file. This can save a significant amount of time and effort, especially when dealing with a large number of files.
Note that this script should be used with caution, as it has the potential to overwrite existing files in the root folder if they have the same name as files being moved from the subdirectories. It's recommended that you backup any important files before running the script, or modify the script to rename any files that have the same name as existing files in the root folder.

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

