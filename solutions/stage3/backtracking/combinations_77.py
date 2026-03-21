# 77. 组合 (Combinations)
# https://leetcode.cn/problems/combinations/

from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        核心模型：决策树。
        从 [1, n] 的集合中，依次选出一个数，直到路径长度达到 k。
        
        思考引导：
        1. 路径 (Path)：当前已经选了哪些数？
        2. 选择列表：当前还可以选哪些数？为了防止 [1, 2] 和 [2, 1] 这种重复组合，
           我们需要一个 `startIndex`，保证每次只能往后选。
        3. 终止条件：路径长度 == k。
        """
        # 存放最终结果
        result = []
        # 存放当前路径
        path = []

        # 回溯函数
        def backtracking(start_index):
            # 💡 终止条件：什么时候说明这一条路走通了？
            # 当路径长度等于 k 时，说明找到了一个组合
            if len(path) == k:
                result.append(path[:])
                return

            # 💡 横向遍历：从 start_index 开始
            # 【核心剪枝逻辑】：如果剩余的可选元素数量不够凑齐 k 个，就没必要再搜索了。
            # 1. 还需要几个数？ needed = k - len(path)
            # 2. 至多从哪开始？ n - (k - len(path)) + 1
            # 3. range 停止位（左闭右开）：n - (k - len(path)) + 2
            for i in range(start_index, n - (k - len(path)) + 2):
                # 1. 做决定
                path.append(i)
                # 2. 纵向深入
                backtracking(i + 1)
                # 3. 撤销决定
                path.pop()

        # 从 1 开始回溯
        backtracking(1)
        return result

# ==========================================
# 大脑模拟测试
# ==========================================
if __name__ == "__main__":
    sol = Solution()
    
    # 测试 1: n=4, k=2
    # 期望输出: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    print(f"Test 1 - n=4, k=2: \n{sol.combine(4, 2)}")
    
    # 测试 2: n=1, k=1
    # 期望输出: [[1]]
    print(f"Test 2 - n=1, k=1: \n{sol.combine(1, 1)}")
