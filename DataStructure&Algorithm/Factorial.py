# function for finding the factorial of the number!

def fact(a):
    if(a==1):
        return 1
    elif(a==0):
        return 1
    else:
        return (a*fact(a-1))

print(fact(int(input())))