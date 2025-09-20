import random

number = random.randint(1,100)
print("Welccome! u have 7 chances to guess the number")
ch = 7
gc = 0

while gc < ch:
    gc += 1
    guess = int(input("Guess the number"))

    if guess == number:
        print("Good job u'r guess is corret!{number}")
        break
  
    elif guess > number:
            print("no it's smaller")

    elif guess < number:
        print("No it's bigger")
