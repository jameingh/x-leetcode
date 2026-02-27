from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        题目：142. 环形链表 II (找到环的起点)
        思路引导：
        1. **第一步：检测环**。依然使用快慢指针，直到它们相遇。
        2. **第二步：寻找起点**。当快慢指针在环内某处相遇时，
           有一个数学上的巧合：此时从“链表头部”出发一个指针，
           从“相遇点”同时出发一个指针，它们以同样的速度前进，
           最终一定会在“环的起点”撞个满怀。
        3. 如果快慢指针遇到了 None，说明没有环，直接返回 None。
        
        第一步（相遇）：依然让快慢指针出发，在环内某个点相遇。
        第二步（寻根）：当它们相遇的那一刻，我们把其中一个指针（比如 slow）放回链表头部，而另一个（fast）留在原地（相遇点）。
        大结局：现在，让这两个指针都以同样的速度（每次一步）往前走。它们再次撞见的地方，绝对就是环的起点。
        """
        # 请根据“双指针/数论巧合”思维模式在此完善代码
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
        if not fast or not fast.next:
            return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow

if __name__ == "__main__":
    # 构造测试用例: 3 -> 2 -> 0 -> -4 -> (back to 2)
    n1, n2, n3, n4 = ListNode(3), ListNode(2), ListNode(0), ListNode(-4)
    n1.next, n2.next, n3.next, n4.next = n2, n3, n4, n2
    
    sol = Solution()
    res = sol.detectCycle(n1)
    print(f"Test Cycle Start: {res.val if res else None} (Expect: 2)")
    
    # 构造无环测试
    na, nb = ListNode(1), ListNode(2)
    na.next = nb
    res2 = sol.detectCycle(na)
    print(f"Test No Cycle: {res2} (Expect: None)")
