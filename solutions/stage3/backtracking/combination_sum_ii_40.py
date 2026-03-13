# 40. 组合总和 II (Combination Sum II)
# https://leetcode.cn/problems/combination-sum-ii/

from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        核心挑战：数组中有重复数字，但结果集不能有重复组合。
        
        剪枝精髓：树层去重。
        1. 首先必须排序！这样重复的数字才会挨在一起。
        2. 思考：如果我们在“同一层”选妃，刚选了一个 1，发现后面紧接着又是一个 1，
           如果我们选了第二个 1 开启的分支，绝对会和第一个 1 开启的分支产生重复。
        """
        result = []
        path = []
        
        # 💡 第一步：排序是去重的前提
        candidates.sort()

        def backtracking(start_index, current_sum):
            # 终止条件 1：中头奖了
            if current_sum == target:
                result.append(path[:])
                return
            
            # 终止条件 2：超重了（这本身就是一种基础剪枝）
            if current_sum > target:
                return

            for i in range(start_index, len(candidates)):
                # 💡 核心剪枝逻辑：树层去重
                # 如果当前数和前一个数相同，且我们处于“同一层”循环（i > start_index）
                # 说明这个数字开启的分支我们已经搜过了，直接跳过。
                
                # [请在此处填入去重剪枝逻辑]
                
                
                # [请在此处填入标准的做选择、递归、回溯逻辑]
                # 提示：current_sum 也要记得更新哦
                pass

        backtracking(0, 0)
        return result

# ==========================================
# 测试用例
# ==========================================
if __name__ == "__main__":
    sol = Solution()
    
    # 测试 1: 重复数字去重
    # 期望输出包含: [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
    print(f"Test 1 - [10,1,2,7,6,1,5], target=8: \n{sol.combinationSum2([10,1,2,7,6,1,5], 8)}")
    
    # 测试 2: 期望输出: [[1, 2, 2], [5]]
    print(f"Test 2 - [2,5,2,1,2], target=5: \n{sol.combinationSum2([2,5,2,1,2], 5)}")
