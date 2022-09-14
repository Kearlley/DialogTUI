#!/bin/env python3
# *-- coding:utf-8 --*

import DialogTUI as ui
from DialogTUI import Args

window = ui.Window(
    'Window Title',
    20,  # 高
    30,  # 宽
    Args.NO_SHADOW
)

# 这种是变量传递，硬编码方式
# 还可以创建一个JSON文件来写每个窗口的样式来更好的维护
# Example:
MenuDesign = ui.LoadJsonDesign('example.json')

menu_out = window.Menu(
    'Hello World!',  # 文本
    4,  # 菜单高度
    {
        '1': 'InputBox',
        '2': 'MessageBox',
        '3': 'Im Json Menu'
    }  # 菜单列表
)  # 在用户确认后返回一个元组，包含 状态码 和 用户选择 的内容

match menu_out[1][0]:
    case '1':  # If Chose 1
        input_out = window.InputBox('Hello World!', 'This a Default Input')  # 文本
    case '2':  # If Chose 2
        msgbox_out = window.MessageBox('Im Msgbox!')
    case '3':
        window.Menu('Im Show again', 4, MenuDesign)
