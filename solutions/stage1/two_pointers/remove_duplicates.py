from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        题目：26. 删除有序数组中的重复项
        思路引导：
        1. 数组是有序的，重复元素必然相邻。
        2. 慢指针是一个“管理员”，守住当前已排好的有效位置边界。
        3. 快指针是一个“探路者”，去前面寻找与管理员位置不一样的“新鲜面孔”。

        slow从0开始，fast从1开始（为什么不从0开始？）
        当fast遇到与slow不同的元素时，slow右移一位，fast的值赋给slow
        最后返回slow+1（为什么不返回slow？）

        1、关于 fast 初始值：因为第一个元素 nums[0] 永远是我们要保留的。因为它是“第一张面孔”，没有任何东西可以与之重复。所以我们直接让 slow 守住它，让侦察兵从 1 开始往后找“不一样的面孔”即可。
        2、关于 return slow + 1：因为 slow 记录的是最后一个“不重复元素”的下标。数组长度 = 下标 + 1。比如 slow 停在下标 1，说明有 [0, 1] 两个坑位被填满了，长度就是 2。
        """
        # 请根据“快慢指针/坑位管理”思维模式在此完善代码
        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1

if __name__ == "__main__":
    sol = Solution()
    # 测试用例 1
    nums1 = [1, 1, 2]
    k1 = sol.removeDuplicates(nums1)
    print(f"Test 1: k={k1}, nums={nums1[:k1]} (Expect: k=2, nums=[1, 2])")
    # 测试用例 2
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k2 = sol.removeDuplicates(nums2)
    print(f"Test 2: k={k2}, nums={nums2[:k2]} (Expect: k=5, nums=[0, 1, 2, 3, 4])")
