//给你一个大小为 m x n 的矩阵 mat ，请以对角线遍历的顺序，用一个数组返回这个矩阵中的所有元素。
//
//
//
// 示例 1：
//
//
//输入：mat = [[1,2,3],[4,5,6],[7,8,9]]
//输出：[1,2,4,7,5,3,6,8,9]
//
//
// 示例 2：
//
//
//输入：mat = [[1,2],[3,4]]
//输出：[1,2,3,4]
//
//
//
//
// 提示：
//
//
// m == mat.length
// n == mat[i].length
// 1 <= m, n <= 10⁴
// 1 <= m * n <= 10⁴  ,m
// -10⁵ <= mat[i][j] <= 10⁵
//
// 👍 315 👎 0

package main

import "fmt"

//leetcode submit region begin(Prohibit modification and deletion)
func findDiagonalOrder(mat [][]int) []int {
	m, n := len(mat), len(mat[0])
	res := make([]int, 0, m*n)
	for i := 0; i < m+n-1; i++ {
		if i&1 == 0 {
			x := min498(i, m-1)
			y := max498(i-m+1, 0)
			for x >= 0 && y < n {
				res = append(res, mat[x][y])
				x--
				y++
			}
		} else {
			x := max498(i-n+1, 0)
			y := min498(i, n-1)
			for x < m && y >= 0 {
				res = append(res, mat[x][y])
				x++
				y--
			}
		}
	}
	return res
}

func max498(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func min498(a, b int) int {
	if a < b {
		return a
	}
	return b
}

//leetcode submit region end(Prohibit modification and deletion)

func main() {
	//mat := [][]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}
	mat := [][]int{{1, 2}, {3, 4}}
	result := findDiagonalOrder(mat)
	fmt.Println(result)
}
