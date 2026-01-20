import random

def main():
    print("Hello! I'm going to try to guess your name.\n")
    name = input("First, what is your name? Enter here: ")
    answer = False
    guess_list = []
    while answer == False:
        guess = random.randint(15, 30)
        guess_list.append(guess)
        print("Your age is: " + str(guess))
        clarify = input("Did I get it right? (Type 'y' or 'n'): ")
        if clarify == 'y':
            if guess in guess_list:
                print("Hey! You said no to that earlier! Liar!")
            answer = True
        elif clarify == 'n':
            if guess in guess_list:
                print("Oh yeah, you said no already. My bad.")
            answer = False
            print("Dang! Let me try again...")
    print("Yay! I got it! Wanna go again?")
main()
