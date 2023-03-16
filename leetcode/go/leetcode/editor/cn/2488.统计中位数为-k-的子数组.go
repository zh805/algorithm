/*
 * @lc app=leetcode.cn id=2488 lang=golang
 *
 * [2488] 统计中位数为 K 的子数组
 */

package main

// @lc code=start
// 前缀和+哈希
func countSubarrays(nums []int, k int) int {
	kIndex := -1
	for idx, num := range nums {
		if num == k {
			kIndex = idx
			break
		}
	}
	c := map[int]int{}
	c[0] = 1
	sum := 0
	res := 0
	for idx, num := range nums {
		sum += sign(num - k)
		if idx < kIndex {
			c[sum]++
		} else {
			pre0 := c[sum]
			pre1 := c[sum-1]
			res += pre0 + pre1
		}
	}
	return res
}

func sign(num int) int {
	if num == 0 {
		return 0
	}
	if num < 0 {
		return -1
	}
	return 1
}

// @lc code=end
