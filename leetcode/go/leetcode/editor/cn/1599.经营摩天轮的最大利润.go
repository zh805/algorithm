/*
 * @lc app=leetcode.cn id=1599 lang=golang
 *
 * [1599] 经营摩天轮的最大利润
 */

package main

// @lc code=start
func minOperationsMaxProfit(customers []int, boardingCost int, runningCost int) int {
	res := -1
	curProfit, maxProfit, turn, wait_c := 0, 0, 0, 0
	for wait_c > 0 || turn < len(customers) {
		if turn < len(customers) {
			wait_c += customers[turn]
		}
		upCount := min(wait_c, 4)
		curProfit += boardingCost*upCount - runningCost
		wait_c -= upCount
		if curProfit > maxProfit {
			maxProfit = curProfit
			res = turn + 1
		}
		turn++
	}
	return res
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

// @lc code=end
