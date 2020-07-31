#Take user input and convert it to block text
from blockletters import *

def validText(text):
    """Check if text contains only letters and/or exclamation point."""
    for i in text:
        if (i.upper() >= 'A' and i.upper() <= 'Z') or i == '!' or i == ' ':
            continue
        else:
            return False
    return True

def main():
    """Main method."""
    while True:
        text = input('Enter text (leave blank to exit): ').upper()
        if not text:
            break
        if not validText(text):
            print("Invalid text. Only letters and/or exclamation point allowed.")
            continue
        print(letterToBlocks(text))
    
if __name__ == '__main__':
    main()
