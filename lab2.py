def dfs(src,target,limit,visited_states):
    
    if src==target:
        return True
    
    if limit<=0:
        return False
    
    visited_states.append(src)
    
    
    adj = possible_moves(src,visited_states)
    
    for move in adj:
        if dfs(move,target,limit-1,visited_states):
            return True
    return False

def possible_moves(state,visited_states): 
    # Find index of empty spot and assign it to b
    
    b = state.index(-1)  
    
    #'d' for down, 'u' for up, 'r' for right, 'l' for left - directions array
    d = []
                                    
   
    
    if b+3 in range(9):
        d.append('d')
    if b-3 in range(9):
        d.append('u')
    if b not in [0,3,6]:
        d.append('l')
    if b not in [2,5,8]:
        d.append('r')
    
   
    pos_moves = []
    
   
    for move in d:
        pos_moves.append(gen(state,move,b))
        
    
    return [move for move in pos_moves if move not in visited_states]

def gen(state, m, b):
       temp = state.copy()                            
    
    
    if m=='d':
        a = temp[b+3]
        temp[b+3]=temp[b]
        temp[b]=a
    elif m=='u':
        a = temp[b-3]
        temp[b-3]=temp[b]
        temp[b]=a
    elif m=='l':
        a = temp[b-1]
        temp[b-1]=temp[b]
        temp[b]=a
    elif m=='r':
        a = temp[b+1]
        temp[b+1]=temp[b]
        temp[b]=a
    
    
    return temp

def iddfs(src,target,depth):
    visited_states = []
 
    for i in range(1, depth+1):
        if dfs(src, target, i, visited_states): return True
    return False

src = ['*','2','4','*','-1','*','*','3','1']
target = ['-1','1','2','3','4','*','*','*','*']         
       


depth = 4
print(iddfs(src, target, depth))

# Test 2
src = [1,2,3,-1,4,5,6,7,8] 
target=[1,2,3,6,4,5,-1,7,8]

depth = 1
iddfs(src, target, depth) src = None
target = None






iddfs(src, target, depth) 
src = [1, 2, 3, 4, 5, 6, 7, 8, -1]
target = [-1, 1, 2, 3, 4, 5, 6, 7, 8]
for i in range(1, 100):
    val = iddfs(src,target,i)
    print(i, val)
    if val == True:
        break

    src = [5,2,4,6,-1,7,8,3,1]
target = [-1,1,2,3,4,5,6,7,8]    
for i in range(1, 5):
    val = iddfs(src,target,i)
    print(i, val)
    if val == True:
        break

