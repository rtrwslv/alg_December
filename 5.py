class TreeNode:
    def __init__(self, val, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right
"""
Используем очередь, пока у нас в ней есть элементы, которые мы кидаем через pop листья в очередь и
строку со стрелочками, затем сращиваем элементы, которые одинаково начинаются и кончаются
"""


root = TreeNode(1, TreeNode(2, TreeNode(5)), TreeNode(3))

quene = []
result = []
quene.append(root)

while quene:
    if quene[0].left:
        result.append(str(quene[0].val) +  "->" + str(quene[0].left.val))
        quene.append(quene[0].left)
    if quene[0].right:
        result.append(str(quene[0].val) +  "->" + str(quene[0].right.val))
        quene.append(quene[0].right)
    quene.pop(0)
for i in range(len(result)):
    for j in range(i, len(result)):
        if result[i][-1] == result[j][0]:
            result[i] += result[j][1:]
            result.pop(j)
print(result)