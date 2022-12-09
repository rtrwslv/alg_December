class LinkedList:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
head = LinkedList(1, LinkedList(0, LinkedList(1)))
s = ""
while head:
    s += str(head.val)
    head = head.next
print(int(s, 2))