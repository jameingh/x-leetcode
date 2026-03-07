# 199. 二叉树的右视图 (Binary Tree Right Side View)
# https://leetcode.cn/problems/binary-tree-right-side-view/

from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        核心思维：利用 BFS 层序遍历（水波扩散），每一层我们只关心最后一个被水波触及的人。
        """
        if not root:
            return []
            
        # 1. 初始化队列与结果数组
        queue = deque([root])
        result = []
        
        # 2. 只要水波还在扩散
        while queue:
            # 3. 锁死当前这一层的人数
            level_size = len(queue)
            
            # 4. 横扫当前层
            for i in range(level_size):
                # 出队
                node = queue.popleft()
                
                # 💡 思考引导：
                # 在这一层的遍历中，我们不需要像 102 题那样把所有人都存下来。
                # 我们站在树的右边，实际上只能看到这一层的“最后一个人”。
                # 那么，当循环变量 i 走到什么值的时候，意味着我们遇到了这层的最后一个人？
                # 如果遇到了，请把它收集到 result 中！
                
                # [你的核心逻辑代码填在这里]
                pass
                
                # 5. 把下一层波纹（左右下属）推入队尾排队
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        return result

# ==========================================
# 测试用例
# ==========================================
if __name__ == "__main__":
    sol = Solution()
    
    # 测试 1: 常规树
    #       1            <--- 看 1
    #      / \
    #     2   3          <--- 看 3
    #      \   \
    #       5   4        <--- 看 4
    # 期望输出: [1, 3, 4]
    root1 = TreeNode(1)
    root1.left = TreeNode(2, None, TreeNode(5))
    root1.right = TreeNode(3, None, TreeNode(4))
    
    print(f"Test 1 - (Expected: [1, 3, 4]): {sol.rightSideView(root1)}")
    
    # 测试 2: 左边比右边长
    #       1            <--- 看 1
    #      / 
    #     2              <--- 看 2
    #    /
    #   4                <--- 看 4
    # 期望输出: [1, 2, 4]
    root2 = TreeNode(1, TreeNode(2, TreeNode(4)))
    print(f"Test 2 - (Expected: [1, 2, 4]): {sol.rightSideView(root2)}")
    
    # 测试 3: 空树
    print(f"Test 3 - (Expected: []): {sol.rightSideView(None)}")
