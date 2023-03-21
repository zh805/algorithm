/*
 * @lc app=leetcode.cn id=2469 lang=golang
 *
 * [2469] 温度转换
 */

package main

// @lc code=start
func convertTemperature(celsius float64) []float64 {
	var res []float64
	res = append(res, celsius+273.15)
	res = append(res, celsius*1.8+32)
	return res
}

// @lc code=end
