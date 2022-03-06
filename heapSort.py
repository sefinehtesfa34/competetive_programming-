class Solution:
    def heapify(self,arr, n, i):
        left=self.getLeftChild(i)
        right=self.getRightChild(i)
        if left < n and arr[left] < arr[i]:
            smallest = left
        else:
            smallest = i
        if right < n and arr[right] < arr[smallest]:
            smallest = right
        if smallest != i:
            self.swap(arr,smallest,i)
            self.heapify(arr,n, smallest)
    def buildHeap(self,arr,n):
        n = int((n//2)-1)
        for k in range(n, -1, -1):
            self.heapify(arr,len(arr),k)
    def HeapSort(self, arr, n):
        self.buildHeap(arr,n)
        for i in range(n-1, 0, -1):
            self.swap(arr,i,0)
            self.heapify(arr, i, 0)
        for i in range(n//2):
            self.swap(arr,i,n-i-1)
    def getLeftChild(self,index):
        return 2*index+1
    def getRightChild(self,index):
        return 2*index+2
    def getParent(self,index):
        return (index-1)//2
    def swap(self,arr,index1,index2):
        arr[index1],arr[index2]=arr[index2],arr[index1]
    
