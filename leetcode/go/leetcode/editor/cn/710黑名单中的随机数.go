//给定一个整数 n 和一个 无重复 黑名单整数数组 blacklist 。设计一种算法，从 [0, n - 1] 范围内的任意整数中选取一个 未加入 黑名单
//blacklist 的整数。任何在上述范围内且不在黑名单 blacklist 中的整数都应该有 同等的可能性 被返回。
//
// 优化你的算法，使它最小化调用语言 内置 随机函数的次数。
//
// 实现 Solution 类:
//
//
// Solution(int n, int[] blacklist) 初始化整数 n 和被加入黑名单 blacklist 的整数
// int pick() 返回一个范围为 [0, n - 1] 且不在黑名单 blacklist 中的随机整数
//
//
//
//
// 示例 1：
//
//
//输入
//["Solution", "pick", "pick", "pick", "pick", "pick", "pick", "pick"]
//[[7, [2, 3, 5]], [], [], [], [], [], [], []]
//输出
//[null, 0, 4, 1, 6, 1, 0, 4]
//
//解释
//Solution solution = new Solution(7, [2, 3, 5]);
//solution.pick(); // 返回0，任何[0,1,4,6]的整数都可以。注意，对于每一个pick的调用，
//                 // 0、1、4和6的返回概率必须相等(即概率为1/4)。
//solution.pick(); // 返回 4
//solution.pick(); // 返回 1
//solution.pick(); // 返回 6
//solution.pick(); // 返回 1
//solution.pick(); // 返回 0
//solution.pick(); // 返回 4
//
//
//
//
// 提示:
//
//
// 1 <= n <= 10⁹
// 0 <= blacklist.length <= min(10⁵, n - 1)
// 0 <= blacklist[i] < n
// blacklist 中所有值都 不同
// pick 最多被调用 2 * 10⁴ 次
//
// 👍 152 👎 0

//leetcode submit region begin(Prohibit modification and deletion)
package main

// Solution 方法1： 找出白名单，依次输出。空间复杂度超出限制。
//type Solution struct {
//	whitelist []int
//	length    int
//	idx       int
//}
//
//func Constructor(n int, blacklist []int) Solution {
//	var whitelist []int
//	black := make(map[int]bool)
//	for _, num := range blacklist {
//		black[num] = true
//	}
//	for i := 0; i < n; i++ {
//		_, ok := black[i]
//		if ok == false {
//			whitelist = append(whitelist, i)
//		}
//	}
//	return Solution{
//		whitelist: whitelist,
//		length:    len(whitelist),
//		idx:       0,
//	}
//}
//
//func (this *Solution) Pick() int {
//	res := this.whitelist[this.idx%this.length]
//	this.idx++
//	return res
//}

// Solution 方法2： 只记录黑名单，超时
//type Solution struct {
//	n     int
//	black map[int]bool
//	num   int
//}
//
//func Constructor(n int, blacklist []int) Solution {
//	black := make(map[int]bool)
//	for _, num := range blacklist {
//		black[num] = true
//	}
//	return Solution{
//		n:     n,
//		black: black,
//		num:   0,
//	}
//}
//
//func (this *Solution) Pick() int {
//	var res int
//	for {
//		_, ok := this.black[this.num%this.n]
//		if ok != true {
//			res = this.num % this.n
//			this.num++
//			break
//		} else {
//			this.num++
//		}
//	}
//	return res
//}

// Solution 方法3：白名单与黑名单映射
//type Solution struct {
//	bound int
//	b2w   map[int]int
//}
//
//func Constructor(n int, blacklist []int) Solution {
//	m := len(blacklist)
//	bound := n - m
//
//	black := map[int]bool{}
//	for _, num := range blacklist {
//		if num >= bound {
//			black[num] = true
//		}
//	}
//	w := bound
//	b2w := make(map[int]int, m-len(black))
//	for _, b := range blacklist {
//		if b < bound {
//			for black[w] {
//				w++
//			}
//			b2w[b] = w
//			w++
//		}
//	}
//
//	return Solution{
//		bound: bound,
//		b2w:   b2w,
//	}
//}
//
//func (this *Solution) Pick() int {
//	res := rand.Intn(this.bound)
//	if this.b2w[res] > 0 {
//		return this.b2w[res]
//	}
//	return res
//}

/**
 * Your Solution object will be instantiated and called as such:
 * obj := Constructor(n, blacklist);
 * param_1 := obj.Pick();
 */
//leetcode submit region end(Prohibit modification and deletion)

//func main() {
//	n, blacklist := 7, []int{2, 3, 5}
//	obj := Constructor(n, blacklist)
//	fmt.Println(obj.Pick())
//	fmt.Println(obj.Pick())
//	fmt.Println(obj.Pick())
//	fmt.Println(obj.Pick())
//	fmt.Println(obj.Pick())
//	fmt.Println(obj.Pick())
//	fmt.Println(obj.Pick())
//}
