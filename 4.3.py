guess = input("Guess a letter: ").lower()

if len(guess)>1 and guess.isalpha():
    print ("E1")
elif len(guess) == 1 and not guess.isalpha():
    print ("E2")
elif len(guess)>1 and not guess.isalpha():
    print ("E3")