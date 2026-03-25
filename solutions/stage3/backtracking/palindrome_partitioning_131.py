# 131. 分割回文串 (Palindrome Partitioning)
# https://leetcode.cn/problems/palindrome-partitioning/

from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        核心模型：切割问题 -> 组合问题的变体。
        
        思考引导：
        1. 路径 (Path)：当前已经切分好的回文子串列表。
        2. startIndex：当前这一刀从哪里开始切？
        3. i：切点的位置（从 startIndex 到 n-1）。
           - 截取的子串是 s[startIndex : i + 1]。
        4. 回文判定：如果切下来的这一坨不是回文，这分支就没戏了，直接看下一个切点。
        """
        result = []
        path = []
        n = len(s)

        def is_palindrome(sub_s: str) -> bool:
            # 💡 提示：用双指针来判断一个字符串是否回文
            # 头尾向中间挤压
            left, right = 0, len(sub_s) - 1
            while left < right:
                if sub_s[left] != sub_s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def backtracking(start_index: int):
            # 💡 终止条件：当切割线移动到字符串末尾时，说明这一路切到底了且全是回文。
            if start_index >= n:
                result.append(path[:])
                return

            for i in range(start_index, n):
                # 1. 尝试切一块：s[start_index : i+1]
                sub = s[start_index : i + 1]
                
                # 2. 剪枝：如果不是回文，这个切点直接 pass，试下一个更长的切点
                # TODO: 调研是否有更快的判断方法（比如 DP 预处理）？
                if not is_palindrome(sub):
                    continue
                
                # 3. 做选择：加入路径
                path.append(sub)
                
                # 4. 纵向深入：从 i+1 的位置继续切剩下的
                backtracking(i + 1)
                
                # 5. 撤销选择：回溯
                path.pop()

        backtracking(0)
        return result

# ==========================================
# 大脑模拟测试
# ==========================================
if __name__ == "__main__":
    sol = Solution()
    
    # 测试 1: s = "aab"
    # 期望输出: [["a","a","b"],["aa","b"]]
    print(f"Test 1 - s='aab': \n{sol.partition('aab')}")
    
    # 测试 2: s = "a"
    # 期望输出: [["a"]]
    print(f"Test 2 - s='a': \n{sol.partition('a')}")
