

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def topView(root):
    if(root == None):
        return
    q = []
    m = dict()
    hd = 0
    root.hd = hd
 
    # push node and horizontal
    # distance to queue
    q.append(root)
 
    while(len(q)):
        root = q[0]
        hd = root.hd
 
        # count function returns 1 if the
        # container contains an element
        # whose key is equivalent to hd,
        # or returns zero otherwise.
        if hd not in m:
            m[hd] = root.info
        if(root.left):
            root.left.hd = hd - 1
            q.append(root.left)
 
        if(root.right):
            root.right.hd = hd + 1
            q.append(root.right)
 
        q.pop(0)
    for i in sorted(m):
        print(m[i], end=" ")
    #Write your code here

