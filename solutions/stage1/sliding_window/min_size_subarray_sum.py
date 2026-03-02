from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        题目：209. 长度最小的子数组
        
        🧠 大脑模拟引导（寻找“最短”）：
        1. 窗口扩张：right 指针不断向右移动，把数值加进“当前总和” (current_sum)。
        2. 触发收缩：一旦 current_sum >= target，说明我们找到了一个满足条件的窗口！
        3. 贪心优化：此时满足条件了，我们尝试把 left 指针向右移，看看踢掉左边的数后，剩下的窗口是否依然 >= target？
        4. 全局记录：在每一个“满足条件”的瞬间，记录下当前的窗口长度 (right - left + 1)，并保留那个最小值。
        
        注意：如果整个数组加起来都不到 target，应该返回 0。
        """
        # 请根据“滑动窗口/寻找最短”思维模型在此完善代码
        left = 0
        right = 0
        current_sum = 0
        # 记录最小长度，初始值设置一个很大的数正无穷
        min_length = float('inf')
        while right < len(nums):
            current_sum += nums[right]
            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1
            right += 1
        return min_length if min_length != float('inf') else 0

if __name__ == "__main__":
    sol = Solution()
    
    # 测试用例 1
    t1, n1 = 7, [2, 3, 1, 2, 4, 3]
    res1 = sol.minSubArrayLen(t1, n1)
    print(f"Test 1: target={t1}, nums={n1} -> {res1} (Expect: 2)")
    
    # 测试用例 2
    t2, n2 = 4, [1, 4, 4]
    res2 = sol.minSubArrayLen(t2, n2)
    print(f"Test 2: target={t2}, nums={n2} -> {res2} (Expect: 1)")
    
    # 测试用例 3
    t3, n3 = 11, [1, 1, 1, 1, 1, 1, 1, 1]
    res3 = sol.minSubArrayLen(t3, n3)
    print(f"Test 3: target={t3}, nums={n3} -> {res3} (Expect: 0)")
