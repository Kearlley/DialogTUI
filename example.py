#!/bin/env python3
# *-- coding:utf-8 --*

import DialogTUI as ui

menu_out = ui.Window(
    'Window Title',
    20,  # 高
    30,  # 宽
).Menu(
    'Hello World!',  # 文本
    4,  # 菜单高度
    {
        'tag1': 'name1',
        'tag2': 'name2'
    }  # 菜单列表
)  # 在用户确认后返回一个列表，包含 状态码 和 用户选择 的内容

input_out = ui.Window('Window Title', 20, 30).InputBox('Hello World!')  # 文本
print(input_out)  # 在用户确认后返回一个列表，包含 状态码 和 用户输入 的内容
