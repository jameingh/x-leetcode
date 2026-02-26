from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        题目：141. 环形链表
        思路引导：
        1. 想象“操场跑步”。
        2. 如果链表带环，快慢指针最终会发生什么？
        3. “快”指针应该比“慢”指针快多少步最稳妥？
        """
        # 请根据“快慢指针/套圈”思维模式在此完善代码
        pass

if __name__ == "__main__":
    # 创建带环链表用于测试: 3 -> 2 -> 0 -> -4 -> (back to 2)
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2 # 建立环

    sol = Solution()
    print(f"Test Has Cycle: {sol.hasCycle(node1)} (Expect: True)")
    
    # 创建无环链表: 1 -> 2
    node_a = ListNode(1)
    node_b = ListNode(2)
    node_a.next = node_b
    print(f"Test No Cycle: {sol.hasCycle(node_a)} (Expect: False)")
