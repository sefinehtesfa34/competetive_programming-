class Solution:
    def intersection(self,line1,line2):
        x1 = line1[0][0]
        x2 = line1[1][0]
        y1 = line1[0][1]
        y2 = line1[1][1]
        #Case I
        if x1 == x2:
            pass 
        else:
            pass 
        # Case II
        if y1 == y2:
            pass 
        else:
            pass 
        
        ''' /
    _______/_________________
          /
         /
         y = 2x + 4
         = 4x - 9
            \      |
              \  |
                \|           /
                |\         /  (x2,y2)
 _______________|_\______/______
                |  \    /
                |       /
                |      /
                |     /
                |         (x21,y21)
         
         
         
         
         
         
        ''' 
solution = Solution()
line1 = list(input().split())
line2 = list(input().split())
result = solution.intersection(line1,line2)
print(result)
