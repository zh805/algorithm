//假如有一排房子，共 n 个，每个房子可以被粉刷成红色、蓝色或者绿色这三种颜色中的一种，你需要粉刷所有的房子并且使其相邻的两个房子颜色不能相同。
//
// 当然，因为市场上不同颜色油漆的价格不同，所以房子粉刷成不同颜色的花费成本也是不同的。每个房子粉刷成不同颜色的花费是以一个 n x 3 的正整数矩阵
//costs 来表示的。
//
// 例如，costs[0][0] 表示第 0 号房子粉刷成红色的成本花费；costs[1][2] 表示第 1 号房子粉刷成绿色的花费，以此类推。
//
// 请计算出粉刷完所有房子最少的花费成本。
//
//
//
// 示例 1：
//
//
//输入: costs = [[17,2,17],[16,16,5],[14,3,19]]
//输出: 10
//解释: 将 0 号房子粉刷成蓝色，1 号房子粉刷成绿色，2 号房子粉刷成蓝色。
//     最少花费: 2 + 5 + 3 = 10。
//
//
// 示例 2：
//
//
//输入: costs = [[7,6,2]]
//输出: 2
//
//
//
//
// 提示:
//
//
// costs.length == n
// costs[i].length == 3
// 1 <= n <= 100
// 1 <= costs[i][j] <= 20
//
//
//
//
// 注意：本题与主站 256 题相同：https://leetcode-cn.com/problems/paint-house/
// 👍 85 👎 0

//leetcode submit region begin(Prohibit modification and deletion)

package main

import "fmt"

// 方法1：动态规划
//func minCost(costs [][]int) int {
//	// dp[i][j]为第i个房子粉刷红、蓝、绿颜色的费用
//	n := len(costs)
//	//dp := make([][]int, n, 3)
//	var dp [][3]int
//	row1 := [3]int{costs[0][0], costs[0][1], costs[0][2]}
//	dp = append(dp, row1)
//	for i := 1; i < n; i++ {
//		row := [3]int{}
//		for j := 0; j < 3; j++ {
//			switch j {
//			case 0:
//				row[j] = minOffer091(dp[i-1][1], dp[i-1][2]) + costs[i][j]
//			case 1:
//				row[j] = minOffer091(dp[i-1][0], dp[i-1][2]) + costs[i][j]
//			case 2:
//				row[j] = minOffer091(dp[i-1][0], dp[i-1][1]) + costs[i][j]
//			}
//		}
//		dp = append(dp, row)
//	}
//	return minOffer091(minOffer091(dp[n-1][0], dp[n-1][1]), dp[n-1][2])
//
//}

// 方法1.1，优化空间复杂度
//func minCost(costs [][]int) int {
//	dp := [3]int{costs[0][0], costs[0][1], costs[0][2]}
//	n := len(costs)
//	for i := 1; i < n; i++ {
//		row := [3]int{}
//		for j := 0; j < 3; j++ {
//			row[j] = minOffer091(dp[(j+1)%3], dp[(j+2)%3]) + costs[i][j]
//		}
//		dp = row
//	}
//	return minOffer091(minOffer091(dp[0], dp[1]), dp[2])
//}

// 方法1.2，答案的解法
func minCost(costs [][]int) int {
	dp := costs[0]
	for _, cost := range costs[1:] {
		row := make([]int, 3)
		for j := 0; j < 3; j++ {
			row[j] = minOffer091(dp[(j+1)%3], dp[(j+2)%3]) + cost[j]
		}
		dp = row
	}
	return minOffer091(minOffer091(dp[0], dp[1]), dp[2])
}

func minOffer091(a, b int) int {
	if a < b {
		return a
	} else {
		return b
	}
}

//leetcode submit region end(Prohibit modification and deletion)

func main() {
	costs := [][]int{{17, 2, 17}, {16, 16, 5}, {14, 3, 19}}
	//costs := [][]int{{7, 6, 2}}
	result := minCost(costs)
	fmt.Println(result)
}
