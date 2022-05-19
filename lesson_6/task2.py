class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root):

        if not root: return None
        q = [root]
        while q:
            for i in range(1, len(q)):
                q[i - 1].next = q[i]
            q = [kid for node in q for kid in (node.left, node.right) if kid]

        return root

