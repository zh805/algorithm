# 给你一个日期，请你设计一个算法来判断它是对应一周中的哪一天。 
# 
#  输入为三个整数：day、month 和 year，分别表示日、月、年。 
# 
#  您返回的结果必须是这几个值中的一个 {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", 
# "Friday", "Saturday"}。 
# 
#  
# 
#  示例 1： 
# 
#  输入：day = 31, month = 8, year = 2019
# 输出："Saturday"
#  
# 
#  示例 2： 
# 
#  输入：day = 18, month = 7, year = 1999
# 输出："Sunday"
#  
# 
#  示例 3： 
# 
#  输入：day = 15, month = 8, year = 1993
# 输出："Sunday"
#  
# 
#  
# 
#  提示： 
# 
#  
#  给出的日期一定是在 1971 到 2100 年之间的有效日期。 
#  
#  👍 110 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
    #     """
    #     方法1：datetime
    #     :param day:
    #     :param month:
    #     :param year:
    #     :return:
    #     """
    #     from datetime import date
    #     d = date(year=year, month=month, day=day)
    #     return d.strftime('%A')

    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        """
        方法2：模拟法，计算当前日期距离1970年12月31日（星期四）共多少天
        1) 计算整年的天数（year-1971）* （365 or 366）
        2）计算整月的天数
        3）计算本月天数
        4）以上相加后对7取余
        :param day:
        :param month:
        :param year:
        :return:
        """
        days = 4

        week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        for i in range(1971, year):
            if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
                days += 366
            else:
                days += 365

        for i in range(1, month):
            days += month_days[i-1]
            if i == 2 and ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
                days += 1

        days += day
        return week[days % 7]

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    day = 31
    month = 8
    year = 2019
    # day = 1
    # month = 1
    # year = 1971
    result = Solution().dayOfTheWeek(day, month, year)
    print(result)
