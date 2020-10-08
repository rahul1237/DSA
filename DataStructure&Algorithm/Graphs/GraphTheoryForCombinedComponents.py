# v as vertex
# e as edges
# a as matrix of order v*v
# f as first_vertex
# s as second_vertex
# sv as startingvertex
# vd as visited array
# ans as answer
# DFS is the function for answer of the combined components


print("""1. Enter number of verticies in the graph
2. Enter the number of edges in graph
3. Enter the edges btw 2 vertivies!\n\n""")

# ans function
def ans(a,v,sv,vd):
    print(sv)
    vd[sv]=1
    for _ in range(v):
        if(_==sv):
            continue
        if(a[sv][_]==1):
            if(vd[_]==1):
                continue
            ans(a,v,_,vd)

def DFS(a,v):
    # created an empty array to enter the visited verticies

    vd=[]
    for _ in range(v):
        vd.append(0)
    # check which of the element is not visited

    for i in range(v):
        if(vd[i]==0):
            ans(a,v,i,vd)



v=int(input())
e=int(input())
# sv=int(input())

# creation of matrix of order v*v

import numpy as np

a=np.zeros(shape=(v,v),dtype=int)

# looping for updating the matrix

for _ in range(e):
    f,s=map(int,input().split())
    a[f][s]=True
    a[s][f]=True



# anspart

DFS(a,v)

                                                                   # !!SAMPLE CASE!!


                                                    # Consider a GRAPH having:

                                                    #             9 nodes
                                                    #             8 edges

                                                    #vertices are:
                                                                    # -
                                                                # 0 1  |
                                                                # 1 2  |        1st component
                                                                # 1 3  |
                                                                # 2 3  |
                                                                    #  -
                                                                # 4 7  |
                                                                # 4 8  |        2nd component
                                                                # 7 8  |
                                                                    #  -
                                                                # 5 6  |        3rd component
                                                                    #  -


                                    # Here the graph is in the component form so its illogical
                                    # to talk about BFS and DFS as both of them give same output!


                                                    # Output:
                                                            # 0
                                                            # 1
                                                            # 2
                                                            # 3
                                                            # 4
                                                            # 7
                                                            # 8
                                                            # 5
                                                            # 6


# CodeBy: RAHUL MAHAJAN
# CF: anonymous3107
# CC: anonymous0201