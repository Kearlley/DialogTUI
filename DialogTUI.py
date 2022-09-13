#!/bin/env python
# *-- coding:utf-8 --*
import subprocess as sp


def Shell(cmd):
    """
    运行一个命令

    :type cmd: list
    :param cmd: 命令
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


def __DATE_TIME__(command: list, X: int = None, Y: int = None, Z: int = None) -> list:
    cmd = []
    if X is not None:
        cmd.append(str(X))
    else:
        cmd.append('0')
    if Y is not None:
        cmd.append(str(Y))
    else:
        cmd.append('0')
    if Z is not None:
        cmd.append(str(Z))
    else:
        cmd.append('0')
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
        self.cmd = [
            'dialog',
            '--stdout',
            '--title', self.title,
            # 4 -- window , # 5 text
            str(height),
            str(width),
        ]
        # --no-shadow 无阴影

    def MessageBox(self, Message: str) -> int:
        """
        消息窗体

        :param Message: 信息文本
        :return: 状态码
        """
        cmd = [] + self.cmd
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
        cmd = [] + self.cmd
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
        cmd = [] + self.cmd
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
        cmd = [] + self.cmd
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
        cmd = [] + self.cmd
        cmd.insert(4, '--menu')
        cmd.insert(5, Message)
        cmd.append(str(menu_height))
        out = Shell(__DICT_Style_1__(cmd, menu_dict))
        return out.returncode, out.stdout.decode('utf-8').split()

    def InputMenu(self, Message: str, inputmenu_height: int, inputmenu_dict: dict) -> tuple:
        """

        :param Message: 消息文本
        :param inputmenu_height: 菜单高度
        :param inputmenu_dict: 菜单字典
        example: {'tag1':'name','tag2':'name'}
        :return: 返回一个元组，如果用户未点击RENAME按钮 将只会返回一个状态码，如果点击了RENAME按钮则会返回 ['RENAME','TAG1','Name']
        """
        cmd = [] + self.cmd
        cmd.insert(4, '--inputmenu')
        cmd.insert(5, Message)
        cmd.append(str(inputmenu_height))
        out = Shell(__DICT_Style_1__(cmd, inputmenu_dict))
        return out.returncode, out.stdout.decode('utf-8').split()

    def TwoChoseList(self, Message: str, tclist_height: int, tclist_dict: dict) -> tuple:
        """
        双栏选择列表,左为未选右为已选,使用空格来选择,TAB来切换列表

        :param Message: 消息文本
        :param tclist_height: 选择框的高度
        :param tclist_dict: 传入一个字典
        example: {'tag1':['show_name','On / Off']}
        :return: 返回一个元组 包含 状态码 用户选择所对应的TAG
        """
        cmd = [] + self.cmd
        cmd.insert(4, '--buildlist')
        cmd.insert(5, Message)
        cmd.append(str(tclist_height))
        out = Shell(__DICT_Style_2__(cmd, tclist_dict))
        return out.returncode, out.stdout.decode('utf-8').split()

    def DateChose(self, Message: str, Year: int = None, Month: int = None, Day: int = None) -> tuple:
        """
        日期选择器

        :param Message: 消息文本
        :param Year: 默认年
        :param Month: 默认月
        :param Day: 默认日
        :return: 返回一个元组 包含 状态码 用户选择的日期(DD:MM:YY)
        """
        cmd = [] + self.cmd
        cmd.insert(4, '--calendar')
        cmd.insert(5, Message)
        out = Shell(__DATE_TIME__(cmd, Year, Month, Day))
        return out.returncode, out.stdout.decode('utf-8').split('/')

    def TimeChose(self, Message: str, hour: int = None, minute: int = None, second: int = None) -> tuple:
        """
        时间选择

        :param Message: 消息文本
        :param hour: 默认年
        :param minute: 默认月
        :param second: 默认日
        :return: 返回一个元组 包含 状态码 用户选择的日期(DD:MM:YY)
        """
        cmd = [] + self.cmd
        cmd.insert(4, '--timebox')
        cmd.insert(5, Message)
        out = Shell(__DATE_TIME__(cmd, hour, minute, second))
        return out.returncode, out.stdout.decode('utf-8').split(':')

    def CheckList(self, Message: str, checklist_height: int, checklist_dict: dict) -> tuple:
        """
        选择框列表

        :param Message: 消息文本
        :param checklist_height: 列表高度
        :param checklist_dict: 传入一个字典
        example: {'tag1':['show_name','On / Off']}
        :return: 返回一个元组 包含 状态码 和 用户选择的 TAG
        """
        cmd = [] + self.cmd
        cmd.insert(4, '--checklist')
        cmd.insert(5, Message)
        cmd.insert(6, str(checklist_height))
        out = Shell(__DICT_Style_2__(cmd, checklist_dict))
        return out.returncode, out.stdout.decode('utf-8').split()

    def RadioList(self, Message: str, radiolist_height: int, radiolist_dict: dict) -> tuple:
        """
        选择框列表 - 只能选择一个

        :param Message: 消息文本
        :param radiolist_height: 列表高度
        :param radiolist_dict: 传入一个字典
        example: {'tag1':['show_name','On / Off']}
        :return: 返回一个元组 包含 状态码 和 用户选择的 TAG
        """
        cmd = [] + self.cmd
        cmd.insert(4, '--radiolist')
        cmd.insert(5, Message)
        cmd.insert(6, str(radiolist_height))
        out = Shell(__DICT_Style_2__(cmd, radiolist_dict))
        return out.returncode, out.stdout.decode('utf-8').split()

    def DirectorySelect(self, dir_path: str) -> tuple:
        """
        目录选择器

        :param dir_path: 指定一个初始路径位置
        :return: 返回一个元组 包含 状态码 和 用户选择或输入的相对路径
        """
        cmd = [] + self.cmd
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
        cmd = [] + self.cmd
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
        cmd = [] + self.cmd
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
        cmd = [] + self.cmd
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
        cmd = [] + self.cmd
        cmd.insert(4, '--editbox')
        cmd.insert(5, file)
        out = Shell(cmd)
        return out.returncode, out.stdout.decode('utf-8')

    def RunCommand(self, Message: str, command: str) -> int:
        """
        运行命令并将返回结果到窗口

        :param Message: 消息文本
        :param command: 命令
        :return: 返回一个状态码
        """
        cmd = [] + self.cmd
        cmd.insert(4, '--prgbox')
        cmd.insert(5, Message)
        cmd.insert(6, command)
        out = Shell(cmd)
        return out.returncode

    def TailBox(self, file: str) -> int:
        """
        监控日志或者是文件更新的实时内容并输出到窗口

        :param file: 文件路径
        :return: 返回一个状态码
        """
        cmd = [] + self.cmd
        cmd.insert(4, '--tailbox')
        cmd.insert(5, file)
        out = Shell(cmd)
        return out.returncode

    def TailBoxBG(self, file: str) -> int:
        """
        研究中...应该也是和tailbox一样来监控日志或者是文件更新的实时内容的，从命命来看应该是直接输出到背景

        :param file: 文件路径
        :return: 返回一个状态码
        """
        cmd = [] + self.cmd
        cmd.insert(4, '--tailboxbg')
        cmd.insert(5, file)
        out = Shell(cmd)
        return out.returncode

    def ProgressBar(self, Message: str, percent: int) -> int:
        """
        进度条

        :param Message: 消息文本
        :param percent: 进度
        :return: 返回一个状态码
        """
        cmd = [] + self.cmd
        cmd.insert(4, '--gauge')
        cmd.insert(5, Message)
        cmd.append(str(percent))
        out = Shell(cmd)
        return out.returncode

    def MixedProgressBar(self, Message: str, percent: int, menu_dict: dict) -> int:
        """
        混合进度条 包含进度条和菜单字典

        :param Message: 消息文本
        :param percent: 进度
        :param menu_dict: 菜单字典,我推荐这样用
        example: {'name1':'status','name1':'status'}
        :return: 返回一个状态码
        """
        cmd = [] + self.cmd
        cmd.insert(4, '--mixedgauge')
        cmd.insert(5, Message)
        cmd.append(str(percent))
        out = Shell(__DICT_Style_1__(cmd, menu_dict))
        return out.returncode

    def CountdownConfirm(self, Message: str, seconds: int) -> int:
        """
        倒计时确认窗体

        :param Message: 消息文本
        :param seconds: 倒计时时间
        :return: 返回一个状态码
        """
        cmd = [] + self.cmd
        cmd.insert(4, '--pause')
        cmd.insert(5, Message)
        cmd.append(str(seconds))
        out = Shell(cmd)
        return out.returncode

    def RangeChose(self, Message: str, min_range: int, max_range: int, step: int) -> tuple:
        """
        范围选择窗口

        :param Message: 消息文本
        :param min_range: 最小值
        :param max_range: 最大值
        :param step: 每次步进的值
        :return: 返回一个元组 包含 状态码 和 用户选择的值
        """
        cmd = [] + self.cmd
        cmd.insert(4, '--rangebox')
        cmd.insert(5, Message)
        cmd.append(str(min_range))
        cmd.append(str(max_range))
        cmd.append(str(step))
        out = Shell(cmd)
        return out.returncode, out.stdout.decode('utf-8')

    def TreeList(self,Message:str,treelist_height:int,treelist_dict:dict) -> tuple:
        """
        依旧是一个选择框，以树状显示，不会显示TAG

        :param Message: 消息文本
        :param treelist_height: 列表高度
        :param treelist_dict: 一个字典
        example: {'tag1':['name1','On / Off','位于树结构的具体深度值']}
        :return: 返回一个元组 包含 状态码 和用户选择的TAG
        """
        cmd = [] + self.cmd
        cmd.insert(4, '--treeview')
        cmd.insert(5, Message)
        cmd.append(str(treelist_height))
        out = Shell(__DICT_Style_3__(cmd,treelist_dict))
        return out.returncode, out.stdout.decode('utf-8')

# TODO: add more function
# --form         <text> <height> <width> <form height> <label1> <l_y1> <l_x1> <item1> <i_y1> <i_x1> <flen1> <ilen1>...
# --mixedform    <text> <height> <width> <form height> <label1> <l_y1> <l_x1> <item1> <i_y1> <i_x1> <flen1> <ilen1> <itype>...
# --passwordform <text> <height> <width> <form height> <label1> <l_y1> <l_x1> <item1> <i_y1> <i_x1> <flen1> <ilen1>...

# --programbox   <text> <height> <width>
# --progressbox  <text> <height> <width>
