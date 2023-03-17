/*
 * @lc app=leetcode.cn id=2389 lang=golang
 *
 * [2389] 和有限的最长子序列
 */

package main

import "sort"

// 前缀和+二分查找
// @lc code=start
func answerQueries(nums []int, queries []int) []int {
	n := len(nums)
	f := make([]int, n)
	sort.Ints(nums)
	f[0] = nums[0]
	for i := 1; i < n; i++ {
		f[i] = f[i-1] + nums[i]
	}
	res := []int{}
	for _, q := range queries {
		idx := sort.SearchInts(f, q+1)
		res = append(res, idx)
	}
	return res
}

// @lc code=end
