class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        val=0
        cap=capacity
        for i in range(len(plants)-1):
            val+=1
            cap-=plants[i]
            if cap<plants[i+1]:
                val+=len(plants[:i+1])*2
                cap=capacity
        return val+1