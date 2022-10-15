class TreeNode {
    constructor(val){
        this.val = val 
        this.left = null 
        this.right = null 
    }
}
const dfs = (root) =>{
    if (root === null){
        return null 
    }
    const stack = [root]
    while (stack.length > 0){
        curNode = stack.pop()
        console.log(curNode.val)
        if (curNode.right) stack.push(curNode.right)
        if (curNode.left) stack.push(curNode.left)
    }
}

const a = new TreeNode('a')
const b = new TreeNode('b')
const c = new TreeNode('c')
const d = new TreeNode('d')
a.left = b 
a.right = c
c.left = d 
dfs(a)
/*
   a
  / \
 b   c
     /
    d
*/