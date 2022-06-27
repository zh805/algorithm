# -*- coding: utf-8 -*-
#
# @Time           2022/6/6 4:17 PM
# @File           excel_kai.py
# @Description    excel文件处理
# @Author
#

import openpyxl
import pandas as pd
import os


def test_1():
    os.chdir('C:/Users/86138/Desktop')
    path = '照片'
    writer = pd.ExcelWriter("img.xlsx")
    list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            print(file)
            file = file.rstrip(".jpg")
            list.append(file)
    dict = {'filename': list}
    print(dict)
    df = pd.DataFrame(dict)
    df.to_excel(writer, 'sheet1', startcol=0, index=False)
    writer.save()


def test_2():
    # 文件路径; 换成自己本地的文件路径
    file = "/Users/zhanghui/Downloads/坐标.xlsx"
    # 使用pandas读文件
    df = pd.read_excel(file, engine='openpyxl')

    # new_name存提取出来的坐标
    new_name = []
    # 一行一行读excel文件
    for idx, row in df.iterrows():
        # 读filename这一列
        name = row["filename"]
        print(f'这一行的文件名是: {name}')

        # 使用下划线 _ 分割字符串，name分割后的结果是一个列表。 比如： ['ADE1712A115', '-79396', '-191018', 'FIXREVIEW.JPG']
        a = name.split('_')
        print(f'分割后的结果是:{a}')

        # lstrip: 把字符串左边的 - 去掉。
        # 把列表中的坐标取出来然后去掉 -
        x = a[1].lstrip('-')
        y = a[2].lstrip('-')
        print(f'提取出的坐标x是:{x},坐标y是{y}')

        # 把 x和y使用逗号拼成一个字符串
        coordinate = x + ',' + y
        print(f'拼接后的坐标是:{coordinate}')

        # 把拼好的字符串放入new_name列表
        new_name.append(coordinate)

    print(f'所有提取出的坐标是: {new_name}')

    # 把提取出来的坐标写到一个新文件
    data = {"坐标": new_name}
    # 新文件的路径；换成自己电脑的路径。
    new_file = "/Users/zhanghui/Downloads/新坐标.xlsx"
    print(f'开始把数据写到新文件: {new_file}')

    # 使用pandas把数据写到新文件
    writer = pd.ExcelWriter(new_file)
    df = pd.DataFrame(data)
    df.to_excel(writer, 'sheet1', startcol=0, index=False)
    writer.save()
    print("数据已写入新文件")


def test_3():
    # 文件路径; 换成自己本地的文件路径
    file = "/Users/zhanghui/Downloads/坐标.xlsx"
    # 使用pandas读文件
    df = pd.read_excel(file, engine='openpyxl')

    # 分别保存提取到的文件名、坐标x，坐标y
    filenames, x_list, y_list = [], [], []
    # 一行一行读excel文件
    for idx, row in df.iterrows():
        # 读filename这一列
        name = row["filename"]
        print(f'这一行的文件名是: {name}')
        filenames.append(name)

        # 使用下划线 _ 分割字符串，name分割后的结果是一个列表。 比如： ['ADE1712A115', '-79396', '-191018', 'FIXREVIEW.JPG']
        a = name.split('_')
        print(f'分割后的结果是:{a}')

        # lstrip: 把字符串左边的 - 去掉。
        # 把列表中的坐标取出来然后去掉 -
        x = a[1].lstrip('-')
        y = a[2].lstrip('-')
        print(f'提取出的坐标x是:{x},坐标y是{y}')

        # 把x,y坐标放入列表中保存
        x_list.append(x)
        y_list.append(y)

    # 把提取出来的数据写到一个新文件，一共三列。
    data = {"filename": filenames, "坐标x": x_list, "坐标y": y_list}
    # 新文件的路径；换成自己电脑的路径。
    new_file = "/Users/zhanghui/Downloads/新坐标.xlsx"
    print(f'开始把数据写到新文件: {new_file}')

    # 使用pandas把数据写到新文件
    writer = pd.ExcelWriter(new_file)
    df = pd.DataFrame(data)
    df.to_excel(writer, 'sheet1', startcol=0, index=False)
    writer.save()
    print("数据已写入新文件")


if __name__ == '__main__':
    # test_1()
    # test_2()
    test_3()
