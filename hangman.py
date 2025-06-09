# HANGMAN <3
import random

FILE_NAME= "words.txt"
def get_words_from_file():
    """
    This function has been implemented for you. It opens a file, 
    and stores all of the lines into a list of strings. 
    It returns a list of all lines in the file. 
    """
    lines = []
    with open(FILE_NAME) as f:
        for line in f:
            # removes whitespace characters (\n) from the start and end of the line
            line = line.strip() 
            # if the line was only whitespace characters, skip it 
            if line != "":
                lines.append(line)
                
    return lines
def play_game(words):
    random_word = random.choice(words)
    print("words include animals🐹/birds🕊️/fruits🍒/objects🧸")
    print(f"the word starts with {random_word[0]} and ends with {random_word[-1]}")
    for i in range(len(random_word)):
        print("__",end=" ")
    while True:
        guess=input("guess my word 🍓🍍:(type no if you fail to guess/type hint if you want a hint) ").lower()
        if guess==random_word:
            print("Yayy you guessed it correctly🦊🌸")
            break
        elif len(guess)!=len(random_word) and guess!=random_word and guess!="no" and guess!="hint":
            print(f"your word has {len(guess)} letters in it, mine has {len(random_word)} letters....try again!🔁 ")
        elif guess== "no" and guess!="hint" :
            print(f"my word is {random_word}, you did your best!!!🐥🍀")
            break
        elif guess=="hint":
            print(f"the 2nd letter is {random_word[1]}")
        else:
            print(f"both words have {len(guess)} letters in it, but the guess is incorrect...try again!🐰✨")
    

def main():
    words = get_words_from_file()
    play_game(words)
main()

