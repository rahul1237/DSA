def hcf(a,b):
    if(b!=0):
        return hcf(b,a%b)
    else:
        return a

print(hcf(int(input()),int(input())))