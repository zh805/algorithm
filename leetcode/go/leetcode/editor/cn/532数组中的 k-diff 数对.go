//给你一个整数数组 nums 和一个整数 k，请你在数组中找出 不同的 k-diff 数对，并返回不同的 k-diff 数对 的数目。
//
// k-diff 数对定义为一个整数对 (nums[i], nums[j]) ，并满足下述全部条件：
//
//
// 0 <= i, j < nums.length
// i != j
// nums[i] - nums[j] == k
//
//
// 注意，|val| 表示 val 的绝对值。
//
//
//
// 示例 1：
//
//
//输入：nums = [3, 1, 4, 1, 5], k = 2
//输出：2
//解释：数组中有两个 2-diff 数对, (1, 3) 和 (3, 5)。
//尽管数组中有两个 1 ，但我们只应返回不同的数对的数量。
//
//
// 示例 2：
//
//
//输入：nums = [1, 2, 3, 4, 5], k = 1
//输出：4
//解释：数组中有四个 1-diff 数对, (1, 2), (2, 3), (3, 4) 和 (4, 5) 。
//
//
// 示例 3：
//
//
//输入：nums = [1, 3, 1, 5, 4], k = 0
//输出：1
//解释：数组中只有一个 0-diff 数对，(1, 1) 。
//
//
//
//
// 提示：
//
//
// 1 <= nums.length <= 10⁴
// -10⁷ <= nums[i] <= 10⁷
// 0 <= k <= 10⁷
//
// 👍 206 👎 0

package main

import (
	"fmt"
)

//leetcode submit region begin(Prohibit modification and deletion)

// 排序+滑动窗口
//func findPairs(nums []int, k int) int {
//	res, n, y := 0, len(nums), 0
//	sort.Ints(nums)
//	for x := 0; x < n; x++ {
//		if x == 0 || nums[x] != nums[x-1] {
//			for y < n && (nums[y] < nums[x]+k || y <= x) {
//				y++
//			}
//			if y < n && nums[y] == nums[x]+k {
//				res++
//			}
//		}
//	}
//	return res
//}

// 哈希
func findPairs(nums []int, k int) int {
	visited, res := make(map[int]struct{}), make(map[int]struct{})
	for _, num := range nums {
		if _, ok := visited[num-k]; ok {
			res[num-k] = struct{}{}
		}
		if _, ok := visited[num+k]; ok {
			res[num] = struct{}{}
		}
		visited[num] = struct{}{}
	}
	return len(res)
}

//leetcode submit region end(Prohibit modification and deletion)

func main() {
	//nums := []int{3, 1, 4, 1, 5}
	//k := 2
	//nums := []int{1, 2, 3, 4, 5}
	//k := 1
	//nums := []int{1, 3, 1, 5, 4}
	//k := 0
	//nums := []int{1, 2, 4, 4, 3, 3, 0, 9, 2, 3}
	//k := 3
	//nums := []int{1, 2, 3, 4, 5}
	//k := 5
	nums := []int{1, 1, 1, 1, 1}
	k := 0
	result := findPairs(nums, k)
	fmt.Println(result)
}
