import random
def result_():
    list_1 = ['paper', 'rock', 'scissor']
    var_1 = random.choice(list_1)
    print(var_1)
    user_1 = input("enter your choice : ").lower()
    list_1.remove(user_1)
    var_2 =''
    while True :
        if user_1=='rock' and var_1=='paper':
            print("Paper wins ==> Computer Wins")
        elif user_1=='scissor' and var_1=='rock':
            print("Rock wins  ==> Computer Wins")
        elif user_1=='paper' and var_1=='scissor':
            print("Scissor wins  ==> Computer Wins")
        elif user_1=='rock' and var_1=='scissor':
            print("Rock wins  ==> User Wins")
        elif user_1=='paper' and var_1=='rock':
            print("Paper wins  ==> User Wins")
        elif user_1=='scissor' and var_1=='paper':
            print("Scissor wins  ==> User Wins")
        else:
            print("Match is a draw")
        var_2= input('Want to play Again please press (Y/N) : ').upper()
        print(var_2)
        if var_2=="Y":
                result_()
        if var_2=='N':
            break



if __name__=="__main__":
    # list_1 = ['paper', 'rock', 'scissor']
    # var_1=random.choice(list_1)
    # print(var_1)
    result_()
    print("\nThanks for playing")




# Rock vs paper-> paper wins
# scissor vs rock-> Rock wins
# paper vs scissor-> scissor wins.