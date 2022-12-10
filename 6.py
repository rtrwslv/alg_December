class TreeNode:
    def __init__(self, val, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

"""
По сути, мы складываем высоту левого и правого дерева
"""

root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(4), TreeNode(5)))
quene_left = []
quene_right = []
result_left = 0
result_right = 0
quene_left.append(root.left)
quene_right.append(root.right)


while quene_left:
    if quene_left[0].left:
        quene_left.append(quene_left[0].left)
    if quene_left[0].right:
        quene_left.append(quene_left[0].right)
    elif not (quene_left[0].right and quene_left[0].left):
        result_left += 1
    quene_left.pop(0)

while quene_right:
    if quene_right[0].left:
        quene_right.append(quene_right[0].left)
    if quene_right[0].right:
        quene_right.append(quene_right[0].right)
    elif not (quene_right[0].right and quene_right[0].left):
        result_right += 1
    quene_right.pop(0)

print(result_left + result_right)