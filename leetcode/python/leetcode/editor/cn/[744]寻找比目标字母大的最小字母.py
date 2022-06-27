# 给你一个排序后的字符列表 letters ，列表中只包含小写英文字母。另给出一个目标字母 target，请你寻找在这一有序列表里比目标字母大的最小字母。 
# 
#  在比较时，字母是依序循环出现的。举个例子： 
# 
#  
#  如果目标字母 target = 'z' 并且字符列表为 letters = ['a', 'b']，则答案返回 'a' 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入: letters = ["c", "f", "j"]，target = "a"
# 输出: "c"
#  
# 
#  示例 2: 
# 
#  
# 输入: letters = ["c","f","j"], target = "c"
# 输出: "f"
#  
# 
#  示例 3: 
# 
#  
# 输入: letters = ["c","f","j"], target = "d"
# 输出: "f"
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= letters.length <= 10⁴ 
#  letters[i] 是一个小写字母 
#  letters 按非递减顺序排序 
#  letters 最少包含两个不同的字母 
#  target 是一个小写字母 
#  
#  👍 172 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    # def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    #     """
    #     方法1：遍历
    #     """
    #     res = ''
    #     min_gap = float('inf')
    #     t = ord(target)
    #
    #     if t < ord(letters[0]) or t >= ord(letters[-1]):
    #         return letters[0]
    #
    #     for letter in letters:
    #         gap = ord(letter) - t
    #         if 0 < gap < min_gap:
    #             min_gap = gap
    #             res = letter
    #
    #     return res

    # def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    #     """
    #     方法1.2：遍历
    #     """
    #     res = letters[0]
    #     for letter in letters:
    #         if letter > target:
    #             res = letter
    #             break
    #     return res

    # def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    #     """
    #     方法2：二分法。求大于target的最小数字，左边界。
    #     """
    #     target = ord(target)
    #
    #     if target < ord(letters[0]) or target >= ord(letters[-1]):
    #         return letters[0]
    #
    #     left, right = 0, len(letters)
    #     # 左闭右开区间
    #     while left < right:
    #         middle = left + (right - left) // 2
    #         mid = ord(letters[middle])
    #         if mid == target:
    #             # 左边界需要右移动
    #             left = middle + 1
    #         elif mid < target:
    #             left = middle + 1
    #         elif mid > target:
    #             right = middle
    #     return letters[left]

    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        """
        方法2：二分法。求大于target的最小数字。字符大小可以直接比较。
        可以使用34题中搜索target结束位置的方法。结束边界+1即为大于target的最小位置。
        """
        if target < letters[0] or target >= letters[-1]:
            return letters[0]

        left, right = 0, len(letters)
        # 左闭右开区间，[left, right)
        while left < right:
            middle = left + (right - left) // 2
            mid = letters[middle]
            if mid == target:
                # 左边界需要右移动
                left = middle + 1
            elif mid < target:
                left = middle + 1
            elif mid > target:
                right = middle
        return letters[left]


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    letters = ["c", "f", "j"]
    target = "g"
    # letters = ["c", "f", "j"]
    # target = "c"
    # letters = ["c", "f", "j"]
    # target = "j"
    result = Solution().nextGreatestLetter(letters, target)
    print(result)
