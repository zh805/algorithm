# 请实现一个 MyCalendar 类来存放你的日程安排。如果要添加的时间内没有其他安排，则可以存储这个新的日程安排。 
# 
#  MyCalendar 有一个 book(int start, int end)方法。它意味着在 start 到 end 时间内增加一个日程安排，注意，这里
# 的时间是半开区间，即 [start, end), 实数 x 的范围为， start <= x < end。 
# 
#  当两个日程安排有一些时间上的交叉时（例如两个日程安排都在同一时间内），就会产生重复预订。 
# 
#  每次调用 MyCalendar.book方法时，如果可以将日程安排成功添加到日历中而不会导致重复预订，返回 true。否则，返回 false 并且不要将该
# 日程安排添加到日历中。 
# 
#  请按照以下步骤调用 MyCalendar 类: MyCalendar cal = new MyCalendar(); MyCalendar.book(
# start, end) 
# 
#  
# 
#  示例: 
# 
#  
# 输入:
# ["MyCalendar","book","book","book"]
# [[],[10,20],[15,25],[20,30]]
# 输出: [null,true,false,true]
# 解释: 
# MyCalendar myCalendar = new MyCalendar();
# MyCalendar.book(10, 20); // returns true 
# MyCalendar.book(15, 25); // returns false ，第二个日程安排不能添加到日历中，因为时间 15 已经被第一个日程安排预
# 定了
# MyCalendar.book(20, 30); // returns true ，第三个日程安排可以添加到日历中，因为第一个日程安排并不包含时间 20 
#  
# 
#  
# 
#  
# 
#  提示： 
# 
#  
#  每个测试用例，调用 MyCalendar.book 函数最多不超过 1000次。 
#  0 <= start < end <= 10⁹ 
#  
# 
#  
# 
#  注意：本题与主站 729 题相同： https://leetcode-cn.com/problems/my-calendar-i/ 
#  👍 19 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import bisect


#
# class MyCalendar:
#
#     def __init__(self):
#         """
#         方法1：列表存储日程，根据日程的结束时间从小到大排序。
#         """
#         from sortedcontainers import SortedList
#         self.calendar = SortedList(key=lambda item: item[1])
#
#     def book(self, start: int, end: int) -> bool:
#         if len(self.calendar) == 0:
#             self.calendar.add((start, end))
#             return True
#         idx = bisect.bisect_left([item[1] for item in self.calendar], end)
#         if idx > 0 and self.calendar[idx - 1][1] > start:
#             return False
#         if idx < len(self.calendar) and end > self.calendar[idx][0]:
#             return False
#         self.calendar.add((start, end))
#         # print(self.calendar)
#         return True

class MyCalendar:

    def __init__(self):
        """
        方法1：列表存储日程，根据日程的结束时间从小到大排序。
        """
        from sortedcontainers import SortedList
        self.calendar = SortedList(key=lambda item: item[1])

    def book(self, start: int, end: int) -> bool:
        if len(self.calendar) == 0:
            self.calendar.add((start, end))
            return True

        def bisect_left(target):
            # 使用二分法找target的插入点，同bisect_left。
            left, right = 0, len(self.calendar)
            while left < right:
                mid = left + (right - left) // 2
                if self.calendar[mid][1] == target:
                    right = mid
                elif self.calendar[mid][1] < target:
                    left = mid + 1
                elif self.calendar[mid][1] > target:
                    right = mid
            return left

        idx = bisect_left(end)

        if idx > 0 and self.calendar[idx - 1][1] > start:
            return False
        if idx < len(self.calendar) and end > self.calendar[idx][0]:
            return False
        self.calendar.add((start, end))
        # print(self.calendar)
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    obj = MyCalendar()
    # books = [[20, 29], [13, 22], [44, 50], [1, 7], [2, 10], [14, 20], [19, 25], [36, 42], [45, 50], [47, 50],
    #          [39, 45], [44, 50], [16, 25], [45, 50], [45, 50], [12, 20], [21, 29], [11, 20], [12, 17], [34, 40],
    #          [10, 18], [38, 44], [23, 32], [38, 44], [15, 20], [27, 33], [34, 42], [44, 50], [35, 40], [24, 31]]
    # books = [[37, 50], [33, 50], [4, 17], [35, 48], [8, 25]]
    books = [[10, 20], [15, 25], [20, 30]]
    for book in books:
        res = obj.book(book[0], book[1])
        print(res)
