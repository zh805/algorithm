//给你一个区间数组 intervals ，其中 intervals[i] = [starti, endi] ，且每个 starti 都 不同 。
//
// 区间 i 的 右侧区间 可以记作区间 j ，并满足 startj >= endi ，且 startj 最小化 。
//
// 返回一个由每个区间 i 的 右侧区间 的最小起始位置组成的数组。如果某个区间 i 不存在对应的 右侧区间 ，则下标 i 处的值设为 -1 。
//
//
// 示例 1：
//
//
//输入：intervals = [[1,2]]
//输出：[-1]
//解释：集合中只有一个区间，所以输出-1。
//
//
// 示例 2：
//
//
//输入：intervals = [[3,4],[2,3],[1,2]]
//输出：[-1,0,1]
//解释：对于 [3,4] ，没有满足条件的“右侧”区间。
//对于 [2,3] ，区间[3,4]具有最小的“右”起点;
//对于 [1,2] ，区间[2,3]具有最小的“右”起点。
//
//
// 示例 3：
//
//
//输入：intervals = [[1,4],[2,3],[3,4]]
//输出：[-1,2,-1]
//解释：对于区间 [1,4] 和 [3,4] ，没有满足条件的“右侧”区间。
//对于 [2,3] ，区间 [3,4] 有最小的“右”起点。
//
//
//
//
// 提示：
//
//
// 1 <= intervals.length <= 2 * 10⁴
// intervals[i].length == 2
// -10⁶ <= starti <= endi <= 10⁶
// 每个间隔的起点都 不相同
//
// Related Topics 数组 二分查找 排序 👍 141 👎 0

package main

import (
	"fmt"
	"sort"
)

//leetcode submit region begin(Prohibit modification and deletion)

func bisectLeft(nums []int, target int) int {
	left, right := 0, len(nums)
	for left < right {
		mid := left + (right-left)/2
		if nums[mid] == target {
			right = mid
		} else if nums[mid] < target {
			left = mid + 1
		} else if nums[mid] > target {
			right = mid
		}
	}
	return left
}

func findRightInterval(intervals [][]int) []int {
	//var res []int
	n := len(intervals)
	res := make([]int, n)
	starts := make([]int, n)
	mapping := make(map[int]int)
	for idx, interval := range intervals {
		mapping[interval[0]] = idx
		starts[idx] = interval[0]
	}

	sort.Ints(starts)
	fmt.Printf("starts: %v \n", starts)
	for i := 0; i < n; i++ {
		end := intervals[i][1]
		idx := bisectLeft(starts, end)
		println(end, idx)
		if idx == n {
			res[i] = -1
		} else {
			res[i] = mapping[starts[idx]]
		}
	}
	return res
}

//leetcode submit region end(Prohibit modification and deletion)

func main() {
	//intervals := [][]int{{1, 2}}
	//intervals := [][]int{{3, 4}, {2, 3}, {1, 2}}
	intervals := [][]int{{1, 4}, {2, 3}, {3, 4}}
	res := findRightInterval(intervals)
	fmt.Printf("res: %v", res)
}
