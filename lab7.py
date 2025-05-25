from collections import deque
tree={
    'A':['B','F','D','E'],
    'B' : ['K','J'],
    'K': ['N','M'],
    'N':[],
    'M':[],
    'J':[],
    'F':[],
    'D':['G'],
    'E':['C','H','I'],
    'I':['L'],
    'L':[],
    'C':[],
    'H':[],
    'G':[]

}
def depth_limiting(start,goal,limit):
    stack=[(start,[start],0)]
    visited=set()

    while stack:
        start,path,current_depth=stack.pop()
        if (start==goal):
            return path
        if (current_depth<limit):
            visited.add(start)
            for child in reversed(tree[start]):
                if child not in visited:
                    stack.append((child,path+[child],current_depth+1))
    return None
def iterative_deepening_search(start,goal):
    depth=0
    while(True):
        result=depth_limiting(start,goal,depth)
        if result is not None:
            return result
        depth+=1
        if(depth>len(tree)):
            return None
        
dls_result=depth_limiting('A','G',3)                
ids_result=iterative_deepening_search('A','G')
if(len(dls_result)<len(ids_result)):
    print("depth limiting search is more efficient")
elif(len(ids_result)<len(dls_result)):
    print("iterative deepening search is more efficient")    
else:
    print("both are equal")
    
print(dls_result)       
    
    
 