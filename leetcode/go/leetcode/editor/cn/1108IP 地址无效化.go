//给你一个有效的 IPv4 地址 address，返回这个 IP 地址的无效化版本。
//
// 所谓无效化 IP 地址，其实就是用 "[.]" 代替了每个 "."。
//
//
//
// 示例 1：
//
// 输入：address = "1.1.1.1"
//输出："1[.]1[.]1[.]1"
//
//
// 示例 2：
//
// 输入：address = "255.100.50.0"
//输出："255[.]100[.]50[.]0"
//
//
//
//
// 提示：
//
//
// 给出的 address 是一个有效的 IPv4 地址
//
// 👍 93 👎 0

//leetcode submit region begin(Prohibit modification and deletion)

package main

import (
	"fmt"
	"strings"
)

// 方法1：遍历
//func defangIPaddr(address string) string {
//	var res []byte
//	for _, ch := range address {
//		if byte(ch) == '.' {
//			res = append(res, '[')
//			res = append(res, '.')
//			res = append(res, ']')
//		} else {
//			res = append(res, byte(ch))
//		}
//	}
//	return string(res)
//}


// 方法2：替换
func defangIPaddr(address string) string {
	return strings.ReplaceAll(address, ".", "[.]")
}



//leetcode submit region end(Prohibit modification and deletion)

func main() {
	//address := "1.1.1.1"
	address := "255.100.50.0"
	result := defangIPaddr(address)
	fmt.Println(result)
}
