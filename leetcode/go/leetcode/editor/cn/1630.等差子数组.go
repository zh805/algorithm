/*
 * @lc app=leetcode.cn id=1630 lang=golang
 *
 * [1630] 等差子数组
 */

package main

// @lc code=start
func checkArithmeticSubarrays(nums []int, l []int, r []int) []bool {
	res := make([]bool, len(l))
	for i := 0; i < len(l); i++ {
		res[i] = checkArithmetic(nums[l[i] : r[i]+1])
	}
	return res
}

func checkArithmetic(nums []int) bool {
	n := len(nums)
	max, min := nums[0], nums[0]
	for _, v := range nums {
		if v > max {
			max = v
		}
		if v < min {
			min = v
		}
	}
	if max == min {
		return true
	}
	// 求公差
	d := (max - min) / (n - 1)
	if (max - min) != d*(n-1) {
		return false
	}
	m := make(map[int]struct{})
	for _, v := range nums {
		m[v] = struct{}{}
	}
	for i := 0; i < n; i++ {
		if _, ok := m[min+d*i]; !ok {
			return false
		}
	}
	return true
}

// @lc code=end
