class Solution: 
    def select(self, arr, i):
        return i,arr
    def selectionSort(self, arr,n):
        for k in range(n):
            mn=arr[k]
            index=k
            for j in range(k+1,n):
                if arr[j]<mn:
                    mn=arr[j]
                    index=j
            start,arr=self.select(arr,k)
            val=arr[start]
            arr[start]=arr[index]
            arr[index]=val
        return arr