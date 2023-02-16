/*
 * @lc app=leetcode.cn id=2341 lang=golang
 *
 * [2341] 数组能形成多少数对
 */

package main

// @lc code=start
func numberOfPairs(nums []int) []int {
	cnt := [101]int{}
	for _, v := range nums {
		cnt[v]++
	}
	s := 0
	for _, v := range cnt {
		s += v / 2
	}
	return []int{s, len(nums) - s*2}
}

// @lc code=end
