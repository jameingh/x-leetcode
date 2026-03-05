from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        题目：35. 搜索插入位置
        
        🧠 大脑模拟引导（“平滑落地”）：
        1. 基础逻辑：这依然是一个典型的二分搜索。数组有序，查找目标。
        2. 核心差异：如果找到了 target，直接返回下标（跟 704 一样）。
        3. 关键思考：**如果没找到，该返回什么呢？**
           - 想象二分搜索结束的那个瞬间。当 `while left <= right` 循环结束时，`left` 刚好指向了第一个“大于” target 的元素位置。
           - 比如在 [1, 3] 中找 2：
             - 第一轮：mid 指向 1 (值是 1)，1 < 2，所以 left 变成 mid + 1 = 1。
             - 第二轮：mid 指向 1 (值是 3)，3 > 2，所以 right 变成 mid - 1 = 0。
             - 结束：此时 left = 1，正是不满足循环条件退出的时刻，而这个 1 恰恰就是 2 应该插入的位置。
        """
        # 请根据“二分搜索/边界降落”思维模型在此完善代码
        # 关键点：
        # 1. 循环条件：left <= right
        # 2. 退出条件：left > right
        # 3. 返回值：left
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

if __name__ == "__main__":
    sol = Solution()
    
    # 测试用例 1: 目标在数组中
    print(f"Test 1: {sol.searchInsert([1, 3, 5, 6], 5)} (Expect: 2)")
    
    # 测试用例 2: 目标不在数组中，应插入中间
    print(f"Test 2: {sol.searchInsert([1, 3, 5, 6], 2)} (Expect: 1)")
    
    # 测试用例 3: 目标在数组末尾之后
    print(f"Test 3: {sol.searchInsert([1, 3, 5, 6], 7)} (Expect: 4)")
    
    # 测试用例 4: 目标在数组开头之前
    print(f"Test 4: {sol.searchInsert([1, 3, 5, 6], 0)} (Expect: 0)")
