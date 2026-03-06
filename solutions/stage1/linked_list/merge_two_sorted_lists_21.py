from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        题目：21. 合并两个有序链表
        
        🧠 大脑模拟引导（“挂钩与组装”）：
        1. 挂钩（核心）：创建一个 dummy 节点作为新链表的“固定挂钩”。
        2. 手工：创建一个 cur 指针指向这个挂钩，它负责在后面接新的节点。
        3. 选秀：比较 list1 和 list2 当前的节点，谁的值小，就把 cur.next 指向谁，并把对应的链表往后挪一步。
        4. 结算：无论谁被选中，cur 都要往后挪一步，守住新的末尾。
        5. 收尾：如果其中一条链表空了，直接把另一条剩下的部分“啪”地贴在 cur.next 上。
        6. 离场：返回 dummy.next（也就是挂钩后面接的第一个真正珠子）。
        """
        # 请根据“哑节点/组装逻辑”思维模型在此完善代码
        # 1. 挂钩（核心）：创建一个 dummy 节点作为新链表的“固定挂钩”。
        dummy = ListNode()
        # 2. 手工：创建一个 cur 指针指向这个挂钩，它负责在后面接新的节点。
        cur = dummy
        # 3. 选秀：比较 list1 和 list2 当前的节点，谁的值小，就把 cur.next 指向谁，并把对应的链表往后挪一步。
        while list1 and list2: # while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                # 谁小接谁
                cur.next = list1
                # 对应的链表往后挪一步
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            # 4. 结算：无论谁被选中，cur都要往后挪一步，守住新的末尾
            cur = cur.next
        # 5. 收尾：如果其中一条链表空了，直接把另一条剩下的部分“啪”地贴在 cur.next 上。
        if list1:
            cur.next = list1
        if list2:
            cur.next = list2
        # 6. 离场：返回 dummy.next（也就是挂钩后面接的第一个真正珠子）。
        return dummy.next

def print_list(head: Optional[ListNode]):
    res = []
    while head:
        res.append(str(head.val))
        head = head.next
    print(" -> ".join(res) + " -> None")

if __name__ == "__main__":
    # 用例 1: 1->2->4  和  1->3->4
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    
    sol = Solution()
    res = sol.mergeTwoLists(l1, l2)
    print("Merged:")
    print_list(res)
    # 预期输出: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> None
