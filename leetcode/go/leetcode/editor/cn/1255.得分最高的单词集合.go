/*
 * @lc app=leetcode.cn id=1255 lang=golang
 *
 * [1255] 得分最高的单词集合
 */

package main

// @lc code=start
func maxScoreWords(words []string, letters []byte, score []int) int {
	res := 0
	n := len(words)
	letters_counter := map[byte]int{}
	for _, letter := range letters {
		letters_counter[letter]++
	}
	for i := 0; i < (1 << n); i++ {
		temp_counter := map[byte]int{}
		for j := 0; j < n; j++ {
			if (i>>j)&1 == 1 {
				word := words[j]
				for k := 0; k < len(word); k++ {
					temp_counter[word[k]]++
				}
			}
		}
		flag := true
		for k, v := range temp_counter {
			if v > letters_counter[k] {
				flag = false
				break
			}
		}
		if flag == true {
			temp_s := 0
			for k, v := range temp_counter {
				temp_s += score[k-'a'] * v
			}
			if temp_s > res {
				res = temp_s
			}
		}
	}
	return res
}

// @lc code=end
