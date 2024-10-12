from os.path import getctime, join, splitext
from os import listdir, rename
from tkinter import filedialog
from datetime import datetime

# FUNCTIONS

# Select folder
def select_folder() -> str:
    return filedialog.askdirectory(title="Select a folder")  # Returns "" when process canceled

# Automate and rename the files in a selected folder path
def rename_files(path:str, desired_name:str, desired_ext:str, parts:list[str] or str, filter_:str,
                 start:int or None, seq:bool = False) -> (str,str):
    # Sequential Automation
    if seq:
        try:
            # For every file in the selected folder
            for filename in listdir(path):
                name, ori_ext = splitext(filename)
                if name.startswith(filter_):

                    # Process name
                    if not desired_name == "":
                        name = desired_name

                    # Process extension
                    if not desired_ext == "":
                        ori_ext = desired_ext

                    # Create file dict
                    file_dict = {}
                    for part in parts:
                        part = part.lower()
                        # Process date and time fields
                        if part in ["date", "time", "year"]:
                            timestamp = getctime(path + "/" + filename)
                            file_date = datetime.fromtimestamp(timestamp)
                            if part == "date":
                                file_dict[part] = f"{file_date.day}-{file_date.month}-{file_date.year}"
                            elif part == "time":
                                file_dict[part] = f"{file_date.hour}-{file_date.minute}-{file_date.second}"
                            else:
                                file_dict[part] = f"{file_date.year}"

                        # Process name field
                        elif part == "name":
                            file_dict[part] = name

                        # Process number field
                        else:
                            file_dict[part] = start

                    # Create new name
                    new_name = ""
                    for i in parts:
                        i = i.lower()
                        new_name += f"_{file_dict[i]}"

                    # Add extension and crop the first underscore
                    new_name += f".{ori_ext.strip(".")}"
                    new_name = new_name[1:]

                    # Rename the file
                    rename(join(path, filename), join(path, new_name))

                    # Increment counter
                    start += 1

            return "Automation Successful!", "green"

        except Exception as e:
            return f"Error: {e}", "red"

    # Combinational Automation
    else:
        prefix = desired_name
        suffix = desired_ext
        ext = parts
        try:
            # For every file in the selected folder
            for filename in listdir(path):
                name, ori_ext = splitext(filename)
                if name.startswith(filter_):

                    # Process extension
                    if not ext == "":
                        ori_ext = ext

                    # Create new name
                    prefix_ = prefix + "_" if not prefix == "" else prefix
                    suffix_ = "_" + suffix if not suffix == "" else suffix
                    new_name = f"{prefix_}{name}{suffix_}.{ori_ext.strip(".")}"

                    # Rename the file
                    rename(join(path, filename), join(path, new_name))

            return "Automation Successful!", "green"
        except Exception as e:
            return f"Error: {e}", "red"
