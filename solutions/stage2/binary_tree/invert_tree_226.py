from typing import Optional

# 定义二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def __repr__(self):
        # 辅助打印，例如：4(2(1, 3), 7(6, 9))
        left_str = str(self.left) if self.left else "."
        right_str = str(self.right) if self.right else "."
        if left_str == "." and right_str == ".":
            return str(self.val)
        return f"{self.val}({left_str}, {right_str})"

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        题目：226. 翻转二叉树 (Invert Binary Tree)
        
        🧠 大脑模拟引导（“主管下命令”模型）：
        1. 你的身份：你是当前节点的主管。
        2. 你的任务：把你自己的左下属和右下属的位置**对调**（不仅是名字，而是整个部门对换）。
        3. 下放兵权（传达命令）：
           - 光你自己换了没用，底下的基层没换。你还得对他们下命令。
           - 命令左下属：“喂，把你手底下的人翻转一下！” -> `self.invertTree(root.left)`
           - 命令右下属：“你也把你底下的人翻转一下！” -> `self.invertTree(root.right)`
           - 💡 小思考：你是“先调换部门再下命令”，还是“先下完命令再调换他们的位置”？（剧透：都可以，这就是前序遍历和后序遍历的区别！）
        4. 边界条件（撤退时刻）：如果你手下没人（`not root`），这道命令就传不下去了，直接返回 None 结束命令。
        """
        # 请根据“主管下命令”的思维模型在此完善代码
        pass

if __name__ == "__main__":
    sol = Solution()
    
    # 构建测试树: [4, 2, 7, 1, 3, 6, 9]
    #      4
    #    /   \
    #   2     7
    #  / \   / \
    # 1   3 6   9
    root = TreeNode(4)
    root.left = TreeNode(2, TreeNode(1), TreeNode(3))
    root.right = TreeNode(7, TreeNode(6), TreeNode(9))
    
    print("翻转前:", root)
    res = sol.invertTree(root)
    print("翻转后:", res)
    # Expect: 4(7(9, 6), 2(3, 1))
