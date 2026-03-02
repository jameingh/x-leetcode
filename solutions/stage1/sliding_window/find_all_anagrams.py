from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        题目：438. 找到字符串中所有字母异位词
        
        🧠 大脑模拟引导（“固定窗口”）：
        1. 窗口特征：这次窗口的大小是固定的，就是字符串 p 的长度。
        2. 判定标准：“异位词”意味着窗口内字符出现的频率，必须和 p 中字符出现的频率完全一致。
        3. 状态管理：
           - 你可以准备两个“账本”（字典或长度为 26 的数组）。
           - 一个记目标 p 的频率。
           - 一个记当前窗口 s[left:right+1] 的频率。
        4. 滑动节奏：
           - 右边进一个，左边出一个。
           - 每次滑动后，直接对比两个“账本”是否相等。如果相等，就把当前的左边界 left 记入结果。
           
        注意：Python 中字典可以直接用 == 比较，这非常方便！
        """
        # 请根据“滑动窗口/固定窗口”思维模型在此完善代码
        pass

if __name__ == "__main__":
    sol = Solution()
    
    # 测试用例 1
    s1, p1 = "cbaebabacd", "abc"
    res1 = sol.findAnagrams(s1, p1)
    print(f"Test 1: s='{s1}', p='{p1}' -> {res1} (Expect: [0, 6])")
    
    # 测试用例 2
    s2, p2 = "abab", "ab"
    res2 = sol.findAnagrams(s2, p2)
    print(f"Test 2: s='{s2}', p='{p2}' -> {res2} (Expect: [0, 1, 2])")
