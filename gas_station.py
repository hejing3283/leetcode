class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        #### methods 2: similar logic, but some optimization
        if sum(gas) < sum(cost): return -1
        n =len(gas)
        if n == 1: return (-1 if gas[0] < cost[0] else 0)
        curr = 0 ; cnt = 0 
        for i in range(n):
            if gas[i] + curr < cost[i] : 
                curr = 0 ; cnt = i+1; 
            else : 
                curr += gas[i] - cost[i]
        return cnt
    
        ### methods 1: TLE
        # diff = [  gas[i] - cost[i] for i in range(len(gas)) ] 
        # idxMax = sorted(range(len(diff)), key= lambda k:diff[k], reverse = True) 
        
        # if diff[idxMax[0]] < 0: return -1
        
        # def dfs(idx):
        #     prev = gas[idx]; curr = prev - cost[idx]; 
        #     for i in range(idx+1, len(gas)) + range(0, idx+1) :
        #         if curr < 0: return -1 
        #         prev = curr ; curr += gas[i] - cost[i]
        #     return idx

        # while idxMax: 
        #     tmp = idxMax.pop()
        #     resIdx = dfs(tmp)
        #     if resIdx != -1:
        #         return resIdx
        # return -1         
                
        
        