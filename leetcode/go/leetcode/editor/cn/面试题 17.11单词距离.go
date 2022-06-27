//有个内含单词的超大文本文件，给定任意两个不同的单词，找出在这个文件中这两个单词的最短距离(相隔单词数)。如果寻找过程在这个文件中会重复多次，而每次寻找的单词
//不同，你能对此优化吗?
//
// 示例：
//
//
//输入：words = ["I","am","a","student","from","a","university","in","a","city"],
//word1 = "a", word2 = "student"
//输出：1
//
// 提示：
//
//
// words.length <= 100000
//
// Related Topics 数组 字符串 👍 43 👎 0

package main

import (
	"fmt"
	"math"
)

//leetcode submit region begin(Prohibit modification and deletion)
func findClosest(words []string, word1 string, word2 string) int {
	res := math.MaxInt
	mapping := make(map[string][]int)
	for i, word := range words {
		mapping[word] = append(mapping[word], i)
	}
	//fmt.Printf("mapping: %v\n", mapping)

	word1Idxs := mapping[word1]
	word2Idxs := mapping[word2]
	//fmt.Println(word1Idxs, word2Idxs)
	for _, idx1 := range word1Idxs {
		for _, idx2 := range word2Idxs {
			res = min1711(res, int(math.Abs(float64(idx1-idx2))))
		}
	}

	return res
}

func min1711(a, b int) int {
	if a > b {
		return b
	}
	return a
}

//leetcode submit region end(Prohibit modification and deletion)

func main() {
	words := []string{"I", "am", "a", "student", "from", "a", "university", "in", "a", "city"}
	word1 := "a"
	word2 := "student"
	result := findClosest(words, word1, word2)
	fmt.Println(result)
}
