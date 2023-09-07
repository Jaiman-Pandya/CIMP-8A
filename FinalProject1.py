def menu():
    print("MENU")
    print("a - Capitalize")
    print("b - Punctuate")
    print("c - Condense")
    print("d - CountWords")
    print("e - CharCount")
    print("f - Exit")

def capitalize(text):
    caps_count = 0
    new_text = text[0].upper()
    for i in range(1, len(text)):
        if text[i - 1] in [".", "!", "?"] and text[i].islower():
            new_text += text[i].upper()
            caps_count += 1
        else:
            new_text += text[i]
    print("Capitalized letter count:", caps_count)
    return new_text

def punctuate(text, exclam_count=0, semicolon_count=0):
    new_text = text.replace("!", ".")
    exclam_count = text.count("!")
    new_text = new_text.replace(";", ",")
    semicolon_count = text.count(";")
    print("Punctuation replaced\nExclamation count:", exclam_count, "\nSemicolon count:", semicolon_count)
    return new_text

def condense(text):
    while "  " in text:
        text = text.replace("  ", " ")
    return text

def count_words(text):
    return len(text.split())

def count_chars(text):
    return len(text) - text.count(" ")

def process_choice(choice, text):
    if choice == 'a':
        return capitalize(text)
    elif choice == 'b':
        return punctuate(text)
    elif choice == 'c':
        return condense(text)
    elif choice == 'd':
        print("Word count:", count_words(text))
        return text
    elif choice == 'e':
        print("Char count:", count_chars(text))
        return text
    elif choice == 'f':
        return None

def main():
    user_text = input("Enter text: ")
    print("You entered:", user_text)

    while True:
        menu()
        user_choice = input("Choose: ").lower()
        if user_choice in ['a', 'b', 'c', 'd', 'e', 'f']:
            user_text = process_choice(user_choice, user_text)
            if user_text is None:
                break
            print("Modified text:", user_text)
        else:
            print("Invalid choice, try again.")

if __name__ == '__main__':
    main() 