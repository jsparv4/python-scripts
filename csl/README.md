# Excel to Comma Seperated List Utility

This utility script converts a copied range of Excel cells from a single column into a comma-separated list, with optional enclosing characters for each item. The result is then copied back to your clipboard for easy pasting into SQL queries, documents, or text editors.

I have been using the following website utility for this purpose at work for several months now: https://sql.info/h/tools/in-clause/

I wanted to make an 'offline' version that is
1. more flexible. this version lets you pick the enclosing argument or none at all.
2. efficient. no need to ctrl + c, ctrl + v, ctrl + a endlessly when going back and forth from the web tool to your dbms.
3. stable. if the site above becomes unavailable, I would be forced to do this anyway.
   
## Features

- Converts a newline-separated list from Excel into a comma-separated list.
- Optionally encloses each item with a character specified by the user.
- Copies the result back to the clipboard for convenience.

## Requirements

- Python 3.x
- `pyperclip` library

## Installation

1. **Install Python**: Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
2. **Install `pyperclip` library**: Install the required library by running the following command in your terminal or command prompt:
   ```bash
   pip install pyperclip

## Usage

1. **Copy Data from Excel**: Open your .xlsx or .csv file and select the range you want to transform into a comma-separated list. Press ctrl + c.
2. **Save the Script** Save the csl.py script file.

## Run the Script

1. Open terminal or command prompt.
2. Navigate to the directory where you saved **`csl.py`**
3. Run the script by typing 
    ```bash
    python csl.py

## Pitfalls

- Make sure your range is copied to the clipboard before you run the script.
- No need to try to copy the output to the clipboard. This is handled automatically by the script :)
