class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        题目：3. 无重复字符的最长子串
        
        🧠 大脑模拟引导：
        1. 窗口扩张：right 指针不断向右移动，把遇到的字符记入“账本”（字典）。
        2. 出现危机：如果新字符在“账本”里已经存在了，说明窗口内有重复。
        3. 清理门户：left 指针必须向右移动，把旧字符从“账本”里注销，直到重复被消除。
        4. 全局记录：在每一步平衡（无重复）状态下，算算当前的窗口长度 (right - left + 1)，和历史最大值 PK。
        
        提示：Python 的字典 {} 或集合 set() 是非常高效的“账本”。
        """
        # 请根据“滑动窗口/手风琴”思维模型在此完善代码
        # 窗口左边界
        left = 0
        # 窗口右边界
        right = 0
        # 窗口长度
        max_length = 0
        # 窗口状态，记录窗口内每个字符的出现次数
        char_map = {}
        # 窗口扩张
        while right < len(s):
            # 添加右边的元素
            if s[right] in char_map:
                # 窗口内有重复元素
                char_map[s[right]] += 1
            else:
                # 窗口内没有重复元素
                char_map[s[right]] = 1
            # 窗口收缩，直到窗口内没有重复元素，从刚进入到窗口的s[right]检查是否重复
            while char_map[s[right]] > 1:
                # 移出左边的元素
                char_map[s[left]] -= 1
                # 左指针右移
                left += 1
            # 更新最大长度
            max_length = max(max_length, right - left + 1)
            # 右指针右移
            right += 1
        return max_length

if __name__ == "__main__":
    sol = Solution()
    
    # 测试用例 1
    test1 = "abcabcbb"
    res1 = sol.lengthOfLongestSubstring(test1)
    print(f"Test 1: '{test1}' -> {res1} (Expect: 3)")
    
    # 测试用例 2
    test2 = "bbbbb"
    res2 = sol.lengthOfLongestSubstring(test2)
    print(f"Test 2: '{test2}' -> {res2} (Expect: 1)")
    
    # 测试用例 3
    test3 = "pwwkew"
    res3 = sol.lengthOfLongestSubstring(test3)
    print(f"Test 3: '{test3}' -> {res3} (Expect: 3)")
