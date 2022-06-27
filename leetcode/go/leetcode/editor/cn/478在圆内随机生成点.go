//给定圆的半径和圆心的位置，实现函数 randPoint ，在圆中产生均匀随机点。
//
// 实现 Solution 类:
//
//
// Solution(double radius, double x_center, double y_center) 用圆的半径 radius 和圆心的位置
// (x_center, y_center) 初始化对象
// randPoint() 返回圆内的一个随机点。圆周上的一点被认为在圆内。答案作为数组返回 [x, y] 。
//
//
//
//
// 示例 1：
//
//
//输入:
//["Solution","randPoint","randPoint","randPoint"]
//[[1.0, 0.0, 0.0], [], [], []]
//输出: [null, [-0.02493, -0.38077], [0.82314, 0.38945], [0.36572, 0.17248]]
//解释:
//Solution solution = new Solution(1.0, 0.0, 0.0);
//solution.randPoint ();//返回[-0.02493，-0.38077]
//solution.randPoint ();//返回[0.82314,0.38945]
//solution.randPoint ();//返回[0.36572,0.17248]
//
//
//
// 提示：
//
//
// 0 < radius <= 10⁸
// -10⁷ <= x_center, y_center <= 10⁷
// randPoint 最多被调用 3 * 10⁴ 次
//
// 👍 125 👎 0

package main

import (
	"fmt"
	"math/rand"
)

//leetcode submit region begin(Prohibit modification and deletion)
type Solution struct {
	r  float64
	xc float64
	yc float64
}

func Constructor478(radius float64, x_center float64, y_center float64) Solution {
	return Solution{
		r:  radius,
		xc: x_center,
		yc: y_center,
	}
}

func (this *Solution) RandPoint() []float64 {
	for {
		x := rand.Float64()*2 - 1
		y := rand.Float64()*2 - 1
		if x*x+y*y <= 1 {
			return []float64{this.xc + x*this.r, this.yc + y*this.r}
		}
	}
}

/**
 * Your Solution object will be instantiated and called as such:
 * obj := Constructor(radius, x_center, y_center);
 * param_1 := obj.RandPoint();
 */
//leetcode submit region end(Prohibit modification and deletion)

func main() {
	s := Constructor478(10.0, 0.0, 0.0)
	for i := 0; i < 10; i++ {
		result := s.RandPoint()
		fmt.Println(result)
	}
}
