# 98. 验证二叉搜索树 (Validate Binary Search Tree)
# https://leetcode.cn/problems/validate-binary-search-tree/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        核心思维：区间查岗（带着尚方宝剑下发）。
        不能只看父子关系，要看当前节点是否符合“祖先们”定下的规矩！
        """
        
        # 内部定义一个带“区间约束”的辅助递归函数
        def validate(node, min_val, max_val):
            # 1. 终止条件：查到了空节点，说明这条路没发现违规的。返回 True。
            if not node:
                return True
            
            # 2. 查岗动作：当前节点的数值，有没有越界？（<= 最小值，或者 >= 最大值都是违规）
            if node.val <= min_val or node.val >= max_val:
                return False
            
            # 3. 约束下放：
            #    去查左子树吧！记住，最大值不能超过我当前的 val！
            #    去查右子树吧！记住，最小值不能低于我当前的 val！
            return validate(node.left, min_val, node.val) and validate(node.right, node.val, max_val)
            
        # 初始召唤：根节点没有任何约束，大小可以无限上天下地 (float('-inf'), float('inf'))
        return validate(root, float('-inf'), float('inf'))

# ==========================================
# 测试用例
# ==========================================
if __name__ == "__main__":
    sol = Solution()
    
    # 测试 1: 正常的 BST
    #       2
    #      / \
    #     1   3
    root1 = TreeNode(2, TreeNode(1), TreeNode(3))
    print(f"Test 1 - Valid BST (Expected: True): {sol.isValidBST(root1)}")
    
    # 测试 2: 经典陷阱！右子树的所有节点必须 大于 根节点
    #       5
    #      / \
    #     1   4    <-- 4 虽然小于它的父节点 5的右边，但 4 比根节点 5 小！！所以不合法
    #        / \
    #       3   6
    node4 = TreeNode(4, TreeNode(3), TreeNode(6))
    root2 = TreeNode(5, TreeNode(1), node4)
    print(f"Test 2 - Invalid BST (Expected: False): {sol.isValidBST(root2)}")
