from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        题目：167. 两数之和 II - 输入有序数组
        思路引导：
        1. 数组是升序排列的。
        2. 初始指针应放在哪个极端？
        3. 如果当前和 > 目标值，说明结果太大了，应该移动哪个指针来缩小和？
        """
        # 请根据“对撞指针”思维模式在此完善代码
        left = 0
        right = len(numbers) - 1
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1,right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return []

if __name__ == "__main__":
    sol = Solution()
    # 测试用例 1
    test1 = sol.twoSum([2, 7, 11, 15], 9)
    print(f"Test 1: {test1} (Expect: [1, 2])")
    # 测试用例 2
    test2 = sol.twoSum([2, 3, 4], 6)
    print(f"Test 2: {test2} (Expect: [1, 3])")
    # 测试用例 3
    test3 = sol.twoSum([-1, 0], -1)
    print(f"Test 3: {test3} (Expect: [1, 2])")