import random

def main():
    print("Hello! I'm going to try to guess your name.\n")
    name = input("First, what is your name? Enter here: ")
    answer = False
    while answer == False:
        guess = random.randint(15, 30)
        print("Your age is: " + str(guess))
        clarify = input("Did I get it right? (Type 'y' or 'n'): ")
        if clarify == 'y':
            answer = True
        elif clarify == 'n':
            answer = False
            print("Dang! Let me try again...")
    print("Yay! I got it! Wanna go again?")
main()
