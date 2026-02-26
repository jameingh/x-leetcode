from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        题目：26. 删除有序数组中的重复项
        思路引导：
        1. 数组是有序的，重复元素必然相邻。
        2. 慢指针是一个“管理员”，守住当前已排好的有效位置边界。
        3. 快指针是一个“探路者”，去前面寻找与管理员位置不一样的“新鲜面孔”。
        """
        # 请根据“快慢指针/坑位管理”思维模式在此完善代码
        pass

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
