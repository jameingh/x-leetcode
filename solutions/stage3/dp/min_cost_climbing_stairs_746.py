# 746. 使用最小花费爬楼梯 (Min Cost Climbing Stairs)
#
# 题目描述：
# 给你一个整数数组 cost，其中 cost[i] 是从楼梯第 i 个台阶向上爬需要支付的费用。
# 一旦你支付此费用，即可选择向上爬一个或者两个台阶。
# 你可以选择从下标为 0 或下标为 1 的台阶开始爬楼梯。
# 请你计算并返回达到楼梯顶部（数组末尾的再上面一层）的最低花费。
#
# 示例：
#   输入：cost = [10, 15, 20]
#   输出：15（从下标 1 出发，付 15，跨两步直达楼顶）
#
# 思维模型：【挑便宜的那条路】
#   dp[i] = "站到"第 i 级台阶时已付的最小花费（站着不要钱，起跳才要钱）
#   站到第 i 级的最后一步只有两种来源：
#     - 从 i-1 跳 1 步上来：dp[i-1] + cost[i-1]
#     - 从 i-2 跳 2 步上来：dp[i-2] + cost[i-2]
#   两条路只要便宜的：dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
#
# DP 三步走：
#   1. 定义状态：dp[i] = 站到第 i 级台阶的最小花费（楼顶 = 下标 len(cost)）
#   2. 转移方程：dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
#   3. 起点：dp[0] = 0, dp[1] = 0（题目允许免费从 0 或 1 起步）
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 提示 1：楼顶的位置是 len(cost)，所以 dp 表要一直填到下标 len(cost)
        #
        # 提示 2：起点 dp[0] = 0, dp[1] = 0（站上去免费，起跳才收费）
        #
        # 提示 3：从 2 循环到 len(cost)（含），每一格用 min 挑便宜的来源
        #
        # 提示 4：想挑战的话，直接用"滚动变量"写，别忘了"覆盖之前先保值"
        if len(cost) == 0:
            return 0
        if len(cost) == 1:
            return 0
        prev = 0
        curr = 0
        for i in range(2, len(cost) + 1):
            temp = curr
            curr = min(curr + cost[i-1], prev + cost[i-2])
            prev = temp
        return curr

if __name__ == "__main__":
    solution = Solution()

    # 测试用例 1：大脑模拟过的例子
    print(solution.minCostClimbingStairs([10, 15, 20]))  # 期望输出: 15

    # 测试用例 2：需要连续决策的长数组
    print(solution.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))  # 期望输出: 6

    # 测试用例 3：最小规模（只有两级，挑便宜的起点直接登顶）
    print(solution.minCostClimbingStairs([10, 15]))  # 期望输出: 10

    # 测试用例 4：两级同价
    print(solution.minCostClimbingStairs([0, 0]))  # 期望输出: 0
