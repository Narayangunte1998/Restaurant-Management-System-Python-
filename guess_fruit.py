import random

someWords = '''apple banana mango strawberry orange grape pineapple apricot lemon coconut watermelon cherry papaya berry peach lychee muskmelon'''

someWords = someWords.split(' ')
word = random.choice(someWords)
word_list=list(word)
# del word_list[0]
# print(word_list)
guesses=2+len(word_list)
list_1= ['-'] * len(word_list)
# print(list_1)
for i in list_1:
    print(i,end=' ')
k=0
kk=0
for i in range (0,guesses):
    guess_char = input("\nenter your guess character\n")
    for j in range(0, len(word_list)):
        if guess_char==word_list[j]:
            list_1[j]=word_list[j]
            word_list[j]=0
            print("your letter is in word with position",j+1)
            kk=1
            k+=1
            for char in list_1:
                print(char, end=' ')
            break
    if k==len(word_list):
        break
    if ~kk==1:
        print("your letter is not in word, Try again.")
    guesses -= 1
    print("Remaining guesses are:",guesses)
if k==len(word_list):
    str=''
    for i in range(0,len(list_1)):
        str=str+list_1[i]
    print("you win the Game the name of fruit is ",str)
else:
    print("you lose")