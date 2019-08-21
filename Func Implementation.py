def myFun(x):
    x = 20
x = 10
myFun(x);
print(x)

def evenOdd(x):
    if(x % 2 == 0):
        print ("even")
    else:
        print ("odd")
        
def myFun2(x):
    x[0] = 20
    
lst = [10 ,11 , 12, 13, 14, 15]
myFun2(lst);
print(lst)

def swap(x, y):
    temp = x;
    x = y;
    y = temp;
x = 2
y = 3
swap(x, y)
print(x)
print(y)