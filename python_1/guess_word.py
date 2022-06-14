import random
import tkinter as tk

words=['q','w','e','r','t','y','u','a','i','o','p','s','d','f','g','h'
    ,'j','k','l','z','x','c','v','b','n','m']

word = random.choice(words)
guess_ = int(input("how many guesses you want\n"))

print(word)
for i in range(0,guess_):
    var_1 = input("guess the Character from a to z\n")
    if var_1 > word:
        print('You entered char is greater than expected char')
    elif var_1 < word:
        print('You entered char is lesser than expected char')
    elif var_1==word:
        print("Congratulations! your guess is correct")
        print( f"remaining guesses are {guess_ - 1}")
        guess_-=1
        break
    else:
        print('oops you missed Try again\n',f"remaining guesses are {guess_-1}")
        guess_-=1
