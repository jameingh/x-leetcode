from typing import Optional

# 定义二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        题目：104. 二叉树的最大深度
        
        🧠 大脑模拟引导（“部门汇报”模型）：
        1. 你的身份：你是当前节点的主管。
        2. 你的任务：汇报以你为根的这棵树有多深。
        3. 汇报逻辑：
           - 问左下属：你那边最深是多少？(`maxDepth(root.left)`)
           - 问右下属：你那边最深是多少？(`maxDepth(root.right)`)
           - 汇总向上级汇报：由于各部门是并行的，取两边最深的那个，加上你自己这一层。
             即：1 + max(左边深度, 右边深度)
        4. 边界条件（撤退时刻）：如果你发现自己是空节点（手下没人了），汇报 0。
        """
        # 请根据“主管汇报/递归汇总”思维模型在此完善代码
        pass

if __name__ == "__main__":
    sol = Solution()
    
    # 构建测试树: [3, 9, 20, None, None, 15, 7]
    #      3
    #     / \
    #    9  20
    #      /  \
    #     15   7
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    res = sol.maxDepth(root)
    print(f"Test 1: {res} (Expect: 3)")
    
    # 测试用例 2: 空树
    print(f"Test 2: {sol.maxDepth(None)} (Expect: 0)")
