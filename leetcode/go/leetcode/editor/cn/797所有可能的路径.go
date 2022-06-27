//给你一个有 n 个节点的 有向无环图（DAG），请你找出所有从节点 0 到节点 n-1 的路径并输出（不要求按特定顺序）
//
// graph[i] 是一个从节点 i 可以访问的所有节点的列表（即从节点 i 到节点 graph[i][j]存在一条有向边）。
//
//
//
// 示例 1：
//
//
//
//
//输入：graph = [[1,2],[3],[3],[]]
//输出：[[0,1,3],[0,2,3]]
//解释：有两条路径 0 -> 1 -> 3 和 0 -> 2 -> 3
//
//
// 示例 2：
//
//
//
//
//输入：graph = [[4,3,1],[3,2,4],[3],[4],[]]
//输出：[[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
//
//
//
//
// 提示：
//
//
// n == graph.length
// 2 <= n <= 15
// 0 <= graph[i][j] < n
// graph[i][j] != i（即不存在自环）
// graph[i] 中的所有元素 互不相同
// 保证输入为 有向无环图（DAG）
//
//
//
// Related Topics 深度优先搜索 广度优先搜索 图 回溯 👍 265 👎 0

//leetcode submit region begin(Prohibit modification and deletion)

package main

import (
	"fmt"
	"time"
)

func allPathsSourceTarget(graph [][]int) [][]int {
	var ans [][]int
	path := []int{0}

	var dfs func(int)
	dfs = func(x int) {
		if x == len(graph)-1 {
			ans = append(ans, append([]int(nil), path...))
		}
		for _, v := range graph[x] {
			path = append(path, v)
			dfs(v)
			path = path[:len(path)-1]
		}
	}
	dfs(0)
	//fmt.Println(ans)
	return ans

}

func worker(done chan bool) {
	time.Sleep(5 * time.Second)
	done <- true
}

func fibonacci(c, quit chan int) {
	x, y := 0, 1
	for {
		select {
		case c <- x:
			x, y = y, x+y
		case <-quit:
			fmt.Println("quit")
			return
		}
	}
}

func t() {
	now := time.Now()        //获取当前时间
	timestamp1 := now.Unix() //时间戳
	fmt.Printf("现在的时间戳：%v\n", timestamp1)

	ts := 1652782507880
	tss := ts / 1000
	fmt.Println(tss)
	rT := time.Unix(int64(tss), 0)
	diff := now.Sub(rT)
	println(diff.Seconds())
	if diff > 10*time.Second {
		fmt.Println("超时")
	}

	//if now.Sub(rT) > 10*time.Second {
	//	println("超时")
	//}
}

func main() {
	t()

	//c := make(chan int)
	//quit := make(chan int)
	//go func() {
	//	for i := 0; i < 10; i++ {
	//		fmt.Println(<-c)
	//	}
	//	quit <- 0
	//}()
	//fibonacci(c, quit)
	//
	//done := make(chan bool, 1)
	//go worker(done)
	//// 阻塞
	//x := <-done
	//fmt.Println(x)
	//
	//graph := [][]int{{1, 2}, {3}, {3}, {}}
	//ans := allPathsSourceTarget(graph)
	//fmt.Println(ans)
}

//leetcode submit region end(Prohibit modification and deletion)
