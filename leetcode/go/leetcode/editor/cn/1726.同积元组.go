/*
 * @lc app=leetcode.cn id=1726 lang=golang
 *
 * [1726] 同积元组
 */

// @lc code=start

package main

func tupleSameProduct(nums []int) int {
	cnt := map[int]int{}
	n := len(nums)
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			x := nums[i] * nums[j]
			cnt[x]++
		}
	}
	res := 0
	for _, v := range cnt {
		res += v * (v - 1) / 2
	}
	return res << 3
}

// @lc code=end
