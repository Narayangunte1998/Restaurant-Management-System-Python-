# calculate max number
list_1=[1,2,4,9,200,0,432]
list_1.sort(reverse=1)
print(list_1[0])
# or we can go for
c=1
def funCtion(list_2):
    for i in range(0,len(list_2)):
        for j in range(0, len(list_2)):
            if list_2[i]>list_2[j]:
                c=list_2[i]
                list_2[i] =list_2[j]
                list_2[j]=c
    return list_2[0]
print(funCtion(list_1))