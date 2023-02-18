/*
 * @lc app=leetcode.cn id=1237 lang=golang
 *
 * [1237] 找出给定方程的正整数解
 */

// @lc code=start
/**
 * This is the declaration of customFunction API.
 * @param  x    int
 * @param  x    int
 * @return 	    Returns f(x, y) for any given positive integers x and y.
 *			    Note that f(x, y) is increasing with respect to both x and y.
 *              i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
 */

package main

func findSolution(customFunction func(int, int) int, z int) [][]int {
	var res [][]int
	y := 100
	for x := 1; x <= 100; x++ {
		for y > 0 && customFunction(x, y) > z {
			y--
		}
		if y == 0 {
			break
		}
		if customFunction(x, y) == z {
			res = append(res, []int{x, y})
		}
	}
	return res
}

// @lc code=end
