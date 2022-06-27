//你有一个单词列表 words 和一个模式 pattern，你想知道 words 中的哪些单词与模式匹配。
//
// 如果存在字母的排列 p ，使得将模式中的每个字母 x 替换为 p(x) 之后，我们就得到了所需的单词，那么单词与模式是匹配的。
//
// （回想一下，字母的排列是从字母到字母的双射：每个字母映射到另一个字母，没有两个字母映射到同一个字母。）
//
// 返回 words 中与给定模式匹配的单词列表。
//
// 你可以按任何顺序返回答案。
//
//
//
// 示例：
//
// 输入：words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
//输出：["mee","aqq"]
//解释：
//"mee" 与模式匹配，因为存在排列 {a -> m, b -> e, ...}。
//"ccc" 与模式不匹配，因为 {a -> c, b -> c, ...} 不是排列。
//因为 a 和 b 映射到同一个字母。
//
//
//
// 提示：
//
//
// 1 <= words.length <= 50
// 1 <= pattern.length = words[i].length <= 20
//
// 👍 178 👎 0

package main

import "fmt"

//leetcode submit region begin(Prohibit modification and deletion)
func findAndReplacePattern(words []string, pattern string) []string {
	var res []string
	for _, word := range words {
		if match(word, pattern) && match(pattern, word) {
			res = append(res, word)
		}
	}
	return res
}

func match(word string, pat string) bool {
	mapping := map[rune]byte{}
	for i, x := range word {
		y := pat[i]
		if mapping[x] == 0 {
			mapping[x] = y
		} else if mapping[x] != y {
			return false
		}
	}
	return true
}

//leetcode submit region end(Prohibit modification and deletion)

func main() {
	//words := []string{"abc", "deq", "mee", "aqq", "dkd", "ccc"}
	//pattern := "abb"
	//result := findAndReplacePattern(words, pattern)
	//fmt.Println(result)

	s := "hell0 你好"
	fmt.Println(len(s))
	for i := 0; i < len(s); i++ {
		fmt.Printf("idx: %d, ch: %d, %c\n", i, s[i], s[i])
	}

	for i, c := range s {
		fmt.Printf("%d, %d, %c\n", i, c, c)
	}

}
