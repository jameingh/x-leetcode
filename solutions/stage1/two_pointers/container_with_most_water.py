from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        题目：11. 盛最多水的容器
        思路引导：
        1. 容器的容量由“底（距离）”和“高（木桶效应，取较短者）”决定。
        2. 初始指针放两端，底是最长的。
        3. 为了寻找更高的高度来弥补底部的缩减，你应该移动“较长”的那根线还是“较短”的那根线？
        """
        # 请根据“对撞指针”思维模式在此完善代码
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            width = right - left
            h = min(height[left], height[right])
            max_area = max(max_area, width * h)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area

if __name__ == "__main__":
    sol = Solution()
    # 测试用例 1
    test1 = sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
    print(f"Test 1: {test1} (Expect: 49)")
    # 测试用例 2
    test2 = sol.maxArea([1, 1])
    print(f"Test 2: {test2} (Expect: 1)")
