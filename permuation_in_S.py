# Example: Given a smaller strings and a bigger string b, 
# design an algorithm to find all permutations of the shorter string within the longer one. 
# Print the location of each 
# from typing import Counter
# class Solution:
    # def BpermutationInS(self,B,S):
    #     unique = 0
    #     dic = Counter(B)
    #     left = 0
    #     right = len(B) - 1
    #     answer = []
    #     while right < len(S):
    #         if right - left == len(B) or (S[right] in dic and dic[S[right]] ==0):
    #             if unique == len(set(B)):
    #                 answer.append((left,right))
    #             left += 1
    #             char = S[left]
    #             if char in dic:
    #                 dic[char] += 1
    #                 unique -= 1
    #         char = S[right]
    #         if char in dic:
    #             if dic[char] ==0:
    #                 unique += 1
    #             else:
    #                 dic[char] -= 1
    #                 if dic[char] == 0:
    #                     unique += 1
    #         right += 1
    #     return answer
            
            