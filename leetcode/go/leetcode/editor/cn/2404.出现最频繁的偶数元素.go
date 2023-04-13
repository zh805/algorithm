/*
 * @lc app=leetcode.cn id=2404 lang=golang
 *
 * [2404] 出现最频繁的偶数元素
 */

package main

// @lc code=start
func mostFrequentEven(nums []int) int {
	res := -1
	t := 0
	counter := make(map[int]int)
	for _, num := range nums {
		if num&1 == 0 {
			if _, ok := counter[num]; ok {
				counter[num]++
			} else {
				counter[num] = 1
			}
			if counter[num] > t {
				res = num
				t = counter[num]
			} else if counter[num] == t {
				res = min2404(num, res)
			}
		}
	}
	return res
}

func min2404(a, b int) int {
	if a < b {
		return a
	}
	return b
}

// @lc code=end
