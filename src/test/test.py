import os

def hello(x):
    return x*10

print (f"Hello {hello(10)}")

print (f"Current DIR is {os.getcwd()}")

env = os.environ;

print (f"Environment {env['IBM_QUANTUM_TOKEN']}");


for key in os.environ.keys():
    print (key)

for value in os.environ.values():
    print(value)


square = lambda x:x*x

print(hello(10))

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


# Access element at row 2, column 3
print(matrix[1][2]) 


a = [10, 12, 'hello', matrix[1][2] ]

print (a)


for i in a:
    print (i)
    if isinstance(i , int) and i % 2 == 0:
        print('even')
    else:
        print('odd or non-number')



a = [10, 20, 30, 40]

x = map( lambda x:x*2, a);

print (a)
for i in x:
    print (i);


list = (1,2,3, 4)

j = 0;
for i in list:
    list[j] = i*2
    j = j+1
    
    
print (list);

