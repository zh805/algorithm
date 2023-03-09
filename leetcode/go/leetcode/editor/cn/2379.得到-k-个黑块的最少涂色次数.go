/*
 * @lc app=leetcode.cn id=2379 lang=golang
 *
 * [2379] 得到 K 个黑块的最少涂色次数
 */

package main

// @lc code=start
func minimumRecolors(blocks string, k int) int {
	res := len(blocks)
	w_count := 0
	for i, c := range blocks {
		if c == 'W' {
			w_count++
		}
		if i >= k && blocks[i-k] == 'W' {
			w_count--
		}
		if i >= k-1 {
			res = min(res, w_count)
		}
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
