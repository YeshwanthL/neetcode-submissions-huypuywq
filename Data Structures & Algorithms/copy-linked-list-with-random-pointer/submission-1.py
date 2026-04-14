"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        listCopy = {None : None}
        curr = head

        while curr:
            copy = Node(curr.val)

            listCopy[curr] = copy
            curr = curr.next
        
        curr = head

        while curr:
            copy = listCopy[curr]
            copy.next = listCopy[curr.next]
            copy.random = listCopy[curr.random]
            curr = curr.next
        
        return listCopy[head]