# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
#     def getNext(self):
#         return self.next
#
#     def getData(self):
#         return self.val
#
#     def setNext(self, nextNode):
#         self.next = nextNode
#
#
# class UnorderList(object):
#     def __init__(self):
#         self.head = None
#
#     def getHead(self):
#         return self.head
#
#     def isEmpty(self):
#         return self.head is None
#
#     def add(self, item):
#         node = ListNode(item)
#         node.next = self.head
#         self.head = node
#
#     def size(self):
#         current = self.head
#         count = 0
#         if (current is not None):
#             count += 1
#             current = current.getNext()
#
#         return count
#
#     def append(self, item):
#         node = ListNode(item)
#         # if self is None
#         #     self.head = node
#         if self.isEmpty():
#             self.head = node
#         else:
#             current = self.head
#             while current.getNext() is not None:
#                 current = current.getNext()
#             current.setNext(node)
#
#     def printList(self):
#         current = self.head
#         if self.isEmpty():
#             print('Empty')
#         else:
#             while current is not None:
#                 if current is not None:
#                     # print(1)
#                     print(current.getData())
#                     current = current.getNext()
#
# List = UnorderList()
# List.append(1)
# List.append(2)
# List.append(3)
#
# List.printList()
#

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # l1 = ListNode(l1)
        # l2 = ListNode(l2)
        l3 = ListNode(None)
        j = 0
        x = 0
        while(l1 is not None or l2 is not None):
            if l1 is None:
                l1 = ListNode(0)
            if l2 is None:
                l2 = ListNode(0)
            i = (l1.val + l2.val) % 10
            node = ListNode((i + j) % 10)
            if  l3 is None:
                l3 = node
            else:
                l3.next = node
                l3 = l3.next
            j = (l1.val + l2.val + j) // 10
            l1 = l1.next
            l2 = l2.next
            if x is 0 :
                phead = l3
                x= 1
        if j == 1:
            l3.next = ListNode(1)

        return phead

l1 = ListNode(2)
l2 = ListNode(4)
# l3 = ListNode(3)
l1.next = l2
# l2.next = l3

l4 = ListNode(5)
l5 = ListNode(6)
l6 = ListNode(9)
l4.next = l5
l5.next = l6

s1 = Solution()
print(s1.addTwoNumbers(l1,l4).val)
print(s1.addTwoNumbers(l1,l4).next.val)
print(s1.addTwoNumbers(l1,l4).next.next.val)
print(s1.addTwoNumbers(l1,l4).next.next.next.val)




