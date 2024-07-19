import pyperclip

def create_comma_separated_list(enclosing_char=''):
    # Get the data from the clipboard
    data = pyperclip.paste()
    
    # Split the data by newline to create a list
    items = data.splitlines()
    
    # Remove any empty strings from the list
    items = [item.strip() for item in items if item.strip()]
    
    # Enclose each item with the specified character, if any
    if enclosing_char:
        items = [f"{enclosing_char}{item}{enclosing_char}" for item in items]
    
    # Join the items into a comma-separated list
    result = ', '.join(items)
    
    return result

def main():
    enclosing_char = input("Enter the enclosing character (or leave blank for none): ")
    result = create_comma_separated_list(enclosing_char)
    print("Comma-separated list:")
    print(result)
    # Copy the result back to the clipboard
    pyperclip.copy(result)
    print("The result has been copied to the clipboard.")

if __name__ == "__main__":
    main()
