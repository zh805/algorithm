/*
 * @lc app=leetcode.cn id=2363 lang=golang
 *
 * [2363] 合并相似的物品
 */

package main

import "sort"

// @lc code=start
func mergeSimilarItems(items1 [][]int, items2 [][]int) [][]int {
	m := map[int]int{}
	for _, item := range items1 {
		m[item[0]] += item[1]
	}
	for _, item := range items2 {
		m[item[0]] += item[1]
	}
	var res [][]int
	for k, v := range m {
		res = append(res, []int{k, v})
	}
	sort.Slice(res, func(i, j int) bool {
		return res[i][0] < res[j][0]
	})
	return res

}

// @lc code=end
