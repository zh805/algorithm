/*
 * @lc app=leetcode.cn id=2347 lang=golang
 *
 * [2347] 最好的扑克手牌
 */

// @lc code=start

package main

import (
	"bytes"
)

// 方法1
/*
func bestHand(ranks []int, suits []byte) string {
	ranks_counter := make(map[int]int)
	suits_counter := make(map[byte]int)
	for _, item := range ranks {
		ranks_counter[item]++
	}
	for _, item := range suits {
		suits_counter[item]++
	}
	// sort map by value
	// create a slice
	keys := make([]int, 0, len(ranks_counter))
	for k := range ranks_counter {
		keys = append(keys, k)
	}
	sort.Slice(keys, func(i, j int) bool {
		return ranks_counter[keys[i]] >= ranks_counter[keys[j]]
	})

	if len(suits_counter) == 1 {
		return "Flush"
	} else if ranks_counter[keys[0]] >= 3 {
		return "Three of a Kind"
	} else if ranks_counter[keys[0]] == 2 {
		return "Pair"
	} else {
		return "High Card"
	}

}
*/

// 方法2
func bestHand(ranks []int, suits []byte) string {
	if bytes.Count(suits, suits[:1]) == 5 {
		return "Flush"
	}
	counter, pair := map[int]int{}, false
	for _, rank := range ranks {
		counter[rank]++
		if counter[rank] == 3 {
			return "Three of a Kind"
		}
		if counter[rank] == 2 {
			pair = true
		}
	}
	if pair == true {
		return "Pair"
	}
	return "High Card"
}

// @lc code=end
