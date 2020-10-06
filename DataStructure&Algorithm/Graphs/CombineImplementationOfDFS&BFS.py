# v as total number of verticies in the graph
# e as total number of edges in the graph
# sv as the starting vertex from where we start printing the graph
# vd as the visited array
# ea as edges array
# s1 and s2 are starting and ending verticies of the graph
# DFS function that implements Depth First Search
# BFS function that implements Breadth First Search


print("""1. Enter number of verticies in the graph!
2. Enter the number of edges in graph!
3. Enter the staring vertex!
4. Enter the edges btw 2 vertivies!\n\n""")


def DFS(ea,v,sv,vd):
    # creation of visited array!
    for _ in range(v):
        vd.append(0)
    print(sv)
    vd[sv]=True
    for _ in range(v):
        if(sv==_):
            continue
        if(ea[sv][_]==True and vd[_]==False):
            DFS(ea,v,_,vd)



def BFS(ea,v,sv,vd):
    # creation of visited array
    for _ in range(v):
        vd.append(0)
    # creation of queue
    queue=[]
    queue.append(sv)
    # mark the sv as visited
    vd[sv]=1
    while(len(queue)!=0):
        x=queue[0]
        print(x)
        queue.remove(x)
        for _ in range(v):
            if(x==_):
                continue
            if(ea[x][_]==True and vd[_]==False):
                queue.append(_)
                vd[_]=True




# input of basic details

v=int(input())
e=int(input())
sv=int(input())
vd=[]

# creation of edges array(it is or order vertex * vertex)

import numpy
ea=numpy.zeros((v,v),dtype=int)

# insertion of edges in the edge array

for _ in range(e):
    s1,s2=map(int,input().split())
    ea[s1][s2]=True
    ea[s2][s1]=True

# BFS RESULT
print('The BFS Output of the above data is:')
BFS(ea,v,0,vd)

# clear vd array as all the vertices get visited in BFS CASE due to which all positions are 1
vd.clear()


# DFS RESULT
print('The DFS Output of the above data is:')
DFS(ea,v,0,vd)

                                                    # !!SAMPLE CASE!!


                                # Consider a GRAPH having:

                                #             8 nodes
                                #             9 edges
                                #             0 as the staring vertex!

                                      #vertices are:
                                #                 0 4
                                #                 0 5
                                #                 3 6
                                #                 3 4
                                #                 5 6
                                #                 7 6
                                #                 3 2
                                #                 3 1
                                #                 2 1


                                    # BFS(check the graph breadth wise!):
                                    #     Output: 0 4 5 3 6 1 2 7

                                    # DFS(check the graph depth wise!):
                                    #     Output: 0 4 3 1 2 6 5 7


                                    
# CodeBy: RahulMahajan
# CC: anonymous0201
# CF: anonymous3107