# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.head=head
        self.next=next
        curr=head
        sum=0
        while curr!=None:
            curr=curr.next
            sum+=1
        
        curr=head
        for i in range(sum//2):
            curr=curr.next
        return curr