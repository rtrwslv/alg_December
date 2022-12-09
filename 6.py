class TreeNode:
    def __init__(self, val, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right
root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
quene = []
result = 0
quene.append(root)

while quene:
    if quene[0].left:
        quene.append(quene[0].left)
    if quene[0].right:
        quene.append(quene[0].right)
    elif not (quene[0].right and quene[0].left):
        result += 1
    quene.pop(0)

print(result)