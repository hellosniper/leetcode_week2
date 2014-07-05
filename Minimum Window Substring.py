# Minimum Window Substring.py
# Question:  Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
#            For example,
#            S = "ADOBECODEBANC"
#            T = "ABC"
#            Minimum window is "BANC".
#           
# Question from: https://oj.leetcode.com/problems/minimum-window-substring/
# Sulotion:  

# Author: DongDing 
# Date: 2014/07/05
# Time complexity:  O(n)
# space complexity:  O(256)  
# Tag: # Greedy Algorithm
# Comment: 

class Solution:
    # @return a string
    def minWindow(self, S, T):
        if len(S) == 0 or len(T) == 0 or len(S) < len(T):          
            return ""
        minLen = len(S)
        minIndex = 0
        start = 0
        tNum = [0 for i in range(256)]
        windowNum = [0 for i in range(256)]
        foundNum = 0
        isFound = False
        # Store ASCII of T 
        for i in range(len(T)): 
            tNum[ord(T[i])] += 1
        right = 0
        while right < len(S):
            #print "right", right
        #for right in range(len(S)):
            while right <len(S) and foundNum < len(T):
                if windowNum[ord(S[right])] < tNum[ord(S[right])]:
                    foundNum +=1
                windowNum[ord(S[right])] += 1
                right += 1
            if foundNum == len(T):
                isFound = True
                while start < right:
                    if windowNum[ord(S[start])] > tNum[ord(S[start])]:
                        windowNum[ord(S[start])]  -= 1
                        start += 1
                    else:
                        break
                
                if minLen > (right - start ):
                    minLen = right - start
                    minIndex = start
                foundNum -= 1
                windowNum[ord(S[start])] -=1
                start +=1
                #right -=1
                
        if isFound == True:
            return S[minIndex : minIndex+minLen]    
        return ""
