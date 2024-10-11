# Task Automation Tool

## Overview
The **Task Automation Tool** is a Python-based utility designed to simplify the process of renaming multiple files in a folder according to customizable formats. This tool supports sequential numbering, date-time stamping, custom file names, and extension changes, making it ideal for organizing large sets of files.

## Features
- **Sequential File Renaming:** Rename files with sequential numbers and optional custom names, dates, and times.
- **Combination Renaming:** Add prefixes, suffixes, or modify the extension without changing the original file names.
- **Date and Time Stamping:** Automatically append file creation date, time, or just the year to file names.
- **Custom Filters:** Option to rename all files in a folder or only files that start with a specific text.
- **Extension Management:** Option to change file extensions or keep the original ones.

## Installation

1. Clone the repository:
    ```bash
   git clone https://github.com/code-freq/task-automation-tool.git
   ```
2. Install the required dependencies (only `tkinter`):
    ```bash
   pip install tk
   ```

## Usage
1. Run the `main.py` script on your IDE.
2. Follow the prompts to select a folder and configure renaming options.

### Modes
- **Sequential Mode:**

    The user is prompted to define a format for the file names using the following keywords:
    - `name`: Custom name for files.
    - `number`: Sequential numbering.
    - `date`: File creation date.
    - `time`: File creation time.
    - `year`: File creation year.

  Example formats:
  - `name,number`: Results in `CustomName_1.ext`
  - `date,name,number`: Results in `10-11-2024_CustomName_1.ext`
  - `name,number,date,time`: Results in `CustomName_1_10-11-2024_14-35-10.ext`


- **Combinational Mode:**

    In this mode, the user can provide a custom prefix, suffix, and extension to rename files, without altering the original name.
    
    Example:
    - Prefix: `Project`
    - Suffix: `Final`
    - Extension: `txt`
  
    Results in: `Project_OriginalName_Final.txt`

### File Filters
- **Rename All Files:**

This option allows you to rename all files in the selected folder.

- **Rename Files Starting with Specific Text:**

Only files that begin with the text you can type will be renamed.

## Example Outputs
- **Sequential Renaming:**
    ```
    Original files:
    - DSC_001.jpg
    - DSC_002.jpg
  
    Renamed files (using name,number,date,time):
    - NewName_1_10-11-2024_14-35-10.jpg
    - NewName_2_10-11-2024_14-35-11.jpg
    ```
- **Combinational Renaming:**
  ```
  Original files:
  - DSC_001.jpg
  - DSC_002.jpg
  
  Renamed files (using prefix, suffix, and extension):
  - Prefix_001_Suffix.NewExt
  - Prefix_002_Suffix.NewExt
  ```

> [!Note]
> 
> The tool provides user-friendly input validation to ensure the correctness of the file renaming process.
> 
> You can choose to skip changing file names or extensions, and the tool will keep them unchanged.

## Contributing
Feel free to fork the repository and submit pull requests with improvements or bug fixes.

## Contact
For suggestions, recommendations, development ideas, or any issues, feel free to reach out at *code.freq7@gmail.com*