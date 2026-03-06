from typing import Optional

# 定义二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        """
        题目：222. 完全二叉树的节点个数 (Count Complete Tree Nodes)
        
        🧠 大脑模拟引导（“部门人数大普查”模型）：
        1. 你的身份：你是当前节点的主管。
        2. 你的任务：统计以你为首的整个部门（树）一共有多少人。
        3. 汇报逻辑：
           - 问左手下：“你那边一共带了多少人？” (`self.countNodes(root.left)`)
           - 问右手下：“你那边一共带了多少人？” (`self.countNodes(root.right)`)
           - 汇总汇报：总人数 = 左手下的人数 + 右手下的人数 + 你自己(1)。
        4. 撤退条件：如果你是空节点，汇报 0 人。
        
        💡 进阶思考：这和计算“最大深度”有什么异曲同工之妙？
        """
        # 请根据“主管汇总”思维模型在此完善代码
        # 终止条件：空节点
        if not root:
            return 0
        # 递归调用：左路或者右路
        return self.countNodes(root.left) + self.countNodes(root.right) + 1

if __name__ == "__main__":
    sol = Solution()
    
    # 构建测试树: [1, 2, 3, 4, 5, 6]
    #      1
    #    /   \
    #   2     3
    #  / \   / 
    # 4   5 6
    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(4), TreeNode(5))
    root.right = TreeNode(3, TreeNode(6), None)
    
    print(f"Test 1: {sol.countNodes(root)} (Expect: 6)")
    
    # 测试用例 2: 空树
    print(f"Test 2: {sol.countNodes(None)} (Expect: 0)")
