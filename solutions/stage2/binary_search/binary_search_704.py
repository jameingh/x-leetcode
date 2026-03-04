from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        题目：704. 二分查找
        
        🧠 大脑模拟引导（“排除法”）：
        1. 搜地基：数组已经是有序的了，这是二分的金标准。
        2. 选中间：mid = (left + right) // 2。
        3. 做抉择：
           - 如果 mid 的值正好是目标：恭喜，直接返回下标。
           - 如果 mid 的值小了：说明目标在右边，左半边（包括 mid）都没戏了，left 移动到 mid + 1。
           - 如果 mid 的值大了：说明目标在左边，右半边（包括 mid）都没戏了，right 移动到 mid - 1。
        4. 结算：当 left 超过 right 时，说明翻遍了也没找着，返回 -1。
        """
        # 请根据“二分搜索/一刀两断”思维模型在此完善代码
        pass

if __name__ == "__main__":
    sol = Solution()
    
    # 测试用例 1: 目标在中间
    nums1 = [-1, 0, 3, 5, 9, 12]
    target1 = 9
    res1 = sol.search(nums1, target1)
    print(f"Test 1: target={target1} -> index={res1} (Expect: 4)")
    
    # 测试用例 2: 目标不在数组中
    nums2 = [-1, 0, 3, 5, 9, 12]
    target2 = 2
    res2 = sol.search(nums2, target2)
    print(f"Test 2: target={target2} -> index={res2} (Expect: -1)")
