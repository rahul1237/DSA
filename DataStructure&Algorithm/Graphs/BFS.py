# v as vertex
# e as edges
# a as matrix of order v*v
# f as first_vertex
# s as second_vertex
# sv as startingvertex
# vd as visited array
# ans as answer

print("""1. Enter number of verticies in the graph
2. Enter the number of edges in graph
3. Enter the staring vertex
4. Enter the edges btw 2 verticies!\n\n""")

# ans function
def ans(a,v,sv,vd):
    # array that works like queue stores the value of node and then delete it
    arr=[]
    arr.append(sv)
    # mark starting vertex as visited
    vd[sv]=1
    while(len(arr)!=0):
        x=arr[0]
        print(x)
        arr.remove(x)
        for i in range(v):
            if(x==i):
                continue
            if(a[x][i]==1):
                if(vd[i]==1):
                    continue
                arr.append(i)
                vd[i]=True

v=int(input())
e=int(input())
sv=int(input())

# creation of matrix of order v*v

import numpy as np

a=np.zeros(shape=(v,v),dtype=int)

# looping for updating the matrix

for _ in range(e):
    f,s=map(int,input().split())
    a[f][s]=True
    a[s][f]=True

# created an empty array to enter the visited verticies

vd=[]
for _ in range(v):
    vd.append(0)

# anspart

ans(a,v,sv,vd)


# CodeBy: RAHUL MAHAJAN
# CF: anonymous3107
# CC: anonymous0201