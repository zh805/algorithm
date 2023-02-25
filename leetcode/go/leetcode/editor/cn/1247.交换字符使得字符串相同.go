/*
 * @lc app=leetcode.cn id=1247 lang=golang
 *
 * [1247] 交换字符使得字符串相同
 */

package main

// @lc code=start
func minimumSwap(s1 string, s2 string) int {
	xy, yx := 0, 0
	n := len(s1)
	for i := 0; i < n; i++ {
		a, b := s1[i], s2[i]
		if a == 'x' && b == 'y' {
			xy++
		} else if a == 'y' && b == 'x' {
			yx++
		}
	}
	if (xy+yx)%2 == 1 {
		return -1
	}
	return xy/2 + yx/2 + xy%2 + yx%2
}

// @lc code=end
