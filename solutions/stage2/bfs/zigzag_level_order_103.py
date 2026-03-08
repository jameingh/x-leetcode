# 103. 二叉树的锯齿形层序遍历 (Binary Tree Zigzag Level Order Traversal)
# https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/

from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        核心思维：在 BFS 水波扩散的基础模板上，增加一个“方向开关”（状态变量）。
        每遍历完一层，就把开关拨反一次。根据开关的状态，决定要不要把这一层的波纹反转一下再收集。
        """
        if not root:
            return []
            
        queue = deque([root])
        result = []
        
        # 💡 思考引导：
        # 我们需要一个变量来记住当前这一层是“从左到右”还是“从右到左”。
        # 初始第一层（根节点这层）是从左到右的，所以我们可以设定一个布尔变量：
        is_left_to_right = True
        
        while queue:
            level_size = len(queue)
            current_level_values = []
            
            for _ in range(level_size):
                node = queue.popleft()
                current_level_values.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            # 💡 思考引导：
            # 此时 `current_level_values` 里装的是按照正常从左到右顺序收集的节点值。
            # 如果当前状态 is_left_to_right 是 False，也就是规定我们要“从右到左”看，
            # 你该对 current_level_values 做什么处理，再把它放进 result 里？
            
            # [你的核心逻辑代码填在这里]
            
            
            # 操作完别忘了：一层的业务办完了，下一层必须掉头！
            # 请反转 is_left_to_right 的状态
            
            
        return result

# ==========================================
# 测试用例
# ==========================================
if __name__ == "__main__":
    sol = Solution()
    
    # 测试 1: 常规树
    #       3
    #      / \
    #     9  20
    #        /  \
    #       15   7
    # 第一层 L->R: [3]
    # 第二层 R->L: [20, 9] (正常出队是 9, 20，反转就是 20, 9)
    # 第三层 L->R: [15, 7]
    # 期望输出: [[3], [20, 9], [15, 7]]
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20, TreeNode(15), TreeNode(7))
    
    print(f"Test 1 - (Expected: [[3], [20, 9], [15, 7]]): {sol.zigzagLevelOrder(root1)}")
    
    # 测试 2: 只有一根独苗
    root2 = TreeNode(1)
    print(f"Test 2 - (Expected: [[1]]): {sol.zigzagLevelOrder(root2)}")
    
    # 测试 3: 空树
    print(f"Test 3 - (Expected: []): {sol.zigzagLevelOrder(None)}")
