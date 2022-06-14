def even_num(n):
    i=1
    while n:
        yield 2*i
        i += 1
        n-=1
Iterator=even_num(10)
print(Iterator)
list_1=[]
while True:
    try:
        list_1.append(next(Iterator))
    except:
        break
print(list_1)


# list_2=[i*2 for i in range(1,11)]
# print(list_2)

# Generator second
def mygenerator():
    print('First item')
    yield 10

    print('Second item')
    yield 20

    print('Last item')
    yield 30
itr=mygenerator()
print(next(itr))
print(next(itr))
print(next(itr))


# 3rd program
# Here is an example of a python inbuilt iterator
# value can be anything which can be iterate
iterable_value = [1,2,3,4,5,6]
iterable_obj = iter(iterable_value)   #iter iterator
print("Thired program starts")
while True:
    try:
        item = next(iterable_obj)
        print(item)
    except StopIteration :
        break


#Code 4th
# A simple generator for Fibonacci Numbers
def fib(limit):
    # Initialize first two Fibonacci Numbers
    a, b = 0, 1

    # One by one yield next Fibonacci Number
    while a < limit:
        yield a
        a, b = b, a + b


# Create a generator object
x = fib(5)
print("\nUsing for in loop")
for i in fib(5):
    print(i)
list_3=[]
while True:
    try:
        list_3.append(next(x))
    except StopIteration:
        break
print(list_3)
