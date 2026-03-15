"""
78. 子集 (Subsets)

题目描述：
    给你一个整数数组 nums（元素互不相同），返回所有可能的子集（幂集）。
    
    示例：
        输入：nums = [1, 2, 3]
        输出：[[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]

思维模型：
    【子集树 vs 组合树】
    
    77. 组合：只记录"叶子节点"（达到 k 个才记录）
    78. 子集：每个节点都是答案（包括根节点空集）
    
    决策树对比：
    
    组合树 (k=2)：                    子集树：
            []                            []          ← 空集也是答案！
           / | \                         / | \
         [1] [2] [3]                  [1] [2] [3]    ← 这些也是答案！
         /     \                       /  \   \
      [1,2]   [1,3]                [1,2][1,3] [2,3]  ← 这些也是答案！
                                         \
                                       [1,2,3]        ← 这个也是答案！
    
    【关键差异】
    - 组合问题：需要终止条件（长度达到 k）
    - 子集问题：不需要终止条件，每条路径都是有效子集
    
    【代码框架调整】
    1. 记录结果的时机：进入递归后立即记录（而不是等终止条件）
    2. 终止条件：可以省略，或仅用于边界检查
    3. startIndex：仍然需要，防止重复（如 [1,2] 和 [2,1]）

核心代码位置：
    - 在递归函数的"入口处"记录当前 path
    - for 循环的范围仍然是 [startIndex, n)
    - 递归调用传递 i + 1（不能回头选同一元素）
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        返回 nums 的所有可能子集
        
        思路：
            回溯法。与 77. 组合 相比：
            1. 不需要 k 参数，因为任意长度都有效
            2. 每次进入递归就记录 path（每个节点都是答案）
            3. 不需要复杂的终止条件
        """
        result = []
        path = []
        n = len(nums)
        
        def backtrack(startIndex: int):
            # TODO 1: 在这里记录当前子集
            # 提示：每个节点都是答案，所以进入递归就先记录
            # 记得用 path[:] 拍照存证！
            pass
            
            # TODO 2: 填写 for 循环
            # 提示：范围是 [startIndex, n)
            # 循环内：做选择 -> 递归 -> 撤销选择
            # 递归时传递 i + 1，表示不能回头
            pass
        
        backtrack(0)
        return result


# ============ 测试用例 ============
if __name__ == "__main__":
    sol = Solution()
    
    # 测试 1: 标准输入
    nums1 = [1, 2, 3]
    result1 = sol.subsets(nums1)
    print(f"输入: {nums1}")
    print(f"输出: {result1}")
    print(f"子集数量: {len(result1)} (应该是 2^3 = 8)")
    print()
    
    # 测试 2: 单元素
    nums2 = [5]
    result2 = sol.subsets(nums2)
    print(f"输入: {nums2}")
    print(f"输出: {result2}")
    print(f"子集数量: {len(result2)} (应该是 2^1 = 2)")
    print()
    
    # 测试 3: 空数组
    nums3 = []
    result3 = sol.subsets(nums3)
    print(f"输入: {nums3}")
    print(f"输出: {result3}")
    print(f"子集数量: {len(result3)} (应该是 2^0 = 1)")
    print()
    
    # 验证逻辑
    print("=== 验证 ===")
    print(f"测试 1 是否包含空集：[] in result1 = {[] in result1}")
    print(f"测试 1 是否包含全集：[1,2,3] in result1 = {[1,2,3] in result1}")
    print(f"测试 1 子集数量是否正确：len = {len(result1)}, 期望 = 8, 通过 = {len(result1) == 8}")
