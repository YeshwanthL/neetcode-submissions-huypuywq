class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyHashSet:

    def __init__(self):
        self.bucket = [ListNode(0) for _ in range(10**4)]

    def add(self, key: int) -> None:
        curr = self.bucket[ key % len(self.bucket) ]

        while curr.next:
            if curr.next.val == key:
                return
            curr = curr.next
        curr.next = ListNode(key)

    def remove(self, key: int) -> None:
        curr = self.bucket[key%len(self.bucket)]

        while curr.next:
            if curr.next.val == key:
                curr.next = curr.next.next

    def contains(self, key: int) -> bool:
        curr = self.bucket[key%len(self.bucket)]

        while curr.next:
            if curr.next.val == key:
                return True
            curr = curr.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)