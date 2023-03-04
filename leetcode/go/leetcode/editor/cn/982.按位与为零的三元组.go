/*
 * @lc app=leetcode.cn id=982 lang=golang
 *
 * [982] 按位与为零的三元组
 */

package main

// @lc code=start
func countTriplets(nums []int) int {
	res := 0
	c := make(map[int]int)
	for _, x := range nums {
		for _, y := range nums {
			c[x&y]++
		}
	}
	for _, k := range nums {
		for key, value := range c {
			if k&key == 0 {
				res += value
			}
		}
	}
	return res
}

// @lc code=end
