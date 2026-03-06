# 700. 二叉搜索树中的搜索 (Search in a Binary Search Tree)
# https://leetcode.cn/problems/search-in-a-binary-search-tree/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        核心思维：利用 BST 的内置“导航系统”。
        你不需要遍历整棵树，只需要像用字典查字一样去比对和排除。
        """
        # 1. 终止条件：什么时候停下来？（找到了，或者彻底找不到了）
        # 如果当前节点为空，说明已经走到了树的尽头，没有找到目标值
        if not root:
            return None
        # 如果当前节点的值就是目标值，说明找到了，返回当前节点
        if root.val == val:
            return root

        # 2. 单边向左下探：如果目标值小于当前节点的值，该怎么办？
        # 如果目标值小于当前节点的值，说明目标值在左子树中
        if val < root.val:
            return self.searchBST(root.left, val)
        
        # 3. 单边向右下探：如果目标值大于当前节点的值，该怎么办？
        # 如果目标值大于当前节点的值，说明目标值在右子树中
        if val > root.val:
            return self.searchBST(root.right, val)

# ==========================================
# 测试用例
# ==========================================
if __name__ == "__main__":
    # 构造一棵 BST:
    #       4
    #      / \
    #     2   7
    #    / \
    #   1   3
    node1 = TreeNode(1)
    node3 = TreeNode(3)
    node2 = TreeNode(2, node1, node3)
    node7 = TreeNode(7)
    root = TreeNode(4, node2, node7)
    
    sol = Solution()
    
    # 测试 1: 寻找节点值为 2 (应该返回 2 这个节点的对象，即子树 2-1-3)
    res1 = sol.searchBST(root, 2)
    print(f"Test 1 - Search 2 (Expected: 2): {res1.val if res1 else 'None'}")
    
    # 测试 2: 寻找节点值为 5 (不存在，应该返回 None)
    res2 = sol.searchBST(root, 5)
    print(f"Test 2 - Search 5 (Expected: None): {res2.val if res2 else 'None'}")
