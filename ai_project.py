
# coding: utf-8

# In[1]:


import numpy as np
import heapq
import collections


# In[2]:


#3. Define a possible heuristic function (forward cost)
def Gap_Heuristic(tmp):
    
    res = 0
    for i in range(1,len(tmp)):
        if abs(tmp[i]-tmp[i-1]) != 1:
            res += 1
    
    return res


# In[3]:


class priority_queue:
    def __init__(self):
        self.elements = []
        
    def empty(self):
        return len(self.elements) == 0
    
    def put(self,item,priority):
        heapq.heappush(self.elements,(priority,item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]


# In[4]:


#4. Implement an A* algorithm in your language of preference

#start_pancakes = [3,2,5,1,6,4,7]

def A_star(start_pancakes,backward_cost):
    process = priority_queue()
    process.put(start_pancakes,0)
    backward_cost[str(start_pancakes)] = []


    while not process.empty():

        pancakes = process.get()

        if Gap_Heuristic(pancakes) == 0:
            break

        for i in range(1,len(pancakes)):


            pancakes = list(pancakes)
            tmp = pancakes[:i+1][::-1] + pancakes[i+1:]
            h = Gap_Heuristic(tmp)

            #check if it's already there

            if backward_cost[str(tmp)] == 0:
                if backward_cost[str(pancakes)] != 0:
                    path = backward_cost[str(pancakes)].copy()
                else:
                    path = []

                backward_cost[str(tmp)] = path
                backward_cost[str(tmp)].append(i+1)
                total_cost = h + len(backward_cost[str(tmp)])
                process.put(tmp,total_cost)

            else:
                if (len(backward_cost[str(tmp)])+1) <= len(backward_cost[str(pancakes)]):
                    backward_cost[str(tmp)].append(i+1)
                    total_cost = h + len(backward_cost[str(tmp)])
                    process.put(tmp,total_cost) 
                else:
                    continue


    if pancakes[0] == 5:
        backward_cost[str(pancakes)].append(5)
        return (backward_cost[str(pancakes)])
        pancakes = pancakes[::-1]
    else:
        return(backward_cost[str(pancakes)])


# In[5]:


#extra credits

def extra_credits(start_pancakes,backward_cost):
    process = priority_queue()
    process.put(start_pancakes,0)
    backward_cost[str(start_pancakes)] = []


    while not process.empty():

        pancakes = process.get()

        if pancakes[0] == 1 and pancakes[1] == 2 and pancakes[2] == 3 and pancakes[3] == 4 and pancakes[4] == 5:
            break

        for i in range(1,len(pancakes)):


            pancakes = list(pancakes)
            tmp = pancakes[:i+1][::-1] + pancakes[i+1:]

            #check if it's already there

            if backward_cost[str(tmp)] == 0:
                if backward_cost[str(pancakes)] != 0:
                    path = backward_cost[str(pancakes)].copy()
                else:
                    path = []

                backward_cost[str(tmp)] = path
                backward_cost[str(tmp)].append(i+1)
                total_cost = len(backward_cost[str(tmp)])
                process.put(tmp,total_cost)

            else:
                if (len(backward_cost[str(tmp)])+1) <= len(backward_cost[str(pancakes)]):
                    backward_cost[str(tmp)].append(i+1)
                    total_cost = len(backward_cost[str(tmp)])
                    process.put(tmp,total_cost) 
                else:
                    continue

 
    return (backward_cost[str(pancakes)])


# In[11]:


if __name__ == "__main__":
    
    #1. Define the problem as a searching problem
    #Initial state    
    start_pancakes = np.random.permutation([1,2,3,4,5])
    print('initial state: ',start_pancakes)
    
    #2. Define a possible cost function (backward cost)
    backward_cost = collections.Counter()  

    ans = A_star(start_pancakes,backward_cost)
    print('paths: ', ans)
    
    print('extra credits: ')
    start_pancakes = np.random.permutation([1,2,3,4,5])
    print('initial state: ',start_pancakes)
    backward_cost = collections.Counter()
    
    ans = extra_credits(start_pancakes,backward_cost)
    print('paths: ', ans)

