/*
 * @lc app=leetcode.cn id=2399 lang=golang
 *
 * [2399] 检查相同字母间的距离
 */

package main

// @lc code=start
func checkDistances(s string, distance []int) bool {
	m := [26]int{}
	for i := 0; i < 26; i++ {
		m[i] = -1
	}
	for i, c := range s {
		idx := int(c) - 97
		if m[idx] != -1 {
			if i-m[idx]-1 != distance[idx] {
				return false
			}
		}
		m[idx] = i
	}
	return true
}

// @lc code=end
