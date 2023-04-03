/*
 * @lc app=leetcode.cn id=1053 lang=golang
 *
 * [1053] 交换一次的先前排列
 */

package main

// @lc code=start
func prevPermOpt1(arr []int) []int {
	n := len(arr)
	for i := n - 2; i >= 0; i-- {
		if arr[i] > arr[i+1] {
			j := n - 1
			for arr[i] <= arr[j] || arr[j] == arr[j-1] {
				j--
			}
			arr[i], arr[j] = arr[j], arr[i]
			break
		}
	}
	return arr
}

// @lc code=end
