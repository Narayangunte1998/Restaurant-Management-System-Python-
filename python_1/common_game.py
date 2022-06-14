


input_1=input("enter the name of player 1\n").lower()
input_2=input("enter the name of player 2\n").lower()
list_1=list(input_1)
# print(list_2,len(list_2))
list_2=list(input_2)
# print(list_2,len(list_2))
list_3=[]

if len(list_1)<len(list_2):
    for i in list_1:
        for j in list_2:
            # print(list_3)
            if i==j:
                # print(list_3)
                list_3.append(j)
                # list_1.remove(i)
                list_2.remove(j)
                break

# print(list_3)
for i in list_3:
    list_1.remove(i)
count_1=len(list_1)+len(list_2)
list_4=[]
list_4=list_1+list_2
print(list_4,count_1)
while count_1>5:
    list_4.remove(list_4[4])
    list_5=list_4[5:]
    list_6=list_4[0:4]
    list_4=list_5+list_6
    count_1-=1
print(list_4)
k=''
if len(list_4)==1 or len(list_4)==3:
    k=list_4[0]
elif len(list_4)==2 or len(list_4)==4 or len(list_4)==5:
    k=list_4[1]

# flames
if 'f'==k:
    print('Friend')
elif 'l'==k:
    print('Love')
elif 'a'==k:
    print('Affection')
elif 'm'==k:
    print('Marriage')
elif 'e'==k:
    print('Enemy')
elif 's'==k:
    print('Siblings')
else:
    print("Match not found")