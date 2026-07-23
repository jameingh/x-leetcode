# 70. 爬楼梯 (Climbing Stairs)
#
# 题目描述：
# 假设你正在爬楼梯，需要 n 阶你才能到达楼顶。
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
#
# 示例：
#   输入：n = 3
#   输出：3（解释：1+1+1 / 1+2 / 2+1）
#
# 思维模型：【答案拼装】
#   到达第 i 级台阶的最后一步，要么是从第 i-1 级跨 1 步来的，
#   要么是从第 i-2 级跨 2 步来的。没有第三种可能。
#   所以：dp[i] = dp[i-1] + dp[i-2]
#
# DP 三步走：
#   1. 定义状态：dp[i] 表示"到达第 i 级台阶的方法数"
#   2. 转移方程：dp[i] = dp[i-1] + dp[i-2]
#   3. 起点：dp[1] = 1, dp[2] = 2，从小往大推


class Solution:
    def climbStairs(self, n: int) -> int:
        # 提示 1：先处理 n = 1、n = 2 这种小到不需要"拼装"的情况
        #
        # 提示 2：创建 dp 数组（长度 n + 1，方便让下标 i 直接对应第 i 级台阶）
        #         并填好起点 dp[1] 和 dp[2]
        #
        # 提示 3：从 3 开始循环到 n，每一格都用转移方程拼装出来
        #
        # 提示 4：最终答案就是 dp[n]
        if n == 1:
            return 1
        if n == 2:
            return 2

        prev = 1
        curr = 2
        for i in range(3, n + 1):
            temp = prev + curr
            prev = curr
            curr = temp

        return curr


if __name__ == "__main__":
    solution = Solution()

    # 测试用例 1：基础情况
    print(solution.climbStairs(2))  # 期望输出: 2

    # 测试用例 2：大脑模拟过的例子
    print(solution.climbStairs(3))  # 期望输出: 3

    # 测试用例 3：验证推导链条
    print(solution.climbStairs(5))  # 期望输出: 8

    # 测试用例 4：边界情况
    print(solution.climbStairs(1))  # 期望输出: 1
