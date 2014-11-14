import random

class RandomIndex:
    def __init__(self, wlist):
        self._weighted_init = []        
        self._rsize = sum(wlist)-1      
        self._m = {}                    
        i = 0
        s = wlist[i]
        for n in range(self._rsize+1):
            if n == s:
                i += 1
                s += wlist[i]
            self._m[n] = i
 
    def i(self):
        rn = random.randint(0,self._rsize)  
        return self._m[rn]


values_x = [1,2,3,4,5,6]


weights_x = [1,10,100,1000,10000,100000] # weight list
testing = RandomIndex(weights_x) # instance of RandomIndex

initial = [0,0,0,0,0,0]

for i in range(100000):
    initial[testing.i()] +=1  # keep track of number of times each index was generated
     
    
print(initial)          
 


