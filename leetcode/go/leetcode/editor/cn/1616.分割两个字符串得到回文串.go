/*
 * @lc app=leetcode.cn id=1616 lang=golang
 *
 * [1616] 分割两个字符串得到回文串
 */

package main

// @lc code=start

func isPalindrome(s string, i, j int) bool {
	for i < j && s[i] == s[j] {
		i++
		j--
	}
	return i >= j
}

func check(a, b string) bool {
	i, j := 0, len(a)-1
	for i < j && a[i] == b[j] {
		i++
		j--
	}
	return isPalindrome(a, i, j) || isPalindrome(b, i, j)
}

func checkPalindromeFormation(a string, b string) bool {
	return check(a, b) || check(b, a)
}

// @lc code=end
