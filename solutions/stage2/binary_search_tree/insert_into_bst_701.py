# 701. 二叉搜索树中的插入操作 (Insert into a Binary Search Tree)
# https://leetcode.cn/problems/insert-into-a-binary-search-tree/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        核心思维：在 BST 中，“插入”动作就是一次必然失败的“搜索”！
        你只要假装去搜索这个值，走到无路可走（碰到 None）的时候，那个空位就是它该安家的地方。
        """
        
        # 1. 终止条件：走到空位了。这里就是要“建房子”的地方。
        # 返回一个包含新值的新节点。
        pass
            
        # 2. 单边向左下探：如果 val 比当前节点小，说明它该去左边找空位
        # 注意：你需要把当前节点的左指针，重新连到右侧返回的结果上！
        pass
        
        # 3. 单边向右下探：如果 val 比当前节点大，说明它该去右边找空位
        # 注意：你需要把当前节点的右指针，重新连到右侧返回的结果上！
        pass
        
        # 最后别忘了返回当前节点，保持树的链条不折断
        return root

# ==========================================
# 测试用例
# ==========================================
if __name__ == "__main__":
    sol = Solution()
    
    # 辅助函数：中序打印，用于验证结果是不是有序的
    def print_inorder(node):
        return print_inorder(node.left) + [node.val] + print_inorder(node.right) if node else []

    # 测试 1: 插入 5
    #       4
    #      / \
    #     2   7
    #    / \
    #   1   3
    root1 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
    print(f"Test 1 - Before Insert: {print_inorder(root1)}")
    root1 = sol.insertIntoBST(root1, 5)
    print(f"Test 1 - After Insert 5: {print_inorder(root1)} (Should be 1, 2, 3, 4, 5, 7)\n")
    
    # 测试 2: 插入到空树
    root2 = None
    root2 = sol.insertIntoBST(root2, 5)
    print(f"Test 2 - Insert into Empty Tree: {print_inorder(root2)} (Should be 5)")
