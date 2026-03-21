"""
90. 子集 II (Subsets II)

题目描述：
    给你一个整数数组 nums，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。
    解集不能包含重复的子集。返回的解集可以按任意顺序排列。
    
    示例：
    输入：nums = [1, 2, 2]
    输出：[[], [1], [1,2], [1,2,2], [2], [2,2]]

思维模型：
    【子集问题 + 树层去重】
    
    本题是 78. 子集 的进阶版。核心差异在于：
    1. 输入数组有重复元素（如 [1, 2, 2]）。
    2. 如果不加处理，会产生重复子集。例如第一个 2 选了 [1, 2]，第二个 2 也会选出 [1, 2]。
    
    【去重三部曲】
    1. 排序：去重的前提是有序，这样重复元素才会紧挨着。 `nums.sort()`
    2. 判断：在同一树层内（for 循环里），如果当前元素与前一个元素相同，则跳过。
    3. 逻辑：`if i > startIndex and nums[i] == nums[i-1]: continue`
    
    【决策树模拟 ([1, 2, 2])】
              []
           /  |  \
        [1]  [2]  [2] (← 树层重复！跳过)
        / \    \
     [1,2][1,2] [2,2]
       ↓
    (树层重复！跳过)

核心代码位置：
    - 在 backtrack 入口处记录 path。
    - for 循环内增加 `i > startIndex and nums[i] == nums[i-1]` 的判断。
"""

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        返回 nums 的所有可能子集（含重复处理）
        """
        result = []
        path = []
        
        # TODO 1: 排序是去重的第一步！
        nums.sort()
        n = len(nums)
        
        def backtrack(startIndex: int):
            # TODO 2: 记录当前子集
            result.append(path[:])
            
            for i in range(startIndex, n):
                # TODO 3: 树层去重逻辑
                # 提示：如果当前 i 不是 startIndex，且当前元素和前一个相同，则 continue
                if i > startIndex and nums[i] == nums[i-1]:
                    continue
                
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()
        
        backtrack(0)
        return result


# ============ 测试用例 ============
if __name__ == "__main__":
    sol = Solution()
    
    # 测试 1: 含重复元素
    nums1 = [1, 2, 2]
    result1 = sol.subsetsWithDup(nums1)
    print(f"输入: {nums1}")
    print(f"输出: {result1}")
    print(f"子集数量: {len(result1)} (预期为 6)")
    # 验证是否包含重复项
    unique_results = [tuple(sorted(x)) for x in result1]
    is_unique = len(set(unique_results)) == len(result1)
    print(f"结果是否唯一: {is_unique}")
    print()
    
    # 测试 2: 全重复
    nums2 = [4, 4, 4]
    result2 = sol.subsetsWithDup(nums2)
    print(f"输入: {nums2}")
    print(f"输出: {result2}")
    print(f"子集数量: {len(result2)} (期望: [[], [4], [4,4], [4,4,4]] 共 4 个)")
