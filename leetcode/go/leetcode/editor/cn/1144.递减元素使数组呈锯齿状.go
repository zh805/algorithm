/*
 * @lc app=leetcode.cn id=1144 lang=golang
 *
 * [1144] 递减元素使数组呈锯齿状
 */

package main

// @lc code=start
func movesToMakeZigzag(nums []int) int {
	helper := func(pos int) int {
		res := 0
		for i := pos; i < len(nums); i += 2 {
			a := 0
			if i-1 >= 0 {
				a = max(a, nums[i]-nums[i-1]+1)
			}
			if i+1 < len(nums) {
				a = max(a, nums[i]-nums[i+1]+1)
			}
			res += a
		}
		return res
	}
	return min(helper(0), helper(1))
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

// @lc code=end
