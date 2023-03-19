/*
 * @lc app=leetcode.cn id=1625 lang=golang
 *
 * [1625] 执行操作后字典序最小的字符串
 */

package main

// @lc code=start
// BFS
func findLexSmallestString(s string, a int, b int) string {
	q := []string{s}
	ans := s
	n := len(s)
	vis := map[string]bool{s: true}
	for len(q) > 0 {
		s = q[0]
		q = q[1:]
		if ans > s {
			ans = s
		}
		t1 := []byte(s)
		for i := 1; i < n; i += 2 {
			t1[i] = byte((int(t1[i]-'0')+a)%10 + '0')
		}
		t2 := s[n-b:] + s[:n-b]
		for _, t := range []string{string(t1), t2} {
			if !vis[t] {
				vis[t] = true
				q = append(q, t)
			}
		}
	}
	return ans
}

// @lc code=end
