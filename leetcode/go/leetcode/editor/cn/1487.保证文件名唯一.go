/*
 * @lc app=leetcode.cn id=1487 lang=golang
 *
 * [1487] 保证文件名唯一
 */

package main

import (
	"fmt"
)

// @lc code=start
// 方法1：哈希计数
func getFolderNames(names []string) []string {
	d := map[string]int{}
	for i, name := range names {
		if k, ok := d[name]; ok {
			for {
				newName := fmt.Sprintf("%s(%d)", name, k)
				if d[newName] == 0 {
					d[name] = k + 1
					names[i] = newName
					break
				}
				k++
			}
		}
		d[names[i]] = 1
	}
	return names
}

// @lc code=end
