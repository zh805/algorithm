/*
 * @lc app=leetcode.cn id=2357 lang=golang
 *
 * [2357] 使数组中所有元素都等于零
 */
package main

// @lc code=start
func minimumOperations(nums []int) int {
	res := 0
	s := [101]bool{true}
	for _, num := range nums {
		if !s[num] {
			s[num] = true
			res++
		}
	}
	return res
}

// @lc code=end
