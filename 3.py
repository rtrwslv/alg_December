class TreeNode:
    def __init__(self, val, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(3, TreeNode(9, TreeNode(10), TreeNode(5)), TreeNode(20, TreeNode(15), TreeNode(7)))

queue = []
result = []
queue.append(root)

while(queue):
    qlen = len(queue)
    values = 0
    for i in range(qlen):
        node = queue.pop(0)
        values += node.val
        if node.left:   
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    result.append(values/qlen)

print(result)