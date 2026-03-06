from typing import Optional

# 定义二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        题目：101. 对称二叉树 (Symmetric Tree)
        
        🧠 大脑模拟引导（“双分身同步对比”模型）：
        1. 核心挑战：你要判断一棵树是否是自己的“镜像”。
        2. 策略转换：判断一棵树对称，等价于判断它的【左子树】和【右子树】是镜像。
        3. 双分身逻辑 (check 函数)：
           - 你现在有两个探险员：分身 A 站在左树上，分身 B 站在右树上。
           - 他们必须同步移动：
             - 当 A 往【左】跨一步时，B 必须往【右】跨一步（镜像对称）。
             - 当 A 往【右】跨一步时，B 必须往【左】跨一步。
           - 每跨一步，他们都要对讲：“喂，你那里的值跟我这里一样吗？”
        4. 撤退条件（Base Case）：
           - 如果两个分身都走到了空地（None）：说明之前一直都匹配，返回 True。
           - 如果只有一个分身走到了空地，或者两人脚下的值不一样：这门亲事黄了，返回 False。
        """
        if not root:
            return True
        return self.check(root.left, root.right)

    def check(self, node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
        # 请根据“双分身同步探测”思维模型在此完善代码
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        if node1.val != node2.val:
            return False
        return self.check(node1.left, node2.right) and self.check(node1.right, node2.left)

if __name__ == "__main__":
    sol = Solution()
    
    # 构建对称树: [1, 2, 2, 3, 4, 4, 3]
    #      1
    #    /   \
    #   2     2
    #  / \   / \
    # 3   4 4   3
    root1 = TreeNode(1)
    root1.left = TreeNode(2, TreeNode(3), TreeNode(4))
    root1.right = TreeNode(2, TreeNode(4), TreeNode(3))
    
    print(f"Test 1 (Symmetric): {sol.isSymmetric(root1)} (Expect: True)")
    
    # 构建不对称树: [1, 2, 2, None, 3, None, 3]
    root2 = TreeNode(1)
    root2.left = TreeNode(2, None, TreeNode(3))
    root2.right = TreeNode(2, None, TreeNode(3))
    
    print(f"Test 2 (Asymmetric): {sol.isSymmetric(root2)} (Expect: False)")
