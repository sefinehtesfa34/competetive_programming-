class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=[]
        for i in range(len(nums1)):
            check=0
            index=nums2.index(nums1[i])
            for j in range(index+1,len(nums2)):
                if nums1[i]<nums2[j]:
                    l.append(nums2[j])
                    check=1
                    break
            if not check:
                l.append(-1)
        return l
                