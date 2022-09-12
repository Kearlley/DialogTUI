#!/bin/env python
# *-- coding:utf-8 --*
import subprocess as sp


def Shell(cmd):
    """
    运行一个命令

    :type cmd: list
    :param cmd: 命令
    :return:
    """
    return sp.run(cmd, stdout=sp.PIPE)


def __DICT_Style_1__(command: list, menu: dict) -> list:
    cmd = []
    for lists in menu:
        cmd.append(lists)
        cmd.append(menu[lists])
    return command + cmd


def __DICT_Style_2__(command: list, menu: dict) -> list:
    cmd = []
    for lists in menu:
        cmd.append(lists)
        cmd.append(menu[lists][0])
        cmd.append(menu[lists][1])
    return command + cmd


def __DICT_Style_3__(command: list, menu: dict) -> list:
    cmd = []
    for lists in menu:
        cmd.append(lists)
        cmd.append(menu[lists][0])
        cmd.append(menu[lists][1])
        cmd.append(menu[lists][2])
    return command + cmd


class Args:
    WINDOW_AUTOSIZE = 0
    WINDOW_MAXSIZE = -1


class Window:
    """
    窗口基类

    :type title: str
    :param title: 窗口标题

    :type height: int
    :param height: 窗体高度

    :type width: int
    :param width: 窗体宽度
    """

    def __init__(self, title, height, width):
        self.title = title
        self.height = height
        self.width = width
        self.cmd = [
            'dialog',
            '--stdout',
            '--title', self.title,
            # 4 -- window , # 5 text
            str(self.height),
            str(self.width),
        ]
        # --no-shadow 无阴影

    def MessageBox(self, Message: str) -> int:
        """
        消息窗体

        :param Message: 信息文本
        :return: 状态码
        """
        cmd = self.cmd
        cmd.insert(4, '--msgbox')
        cmd.insert(5, Message)
        out = Shell(cmd)
        return out.returncode

    def InfoBox(self, Message: str) -> int:
        """
        提示信息窗体

        :param Message: 消息文本
        :return: 状态码
        """
        cmd = self.cmd
        cmd.insert(4, '--infobox')
        cmd.insert(5, Message)
        out = Shell(cmd)
        return out.returncode

    def TextBox(self, file: str) -> int:
        """
        文本窗体

        :param file: 文件路径
        :return: 状态码
        """
        cmd = self.cmd
        cmd.insert(4, '--textbox')
        cmd.insert(5, file)
        out = Shell(cmd)
        return out.returncode

    def YesNoBox(self, Message: str) -> int:
        """
        Yes or No 选择窗体

        :param Message: 消息文本
        :return: 状态码
        """
        cmd = self.cmd
        cmd.insert(4, '--yesno')
        cmd.insert(5, Message)
        out = Shell(cmd)
        return out.returncode

    def Menu(self, Message: str, menu_height: int, menu_dict: dict) -> tuple:
        """
        菜单窗体

        :param Message: 消息文本
        :param menu_height: 菜单高度
        :param menu_dict: 菜单字典
        example: {'tag1':'name','tag2':'name'}
        :returns: 返回一个元组 包含状态码 用户选择的 TAG 值
        """
        cmd = self.cmd
        cmd.insert(4, '--menu')
        cmd.insert(5, Message)
        cmd.append(str(menu_height))
        out = Shell(__DICT_Style_1__(cmd, menu_dict))
        return out.returncode, out.stdout.decode('utf-8').replace(" ", ",")

    def TwoChoseList(self, Message: str, tclist_height: int, tclist_dict: dict) -> tuple:
        """
        双栏选择列表,左为未选右为已选,使用空格来选择,TAB来切换列表

        :param Message: 消息文本
        :param tclist_height: 选择框的高度
        :param tclist_dict: 传入一个字典
        example: {'tag1':['show_name','On / Off']}
        :return: 返回一个元组 包含 状态码 用户选择所对应的TAG
        """
        cmd = self.cmd
        cmd.insert(4, '--buildlist')
        cmd.insert(5, Message)
        cmd.append(str(tclist_height))
        out = Shell(__DICT_Style_3__(cmd, tclist_dict))
        return out.returncode, out.stdout.decode('utf-8').replace(" ", ",")

    def DataChose(self, Message: str, Year: int = None, Month: int = None, Day: int = None) -> tuple:
        """
        日期选择器

        :param Message: 消息文本
        :param Year: 默认年
        :param Month: 默认月
        :param Day: 默认日
        :return: 返回一个元组 包含 状态码 用户选择的日期(DD:MM:YY)
        """
        cmd = self.cmd
        cmd.insert(4, '--calendar')
        cmd.insert(5, Message)
        if Day is not None:
            cmd.append(str(Day))
        else:
            cmd.append('0')
        if Month is not None:
            cmd.append(str(Month))
        else:
            cmd.append('0')
        if Year is not None:
            cmd.append(str(Year))
        else:
            cmd.append('0')
        out = Shell(cmd)
        return out.returncode, out.stdout.decode('utf-8').replace("/", ",")

    def CheckList(self, Message: str, checklist_height: int, checklist_dict: dict) -> tuple:
        """
        选择框列表

        :param Message: 消息列表
        :param checklist_height: 列表高度
        :param checklist_dict: 传入一个字典
        example: {'tag1':['show_name','On / Off']}
        :return: 返回一个元组 包含 状态码 和 用户选择的 TAG
        """
        cmd = self.cmd
        cmd.insert(4, '--checklist')
        cmd.insert(5, Message)
        cmd.insert(6, str(checklist_height))
        out = Shell(__DICT_Style_2__(cmd, checklist_dict))
        return out.returncode, out.stdout.decode('utf-8').replace(" ", ",")

    def DirectorySelect(self, dir_path: str) -> tuple:
        """
        目录选择器

        :param dir_path: 指定一个初始路径位置
        :return: 返回一个元组 包含 状态码 和 用户选择或输入的相对路径
        """
        cmd = self.cmd
        cmd.insert(4, '--dselect')
        cmd.insert(5, dir_path)
        out = Shell(cmd)
        return out.returncode, out.stdout.decode('utf-8')

    def FileSelect(self, file_path: str) -> tuple:
        """
        文件选择器

        :param file_path: 指定一个初始文件位置
        :return: 返回一个元组 包含 状态码 和 用户选择或输入的相对路径
        """
        cmd = self.cmd
        cmd.insert(4, '--fselect')
        cmd.insert(5, file_path)
        out = Shell(cmd)
        return out.returncode, out.stdout.decode('utf-8')

    def InputBox(self, Message: str, init: str = None) -> tuple:
        """
        输入框

        :param init: 初始内容 [可选]
        :param Message: 消息文本
        :return: 状态码 用户输入信息
        """
        cmd = self.cmd
        cmd.insert(4, '--inputbox')
        cmd.insert(5, Message)
        if init is not None:
            cmd.append(init)
        out = Shell(cmd)
        return out.returncode, out.stdout.decode('utf-8')

    def PasswordBox(self, Message: str, init: str = None) -> tuple:
        """
        密码框

        :param Message: 消息文本
        :param init: 初始内容 [可选]
        :return: 状态码 用户输入信息
        """
        cmd = self.cmd
        cmd.insert(4, '--insecure')
        cmd.insert(5, '--passwordbox')
        cmd.insert(6, Message)
        if init is not None:
            cmd.append(init)
        out = Shell(cmd)
        return out.returncode, out.stdout.decode('utf-8')

    def EditBox(self, file: str) -> tuple:
        """
        编辑窗口

        :param file: 文件路径
        :return: 返回一个元组 包含 状态码 和 用户编辑的内容
        """
        cmd = self.cmd
        cmd.insert(4, '--editbox')
        cmd.insert(5, file)
        out = Shell(cmd)
        return out.returncode, out.stdout.decode('utf-8')

