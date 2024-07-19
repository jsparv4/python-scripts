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
- No need to try to copy the output to the clipboard. This is handled automatically by the script.
- Only ranges from a single column, such as A1:A28 or C2:C17, give the intended result.

## Example

Turn a list like:

Sample1
Sample2
Sample3
Sample4
Sample5
Sample6
Sample7
Sample8
Sample9
Sample10
Sample11
Sample12

into:

'Sample1', 'Sample2', 'Sample3', 'Sample4', 'Sample5', 'Sample6', 'Sample7', 'Sample8', 'Sample9', 'Sample10', 'Sample11', 'Sample12'

In practice, copy the stacked list above: highlight the selection and ctrl + c.
Run the script.

## Practice

Then you can easily paste into a SQL query: 
   ```bash
      SELECT * FROM tbl_sample WHERE sample_field IN ('Sample1', 'Sample2', 'Sample3', 'Sample4', 'Sample5', 'Sample6', 'Sample7', 'Sample8', 'Sample9','Sample10', 'Sample11', 'Sample12');
