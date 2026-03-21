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
            
            # start_index 是当前层的起始索引
            for i in range(start_index, len(candidates)):
                # 💡 强力剪枝：如果当前数字加上去已经超重，后面的数字更大，肯定也超重
                # 直接退出循环 (break)，不再浪费时间搜索。
                if current_sum + candidates[i] > target:
                    break

                # 💡 核心剪枝逻辑：树层去重
                # 如果当前数和前一个数相同，且我们处于“同一层”循环（i > start_index）
                if i > start_index and candidates[i] == candidates[i-1]:
                    continue
                
                # 标准的做选择、递归、回溯逻辑
                path.append(candidates[i])
                current_sum += candidates[i]
                backtracking(i+1, current_sum)
                path.pop()
                current_sum -= candidates[i]

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
