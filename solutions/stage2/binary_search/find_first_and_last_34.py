from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        题目：34. 在排序数组中查找元素的第一个和最后一个位置

        🧠 大脑模拟引导（“双重定界”）：
        1. 挑战：普通的二分只能帮你找到“其中一个”目标，但目标可能有多个且连在一起。
        2. 策略：我们需要做两次二分，或者在一个二分里通过微调逻辑来寻找“左边界”和“右边界”。
        
        🔍 寻找左边界 (First Position)：
        - 当 nums[mid] == target 时，别急着返回！
        - 既然要找最左边的，说明右边（包括当前 mid）都没用了，我们应该锁定左半边：right = mid - 1。
        - 这样，指针会不断向左“挤压”，直到停在第一个 target 的位置。
        
        🔍 寻找右边界 (Last Position)：
        - 同理，当 nums[mid] == target 时，锁定右半边：left = mid + 1。
        
        提示：你可以写一个辅助函数 `findBound(isLeft)` 来复用二分逻辑。
        """
        # 第二步：在这里组合结果
        # 1. 调用 self.findBound(nums, target, True) 找左边界
        # 2. 调用 self.findBound(nums, target, False) 找右边界
        # 3. 返回最终的 [left, right]
        left = self.findBound(nums, target, True)
        right = self.findBound(nums, target, False)
        return [left, right]
    
    def findBound(self, nums: List[int], target: int, isLeft: bool) -> int:
        """
        第一步：实现这一个通用的“找边界”函数。
        我们要利用“记录结果但不停止”的策略。
        """
        left, right = 0, len(nums) - 1
        ans = -1 # 默认没找到就是 -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                # --- 💡 第一步的核心逻辑就在这： ---
                # 1. 既然撞到了目标，赶紧记下来：ans = mid
                # 2. 但是不要停！假设“还没找够”，继续往左或往右找
                #    - 如果是找左边界 (isLeft 为真)，我们想看左边还有没有，所以 right = mid - 1
                #    - 如果是找右边界 (isLeft 为假)，我们想看右边还有没有，所以 left = mid + 1
                ans = mid
                if isLeft:
                    right = mid - 1
                else:
                    left = mid + 1
            
            elif nums[mid] < target:
                # 目标在右边
                left = mid + 1
            else:
                # 目标在左边
                right = mid - 1
                
        return ans

if __name__ == "__main__":
    sol = Solution()
    
    # 测试用例 1: 存在多个目标
    print(f"Test 1: {sol.searchRange([5, 7, 7, 8, 8, 10], 8)} (Expect: [3, 4])")
    
    # 测试用例 2: 目标不存在
    print(f"Test 2: {sol.searchRange([5, 7, 7, 8, 8, 10], 6)} (Expect: [-1, -1])")
    
    # 测试用例 3: 空数组
    print(f"Test 3: {sol.searchRange([], 0)} (Expect: [-1, -1])")
