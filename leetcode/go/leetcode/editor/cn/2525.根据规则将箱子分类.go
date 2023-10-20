/*
 * @lc app=leetcode.cn id=2525 lang=golang
 *
 * [2525] 根据规则将箱子分类
 */

package main

// @lc code=start
func categorizeBox(length int, width int, height int, mass int) string {
	v := length * width * height
	m := max2525(length, max2525(width, height))
	isBulky := v >= 1e9 || m >= 10000
	isHeavey := mass >= 100
	if isBulky && isHeavey {
		return "Both"
	} else if isBulky {
		return "Bulky"
	} else if isHeavey {
		return "Heavy"
	} else {
		return "Neither"
	}
}

func max2525(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

// @lc code=end
