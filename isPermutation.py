# class Solution:
#     def isPermutation(self,word1,word2):
#         num = 0
#         for char in word1:
#             num |= 1 << ord(char) - ord('a')
#         for char in  word2:
#             if num & 1 << ord(char) - ord('a') == 0:
#                 return False 
        # return True 
    # aaab 
    # abc 
    
'''
[1 2 3 4]
[5 6 7 8]
[9 10 11 12]                 
[13 14 15 16]

[13 9 5 1] take a pattern => initial position | after 90 degree rotation (0,0)
[14 10 6 2]          num = 13       (3, 0)    | (0, 0) new i = i - 3, new j = j - 0
[15 11 7 3]   j      num = 14       (3,1)     | (1,0)  new i = i - 2, new j = j - 1
[16 12 8 4]   |      num = 11       (2,2)     | (2,1)  new i = i - 0, new j = j - 1
            |    
            |__ num = 7 =>(1,2)
____________|__|______________ i
            |__|(2,-1)
            |
            |
            |
'''







