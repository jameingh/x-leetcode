# 530. 二叉搜索树的最小绝对差 (Minimum Absolute Difference in BST)
# https://leetcode.cn/problems/minimum-absolute-difference-in-bst/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        """
        核心思维：BST 的中序遍历 = 一维递增数组！
        找树里面任意两个节点的最小差值，如果有序了，最小差值一定在“相邻”的两个节点之间！
        所以，我们只需要在“中序遍历”的过程中，不断计算当前节点和它“上一个节点”的距离就行了。
        """
        
        self.min_diff = float('inf')  # 记录全局最小差值
        self.prev = None              # 记录中序遍历时，“上一个访问的节点的值”
        
        def inorder(node):
            if not node:
                return
            
            # 1. 递归左边：去最左边，找最小的那些数字
            inorder(node.left)
            
            # 2. 中间处理逻辑：在这个时刻，拿当前节点的值 node.val 和上一个记录的值 self.prev 作比较
            # 然后把 self.prev 更新为当面节点的值，准备传给下一个节点
            # a. 为什么要有 if self.prev is not None 呢？
            # 答：因为在第一次进入这个函数的时候，self.prev 是 None，这时候我们还没有访问过任何节点，
            # 所以没有意义去计算差值。只有在访问了至少一个节点之后，我们才有意义去计算差值。
            # b. 还有，因为是 BST，所以 node.val 一定大于 self.prev，所以我们不需要用 abs() 来取绝对值。
            # c. 为什么不写成if self.prev:?
            # 答：因为if self.prev is not None仅仅、严格地检查 self.prev 这个变量是不是空对象（None）。
            # 只要你不是 None，哪怕你是数字 0，或者是负数，它都放行（认为是 True）。
            # 而 if self.prev: 则是检查 self.prev 的“布尔值”。在 Python 中，None 是 False，
            # 而任何非零数字（包括 0）都是 True。所以 if self.prev: 实际上是在检查“self.prev 是否为 0 或 None”。
            # 在本题中，节点的值可能是 0，所以我们必须使用 if self.prev is not None 来避免错误。
            if self.prev is not None:
                self.min_diff = min(self.min_diff, node.val - self.prev)
            self.prev = node.val
            
            # 3. 递归右边：左边和中间处理完了，去探索右边
            inorder(node.right)
            
        inorder(root)
        return self.min_diff

# ==========================================
# 测试用例
# ==========================================
if __name__ == "__main__":
    sol = Solution()
    
    # 测试 1
    #       4
    #      / \
    #     2   6
    #    / \
    #   1   3
    # 中序遍历顺序应当为：1, 2, 3, 4, 6
    # 相邻最小差值为 1
    node2 = TreeNode(2, TreeNode(1), TreeNode(3))
    root1 = TreeNode(4, node2, TreeNode(6))
    print(f"Test 1 - Min Diff (Expected: 1): {sol.getMinimumDifference(root1)}")
    
    # 测试 2
    #       1
    #        \
    #         5
    #        /
    #       3
    # 中序遍历顺序应当为：1, 3, 5
    # 相邻最小差值为 2
    node5 = TreeNode(5, TreeNode(3), None)
    root2 = TreeNode(1, None, node5)
    print(f"Test 2 - Min Diff (Expected: 2): {sol.getMinimumDifference(root2)}")
