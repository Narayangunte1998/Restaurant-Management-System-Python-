import random
player_1=str(random.randint(1,10000))
# print(player_1)
list_=list(player_1)
print(list_)
list_1= ['-'] * len(list_)
list_3=['-'] * len(list_)
# print(list_1)
for i in list_1:
    print(i,end=' ')
# player_2=input("enter the guess number")
guess_value=int(input("\nguesses"))

for j in range(0,guess_value):
    player_2 = str(input("enter the guess number\n"))
    list_2 = list(player_2)
    print(list_2)
    # list_2= ['-'] * len(list_)
    for i in range(0,len(list_1)):
        # print(list_[i])
        if list_[i]==list_2[i]:
            list_3[i]=list_[i]
            # print(list_3)
    # print(list_3)
    str1=''
    for i in list_3:
        str1+=i
    print(str1)
    if str1==player_2:
        print("Congratulations you win number matches")
        break
    else:
        print("Number partially matches")
