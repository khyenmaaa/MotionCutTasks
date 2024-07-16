def count_words(text):
    words = text.split()
    return len(words)

def main():
    print("Enter a sentence or a paragraph:")
    user_input = input("> ").strip()
    if not user_input:
        print("Error: You entered an empty string. Please enter some text.")
        return
    
    word_count = count_words(user_input)
    
    print(f"The number of words in your input is: {word_count}")

main()
