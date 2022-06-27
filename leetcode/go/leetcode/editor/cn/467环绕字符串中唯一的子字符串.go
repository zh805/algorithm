//把字符串 s 看作是 “abcdefghijklmnopqrstuvwxyz” 的无限环绕字符串，所以 s 看起来是这样的：
//
//
// "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd...." .
//
//
// 现在给定另一个字符串 p 。返回 s 中 唯一 的 p 的 非空子串 的数量 。
//
//
//
// 示例 1:
//
//
//输入: p = "a"
//输出: 1
//解释: 字符串 s 中只有一个"a"子字符。
//
//
// 示例 2:
//
//
//输入: p = "cac"
//输出: 2
//解释: 字符串 s 中的字符串“cac”只有两个子串“a”、“c”。.
//
//
// 示例 3:
//
//
//输入: p = "zab"
//输出: 6
//解释: 在字符串 s 中有六个子串“z”、“a”、“b”、“za”、“ab”、“zab”。
//
//
//
//
// 提示:
//
//
// 1 <= p.length <= 10⁵
// p 由小写英文字母构成
//
// Related Topics 字符串 动态规划 👍 240 👎 0

package main

//leetcode submit region begin(Prohibit modification and deletion)

// 动态规划
func findSubstringInWraproundString(p string) int {
	dp := [26]int{}
	k := 0
	for i := 0; i < len(p); i++ {
		if i > 0 && byte(p[i]-p[i-1]+26)%26 == 1 {
			k++
		} else {
			k = 1
		}
		//dp[p[i]-'a'] = int(math.Max(float64(dp[p[i]-'a']), float64(k)))
		dp[p[i]-'a'] = max467(dp[p[i]-'a'], k)
	}
	//fmt.Println(dp)
	ans := 0
	for _, num := range dp {
		ans += num
	}

	return ans
}

func max467(a int, b int) int {
	if a >= b {
		return a
	} else {
		return b
	}
}

//leetcode submit region end(Prohibit modification and deletion)

//func main() {
//	//p := "a"
//	p := "cac"
//	//p := "zab"
//	result := findSubstringInWraproundString(p)
//	fmt.Println(result)
//}
