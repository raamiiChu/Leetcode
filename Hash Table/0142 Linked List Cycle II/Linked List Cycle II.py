# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# time: O(N)
# space: O(1)

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:  # 兩者相遇則跳出迴圈
                break
        else:  # 沒有 cycle 回傳 None
            return None
        
        slow = head  # 初始化 slow
        while slow != fast:  # 兩者一次都只走一步，重疊者為所求
            slow = slow.next
            fast = fast.next
        return slow