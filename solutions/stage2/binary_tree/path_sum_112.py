from typing import Optional

# 定义二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        题目：112. 路径总和 (Path Sum)
        
        🧠 大脑模拟引导（“携带余额下探”模型）：
        1. 你的身份：你是当前节点的主管，手里拿着一份“待开销额度” (`targetSum`)。
        2. 你的动作：
           - 你进驻这个节点，意味着这一层的账单归你了。
           - 额度更新：你手里的余额变成了 `targetSum - root.val`。
        3. 结算时刻（叶子节点）：
           - 如果你发现自己是叶子节点（左右手下都没人了）：
             - 关键审计：现在的余额是否正好等于 0？如果是，说明这条路走通了！
        4. 下放任务：
           - 如果不是叶子节点，你就把“剩下的余额”交给分身。
           - 只要【左路】或者【右路】有一个人汇报“走通了”，你就可以向上级汇报“通了”！
        5. 撤退条件：如果是空节点，永远返回 False。
        """
        # 请根据“余额扣减”思维模型在此完善代码
        # 终止条件：空节点
        if not root:
            return False
        
        # 叶子节点：余额是否为 0
        if not root.left and not root.right:
            return targetSum == root.val
        
        # 递归调用：左路或者右路
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

if __name__ == "__main__":
    sol = Solution()
    
    # 构建测试树: [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
    # targetSum = 22
    # 符合条件的路径: 5 -> 4 -> 11 -> 2 (和为 22)
    node11 = TreeNode(11, TreeNode(7), TreeNode(2))
    node4_left = TreeNode(4, node11, None)
    node8 = TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1)))
    root = TreeNode(5, node4_left, node8)
    
    print(f"Test 1: {sol.hasPathSum(root, 22)} (Expect: True)")
    print(f"Test 2: {sol.hasPathSum(root, 5)} (Expect: False)")
