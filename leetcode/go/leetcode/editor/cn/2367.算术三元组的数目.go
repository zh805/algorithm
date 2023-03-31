/*
 * @lc app=leetcode.cn id=2367 lang=golang
 *
 * [2367] 算术三元组的数目
 */

package main

// @lc code=start
func arithmeticTriplets(nums []int, diff int) int {
	res, n := 0, len(nums)
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			for k := j + 1; k < n; k++ {
				if nums[j]-nums[i] == diff && nums[k]-nums[j] == diff {
					res++
				}
			}
		}
	}
	return res
}

// @lc code=end
