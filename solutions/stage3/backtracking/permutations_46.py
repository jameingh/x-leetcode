# 46. 全排列 (Permutations)
# https://leetcode.cn/problems/permutations/

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        核心思维：在决策树上通过“做选择 -> 递归 -> 撤销选择”穷举解空间。
        
        与 77 题（组合）的区别：
        - 组合：[1, 2] 和 [2, 1] 是同一个东西，所以需要 startIndex 只能往后看。
        - 排列：[1, 2] 和 [2, 1] 是不同的！所以每一层都要从头看，只要这个数还没被用过就行。
        
        思考引导：
        1. 路径 (Path)：当前排列已经收录了哪些数？
        2. 选择列表：nums 中还没有被选进 path 的数。
        3. 状态标记：我们需要一种方式（比如一个 set 或 bool 数组）快速知道某个数是否“已在阵中”。
        """
        result = []
        path = []
        # 用来标记已经选过的数字
        used = [False] * len(nums)

        def backtracking():
            # 💡 终止条件：当 path 长度和 nums 相等，说明一个排列完成了
            if len(path) == len(nums):
                result.append(path[:])
                return

            for i in range(len(nums)):
                # 💡 核心思考：
                # 如果这个数字已经被用过了，该怎么办？（看 used[i]）
                if used[i]:
                    continue
                
                # 1. 做选择：标记为已用，并加入路径
                used[i] = True
                path.append(nums[i])
                
                # 2. 纵向深入：下一层决策树
                backtracking()
                
                # 3. 撤销选择：标记为未用，并从路径弹出
                # 💡 思考：如果不做这一步，下一轮循环选别的数字时会发生什么？
                path.pop()
                used[i] = False

        backtracking()
        return result

# ==========================================
# 大脑模拟测试
# ==========================================
if __name__ == "__main__":
    sol = Solution()
    
    # 测试 1: nums = [1, 2, 3]
    # 期望输出包含: [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]
    print(f"Test 1 - nums=[1, 2, 3]: \n{sol.permute([1, 2, 3])}")
    
    # 测试 2: nums = [0, 1]
    print(f"Test 2 - nums=[0, 1]: \n{sol.permute([0, 1])}")