# TODO: add more function
# --form         <text> <height> <width> <form height> <label1> <l_y1> <l_x1> <item1> <i_y1> <i_x1> <flen1> <ilen1>...
# --gauge        <text> <height> <width> [<percent>]
# --inputmenu    <text> <height> <width> <menu height> <tag1> <item1>...
# --mixedform    <text> <height> <width> <form height> <label1> <l_y1> <l_x1> <item1> <i_y1> <i_x1> <flen1> <ilen1> <itype>...
# --mixedgauge   <text> <height> <width> <percent> <tag1> <item1>...
# --passwordform <text> <height> <width> <form height> <label1> <l_y1> <l_x1> <item1> <i_y1> <i_x1> <flen1> <ilen1>...
# --pause        <text> <height> <width> <seconds>
# --prgbox       <text> <command> <height> <width>
# --programbox   <text> <height> <width>
# --progressbox  <text> <height> <width>
# --radiolist    <text> <height> <width> <list height> <tag1> <item1> <status1>...
# --rangebox     <text> <height> <width> <min-value> <max-value> <default-value>
# --tailbox      <file> <height> <width>
# --tailboxbg    <file> <height> <width>
# --timebox      <text> <height> <width> <hour> <minute> <second>
# --treeview     <text> <height> <width> <list-height> <tag1> <item1> <status1> <depth1>...
