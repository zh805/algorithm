/*
 * @lc app=leetcode.cn id=1653 lang=golang
 *
 * [1653] 使字符串平衡的最少删除次数
 */

package main

// @lc code=start
func minimumDeletions(s string) int {
	leftb, righta := 0, 0
	for _, c := range s {
		if c == 'a' {
			righta++
		}
	}
	res := righta
	for _, c := range s {
		if c == 'a' {
			righta--
		} else {
			leftb++
		}
		res = min(res, leftb+righta)
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
