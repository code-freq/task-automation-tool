from os.path import getctime, join, splitext
from os import listdir, rename
from tkinter import filedialog
from datetime import datetime

# FUNCTIONS

# Select folder
def select_folder() -> str:
    print("Please select a folder", end=": ")
    selected_folder = filedialog.askdirectory(title="Select a folder")
    print(selected_folder)
    return selected_folder

# Automate and rename the files in a selected folder path
def rename_files(path:str, desired_name:str, desired_ext:str, parts:list[str] or str, filter_:str, start:int or None, seq:bool = False):
    # Sequential automating
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
                        new_name += f"_{file_dict[i]}"

                    # Add extension and crop the first underscore
                    new_name += f".{ori_ext.strip(".")}"
                    new_name = new_name[1:]

                    # Rename the file
                    rename(join(folder_path, filename), join(folder_path, new_name))

                    # Increment counter
                    start += 1

            print("\nAutomation successful!")

        except Exception as e:
            print("Error:",e)

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
                    rename(join(folder_path, filename), join(folder_path, new_name))

            print("\nAutomation successful!")

        except Exception as e:
            print("Error:",e)

# Get current and desired file names and extensions from user
def get_user_input() -> (str, str, list[str] or str, str, int or None, bool):

    # Select automation type
    print("\nSelect automation type\n"
          "Sequential (1)\n"
          "Combinational (2)")

    # Get automation type in error handle loop
    while True:
        inp = input(": ")
        # Get sequential automation parameters from user
        if inp == "1":
            print("\nPlease enter the format of your desired file name using \"name\","
                  " \"number\", \"date\", \"time\" and \"year\" keywords.\n"
                  "Examples of valid formats:\n"
                  "- (e.g. name,number --> School-Project-Video_1.wav)\n"
                  "- (e.g. date,name,number --> 21-03-2022_Wedding_1.wav)\n"
                  "- (e.g. number,name,year --> 3_report-Q1_2023.xlsx\n"
                  "- (e.g. name,number,date,time --> flight_5_10-12-2024_14-48-32.bin")

            # Get format of the desired file name in error handle loop, return as list
            while True:
                format_of_name = input(": ").lower().replace(" ",
                                                             "")  # Minimize potential user errors as much as possible.
                parts = format_of_name.split(",")
                checksum = ["name", "number", "date", "time", "year"]
                invalid = False
                for part in parts:
                    if part not in checksum:
                        invalid = True

                if invalid:
                    print("Invalid format input.")
                    continue
                else:
                    if "number" in parts:
                        break
                    else:
                        print("'Number' is required for sequential numbering.")
                        continue

            invalid_chars = None
            if not parts == ["number"]:
                print("\nEnter the desired file name (Press Enter to not change names)", end="")

                # Get desired file name and extension in error handle loop
                invalid_chars = ["\\/:*?\"<>|"]

            desired_extension = None
            while True:
                if not parts == ["number"]:
                    desired_filename = input(": ")
                    invalid = False
                    for char in desired_filename:
                        if char in invalid_chars:
                            invalid = True
                else:
                    desired_filename = ""

                if not invalid:
                    desired_extension = input("Type extension (Press Enter to not change extensions): ").lower().strip(". ")
                    break
                else:
                    print("Invalid file name")
                    continue

            # Get starting number for file numbering from user in error handle loop
            print("Please provide the starting number for file numbering", end="")
            int_inp = None
            while True:
                num_int = input(": ").strip()
                try:
                    int_inp = int(num_int)
                except ValueError:
                    print("Invalid input")
                    continue
                if 1 > int_inp:
                    print("Please enter a number bigger than 0")
                    continue
                else:
                    break

            print("\nWould you like to rename all files or only those starting with a specific text?")
            print("Rename all files (1)")
            print("Rename only files starting with specific text (2)")

            # Another error handle loop for filter selection
            filter_out = None
            while True:
                choice = input(": ").strip()
                if choice == "1":
                    filter_out = ""
                    break
                elif choice == "2":
                    filter_out = input("Enter the text that the files should start with: ")
                    break
                else:
                    print("Invalid input")
                    continue

            return desired_filename, desired_extension, parts, filter_out, int_inp, True

        # Get combinational automation parameters from user
        elif inp == "2":
            prefix = input("Type prefix (Press Enter for no prefix): ")
            suffix = input("Type suffix (Press Enter for no suffix): ")
            ext = input("Type extension (Press enter to not change extensions): ").lower().strip(". ")

            print("\nWould you like to rename all files or only those starting with a specific text?")
            print("Rename all files (1)")
            print("Rename only files starting with specific text (2)")

            # Another error handle loop for filter selection
            filter_out = None
            while True:
                choice = input(": ").strip()
                if choice == "1":
                    filter_out = ""
                    break
                elif choice == "2":
                    filter_out = input("Enter the text that the files should start with: ")
                    break
                else:
                    print("Invalid input")
                    continue

            return prefix, suffix, ext, filter_out, None, False

        # Invalid input
        else:
            print("Invalid input")
            continue


# MAIN

print("------------------- Welcome to Task Automation Tool -------------------\n")

folder_path = select_folder()

main_bool = True
while main_bool:
    des_name, des_ext, format_parts, filt, starting, seq_comb = get_user_input()
    rename_files(folder_path, des_name, des_ext, format_parts, filt, starting, seq_comb)

    print("\nContinue automating with current folder (1)\n"
          "Select new folder (2)\n"
          "Exit (Q)")

    # Get user process selection in error handle loop
    while True:
        user_inp = input(": ")

        if user_inp == "1":
            break
        elif user_inp == "2":
            folder_path = select_folder()
            break
        elif user_inp == "Q":
            print("Exiting the application...")
            main_bool = False
            break
        else:
            print("Invalid input")
            continue







