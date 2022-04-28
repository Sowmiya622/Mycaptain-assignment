#program to print fibonacci series

num=int(input("enter any number"))
a=0
b=1
c=0
if num<=0:
    print("please enter a number greater than zero")
else:
    for i in range(0,num):
        print(c,end=" ")
        c=a+b
        a=b
        b=c
    
