//给定一个由非重叠的轴对齐矩形的数组 rects ，其中 rects[i] = [ai, bi, xi, yi] 表示 (ai, bi) 是第 i 个矩形的左
//下角点，(xi, yi) 是第 i 个矩形的右上角点。设计一个算法来随机挑选一个被某一矩形覆盖的整数点。矩形周长上的点也算做是被矩形覆盖。所有满足要求的点必须等
//概率被返回。 
//
// 在给定的矩形覆盖的空间内的任何整数点都有可能被返回。 
//
// 请注意 ，整数点是具有整数坐标的点。 
//
// 实现 Solution 类: 
//
// 
// Solution(int[][] rects) 用给定的矩形数组 rects 初始化对象。 
// int[] pick() 返回一个随机的整数点 [u, v] 在给定的矩形所覆盖的空间内。 
// 
//
// 
// 
//
// 
//
// 示例 1： 
//
// 
//
// 
//输入: 
//["Solution", "pick", "pick", "pick", "pick", "pick"]
//[[[[-2, -2, 1, 1], [2, 2, 4, 6]]], [], [], [], [], []]
//输出: 
//[null, [1, -2], [1, -1], [-1, -2], [-2, -2], [0, 0]]
//
//解释：
//Solution solution = new Solution([[-2, -2, 1, 1], [2, 2, 4, 6]]);
//solution.pick(); // 返回 [1, -2]
//solution.pick(); // 返回 [1, -1]
//solution.pick(); // 返回 [-1, -2]
//solution.pick(); // 返回 [-2, -2]
//solution.pick(); // 返回 [0, 0] 
//
// 
//
// 提示： 
//
// 
// 1 <= rects.length <= 100 
// rects[i].length == 4 
// -10⁹ <= ai < xi <= 10⁹ 
// -10⁹ <= bi < yi <= 10⁹ 
// xi - ai <= 2000 
// yi - bi <= 2000 
// 所有的矩形不重叠。 
// pick 最多被调用 10⁴ 次。 
// 
// 👍 107 👎 0


//leetcode submit region begin(Prohibit modification and deletion)
type Solution struct {

}


func Constructor(rects [][]int) Solution {

}


func (this *Solution) Pick() []int {

}


/**
 * Your Solution object will be instantiated and called as such:
 * obj := Constructor(rects);
 * param_1 := obj.Pick();
 */
//leetcode submit region end(Prohibit modification and deletion)
