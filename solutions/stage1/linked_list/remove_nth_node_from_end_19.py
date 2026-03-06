from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        题目：19. 删除链表的倒数第 N 个节点
        
        🧠 大脑模拟引导（“时间差位移”）：
        1. 挂钩（安全保障）：先造个 dummy 节点挂在 head 前面。这样即使删掉的是头节点，我们也能稳稳拿住 dummy.next。
        2. 快指针出发：让 fast 指针先从 dummy 往前跑 N 步。
        3. 同步竞速：现在让 slow 从 dummy 出发，和 fast 一起跑（速度一样）。
        4. 到达终点：当 fast 跑到链表最后一个节点时，由于它比 slow 领先了 N 步，
           此时 slow 刚好停在“倒数第 N 个”节点的【前一个】位置。
        5. 剪线（手术）：直接让 slow.next = slow.next.next，就把那个节点给切掉了。
        6. 离场：返回 dummy.next。
        """
        # 请根据“哑节点/快慢指针”思维模型在此完善代码
        # 1. 挂钩（安全保障）：先造个 dummy 节点挂在 head 前面。这样即使删掉的是头节点，我们也能稳稳拿住 dummy.next。
        dummy = ListNode()
        dummy.next = head
        # 2. 快指针出发：让 fast 指针先从 dummy 往前跑 N 步。
        fast = dummy
        slow = dummy
        for i in range(n):
            fast = fast.next
        # 3. 同步竞速：现在让 slow 从 dummy 出发，和 fast 一起跑（速度一样）。
        while fast.next:
            fast = fast.next
            slow = slow.next
        # 4. 到达终点：当 fast 跑到链表最后一个节点时，由于它比 slow 领先了 N 步，
        #    此时 slow 刚好停在“倒数第 N 个”节点的【前一个】位置。
        # 5. 剪线（手术）：直接让 slow.next = slow.next.next，就把那个节点给切掉了。
        slow.next = slow.next.next
        # 6. 离场：返回 dummy.next。
        return dummy.next

def print_list(head: Optional[ListNode]):
    res = []
    while head:
        res.append(str(head.val))
        head = head.next
    print(" -> ".join(res) + " -> None")

if __name__ == "__main__":
    # 用例 1: 1->2->3->4->5, n = 2
    head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    sol = Solution()
    print("Example 1 (n=2):")
    res1 = sol.removeNthFromEnd(head1, 2)
    print_list(res1) 
    # 预期输出: 1 -> 2 -> 3 -> 5 -> None

    # 用例 2: 1, n = 1
    head2 = ListNode(1)
    print("Example 2 (n=1):")
    res2 = sol.removeNthFromEnd(head2, 1)
    print_list(res2)
    # 预期输出: None
