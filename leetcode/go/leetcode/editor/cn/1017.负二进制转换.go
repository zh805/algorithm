/*
 * @lc app=leetcode.cn id=1017 lang=golang
 *
 * [1017] 负二进制转换
 */

package main

// @lc code=start
func baseNeg2(n int) string {
	if n == 0 {
		return "0"
	}
	res := []byte{}
	k := 1
	for n != 0 {
		if n%2 == 1 {
			res = append(res, '1')
			n -= k
		} else {
			res = append(res, '0')
		}
		n /= 2
		k *= -1
	}
	for i, j := 0, len(res)-1; i < j; i, j = i+1, j-1 {
		res[i], res[j] = res[j], res[i]
	}
	return string(res)
}

// @lc code=end
