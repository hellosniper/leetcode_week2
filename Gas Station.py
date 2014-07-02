# Gas Station.py
# Children with a higher rating get more candies than their neighbors.
# Question: There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
#           You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). 
#           You begin the journey with an empty tank at one of the gas stations.
#           Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.
#           
# Question from: https://oj.leetcode.com/problems/gas-station/
# Solution:
# 1. If car starts at A and can not reach B. Any station between A and B can not reach B.(B is the first station that A can not reach.)
#    Then we start from B+1, so on so forth 
# 2. If the total number of gas is bigger than the total number of cost. There must be a solution.

# Author: DongDing 
# Date: 2014/07/01
# Time complexity:  O(n)
# space complexity:  O(1)  
# Tag: 
# Comment: 


class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        tank = 0
        gas_needed = 0
        length = len(gas)
        start = 0 # keep track of starting point
        for i in range(length):
            tank = tank + gas[i] - cost[i]
            if tank < 0:
                gas_needed = gas_needed + tank  # borrow some gas, (tank is a negtive number)
                tank = 0
                start = i+1 # change the start from the next station
                
        if tank + gas_needed >= 0:
            if start == length:
                return 0
            else:
                return start
        else:
            return -1
        
        
gas = [1,2]
cost = [2,1]
a = Solution()
print a.canCompleteCircuit(gas, cost)
