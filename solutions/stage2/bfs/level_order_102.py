# 102. 二叉树的层序遍历 (Binary Tree Level Order Traversal)
# https://leetcode.cn/problems/binary-tree-level-order-traversal/

from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        核心思维：利用队列 (Queue) 模拟水波纹的逐层扩散。
        外层 while 荡起一圈水波，内层 for 循环处理这一圈的所有节点，并将他们的下一代引导至队尾。
        """
        if not root:
            return []
            
        # 1. 初始化队列，并将“第一圈波纹”（根节点）放进去
        queue = deque([root])
        result = []
        
        # 2. 外层循环：只要队列不空，说明还有波纹在扩散
        while queue:
            # 3. 核心堡垒：提前锁死当前这一层有多少个节点！
            # 必须用一个变量先接住 len(queue)，千万不能在 for 循环里动态去读 len(queue)
            level_size = len(queue)
            
            # 用来装这一层所有节点值的临时小数组
            current_level_values = []
            
            # 4. 内层循环：横扫当前层的所有人
            # 出队 -> 把值放进小数组 -> 如果有下属，把下属推进队尾排着
            for _ in range(level_size):
                node = queue.popleft()
                current_level_values.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # 5. 横扫完毕，把当前层的小数组装进最终结果大数组
            result.append(current_level_values)
            
        # 返回最终大数组
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
    # 期望输出: [[3], [9, 20], [15, 7]]
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20, TreeNode(15), TreeNode(7))
    
    print(f"Test 1 - (Expected: [[3], [9, 20], [15, 7]]): {sol.levelOrder(root1)}")
    
    # 测试 2: 只有一根独苗
    root2 = TreeNode(1)
    print(f"Test 2 - (Expected: [[1]]): {sol.levelOrder(root2)}")
    
    # 测试 3: 空树
    print(f"Test 3 - (Expected: []): {sol.levelOrder(None)}")
