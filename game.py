# import random
# def add , mins and genius
# put the variable in randint
# name variable and add it into add, mins and genius
# name choice of the levels
# put if coundtion and while coundtion
# after that break to stop the operation



import random

def add(x,y) :
    return num1+num2
def mins(x,y):
    return x-y
def genius(x,y,z,l,m):
    return x+y-z+l*m

num1 = random.randint(0, 1000)
num2 = random.randint(0, 1000)
num3 = random.randint(0, 1000)
num4 = random.randint(0, 1000)
num5 = random.randint(0, 1000)
r = add(num1, num2)
rs = mins(num1,num2)
rss = genius(num1, num2, num3, num4, num5)
print("- - - - - - -let's play calculator game - - - - - - -")
print("- - - - - - -choose the levels- - - - - - - ")
print("- - - - - - 1.Easy question- - - - - - - -")
print(" - - - -- - 2.Normal question- - - - - ")
print(" - - - - - - 3.Hard question- - - - - -")

while True:
    choose = input(' ( 1 / 2 / 3 ) : ')
    if choose in ('1','2','3'):
        if choose=='1':
            print(num1,"+",num2,"=")
            result = int(input(" enter the the result : "))
            
            if r == result:
                print("true")           
            else:
                print("false")    
        if choose=='2':
            print(num1,"-",num2,"=")
            result = int(input(" enter the the result : "))   
            if rs == result:
                print("true")           
            else:
                print("false")    
        if choose=='3':
            print(num1,"+",num2,"-",num3,"+",num4,"*",num5)
            result = int(input(" enter the the result : "))   
            if rss == result:
                print("true")           
            else:
                print("false")   
    break  



                 
    

    
