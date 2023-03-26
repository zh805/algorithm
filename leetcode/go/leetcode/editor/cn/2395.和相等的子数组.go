/*
 * @lc app=leetcode.cn id=2395 lang=golang
 *
 * [2395] 和相等的子数组
 */

package main

// @lc code=start
func findSubarrays(nums []int) bool {
	s := make(map[int]struct{})
	for i := 0; i < len(nums)-1; i++ {
		a := nums[i] + nums[i+1]
		if _, ok := s[a]; ok {
			return true
		}
		s[a] = struct{}{}
	}
	return false
}

// @lc code=end
