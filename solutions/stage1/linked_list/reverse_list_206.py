from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        题目：206. 反转链表
        
        🧠 大脑模拟引导（“缝合手术”）：
        1. 准备：你需要两个“镊子”——一个 pre (指向前面已缝好的部分，初始为空)，一个 cur (指向当前正在缝的节点)。
        2. 救命（核心）：在断开 cur 的连接之前，**必须**先拿个变量 tmp 拽住它的下一个节点（tmp = cur.next）。
        3. 转向：让 cur 指向它的“前任” (cur.next = pre)。
        4. 接力：整体向后挪一步。pre 走到 cur 的位置，cur 走到 tmp 的位置。
        5. 循环：直到 cur 为空，此时 pre 就是原来的末尾，也就是现在的头。
        """
        # 请根据“链表手术/三指针”思维模型在此完善代码
        # 初始化前指针
        pre = None
        # 初始化当前指针
        cur = head
        # 循环直到当前指针为空
        while cur:
            # 救命：先拿个变量 tmp 拽住它的下一个节点
            tmp = cur.next
            # 转向：让 cur 指向它的“前任”
            cur.next = pre
            # 接力：整体向后挪一步
            pre = cur
            cur = tmp
        # 返回反转后的链表头
        return pre

def print_list(head: Optional[ListNode]):
    """辅助函数：打印链表内容以验证结果"""
    res = []
    while head:
        res.append(str(head.val))
        head = head.next
    print(" -> ".join(res) + " -> None")

if __name__ == "__main__":
    # 构造测试用例: 1 -> 2 -> 3 -> 4 -> 5 -> None
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    
    print("Original:")
    print_list(head)
    
    sol = Solution()
    rev_head = sol.reverseList(head)
    
    print("Reversed:")
    print_list(rev_head)
    # 预期输出: 5 -> 4 -> 3 -> 2 -> 1 -> None
