import datetime
import time
# class Bike_Types:
#     # suppose we have 60 bikes for rent
#     Bike_1 = 60
#     print(" Rent bikes on hourly basis $5 per hour.\n"
#           " Rent bikes on daily basis $20 per day.\n"
#           " Rent bikes on weekly basis $60 per week\n"
#           " Total Bikes =",Bike_1)
#
# object_1=Bike_Types()
# # print(object_1.Bike_1)

def promotion_discount(Type_2):
    # you will get promotion when you will have more than 3 bikes of any type
    if Type_1==1:
        Total=int(0.7*Type_2*5)
    elif Type_1==2:
        Total = int(0.7*Type_2 * 20)
    else:
        Total = int(0.7*Type_2 * 60)

    retun_bike(Total)
    return Total

def total_amount(Type_1,Type_2):

    if Type_1 == 1:
        time.sleep(5 * 1)
        Total = int(Type_2 * 5)
    elif Type_1 == 2:
        time.sleep(60 * 12 * 60)
        Total = int(Type_2 * 20)
    else:
        time.sleep(60 * 12 * 60 * 7)
        Total = int(Type_2 * 60)
    retun_bike(Total)
    # return Total


def retun_bike(Total):
    return_bike_1=input("Want to Rent Again? Y/N").upper()
    print(f'This is total amount: {Total} \nThank you Please visit Again!')
    if return_bike_1=='Y':
        # go to __name function
        # total_amount(Type_1,Type_2)
        pass
    else:
        # Print Receipt and Close
        pass

def input_1():
    return int(input("enter bike count\n"))

if __name__=="__main__":
    total=0.0
    Bike_1 = 60
    Type_1=int(input("Enter your choice\n1 for Hour basis.\n2 for Day basis.\n3 for Weekly basis\n"))
    Type_2=input_1()
    x = datetime.datetime.now().hour
    y=datetime.datetime.now().minute
    z= datetime.datetime.now().now()
    print(x,y)
    while Type_2>Bike_1:
        print("Invalid Input!")
        Type_2=input_1()
    if Type_2>3:
        promotion_discount(Type_2)
        Bike_1-=Type_2
        print("TOtal Bikes remaining"+Bike_1)
    else:
        total_amount(Type_1,Type_2)
        Bike_1 -= Type_2
    # if Type_1==1:
    #     time.sleep(60*1)
    #     pass
    # elif Type_1==2:
    #     time.sleep(60*12*60)
    # elif Type_1==3:
    #     time.sleep(60 * 24 * 60*7)