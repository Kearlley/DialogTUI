#!/bin/env python
# *-- coding:utf-8 --*
import subprocess as sp


# Return Code:
# 0 => OK
# 1 => Close
# 255 => ESC

# cmd = f"dialog --title {self.title} --xxxx {pub.ToStr(Message)} {self.height} {self.width}" (This a backup)

def Shell(cmd):
    """
    运行一个命令

    :type cmd: list
    :param cmd: 命令
    :return:
    """
    return sp.run(cmd, stdout=sp.PIPE)


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

    def MessageBox(self, Message):
        """
        消息窗体

        :type Message: str
        :param Message: 信息文本

        :return: 状态码
        :rtype: int
        """
        cmd = self.cmd
        cmd.insert(4, '--msgbox')
        cmd.insert(5, Message)
        out = Shell(cmd)
        return out.returncode

    def InfoBox(self, Message):
        """
        提示信息窗体

        :type Message: str
        :param Message: 消息文本

        :return: 状态码
        :rtype: int
        """
        cmd = self.cmd
        cmd.insert(4, '--infobox')
        cmd.insert(5, Message)
        out = Shell(cmd)
        return out.returncode

    def TextBox(self, file):
        """
        文本窗体

        :type file: str
        :param file: 文件路径

        :return: 状态码
        :rtype: int
        """
        cmd = self.cmd
        cmd.insert(4, '--textbox')
        cmd.insert(5, file)
        out = Shell(cmd)
        return out.returncode

    def YesNoBox(self, Message):
        """
        Yes or No 选择窗体

        :type Message: str
        :param Message: 消息文本

        :return: 状态码
        :rtype: int
        """
        cmd = self.cmd
        cmd.insert(4, '--yesno')
        cmd.insert(5, Message)
        out = Shell(cmd)
        return out.returncode

    def Menu(self, Message, menu_height, menu_list):
        """
        菜单窗体

        :type Message: str
        :param Message: 消息文本

        :type menu_height: int
        :param menu_height: 菜单高度

        :type menu_list: dict
        :param menu_list: 菜单字典
        {'tag1':'name','tag2':'name'}

        :returns: 状态码 用户选择的 TAG 值
        :rtype: list
        """
        cmd = self.cmd
        cmd.insert(4, '--menu')
        cmd.insert(5, Message)
        cmd.append(str(menu_height))
        for lists in menu_list:
            cmd.append(lists)
            cmd.append(menu_list[lists])
        out = Shell(cmd)
        return out.returncode, out.stdout.decode('utf-8')

    def InputBox(self, Message,args=None):
        """
        输入框

        :type args: str
        :param args: 初始内容 [可选]

        :type Message: str
        :param Message: 消息文本

        :return: 状态码 用户输入信息
        :rtype: list
        """
        cmd = self.cmd
        cmd.insert(4, '--inputbox')
        cmd.insert(5, Message)
        if args is not None:
            cmd.append(args)
        out = Shell(cmd)
        return out.returncode, out.stdout.decode('utf-8')

    def PasswordBox(self, Message,args=None):
        """
        密码框

        :type Message: str
        :param Message: 消息文本

        :type args: str
        :param args: 初始内容 [可选]

        :return: 状态码 用户输入信息
        :rtype: list
        """
        cmd = self.cmd
        cmd.insert(4, '--insecure')
        cmd.insert(5, '--passwordbox')
        cmd.insert(6, Message)
        if args is not None:
            cmd.append(args)
        out = Shell(cmd)
        return out.returncode, out.stdout.decode('utf-8')

# TODO: add more function
# --buildlist    <text> <height> <width> <list-height> <tag1> <item1> <status1>...
# --calendar     <text> <height> <width> <day> <month> <year>
# --checklist    <text> <height> <width> <list height> <tag1> <item1> <status1>...
# --dselect      <directory> <height> <width>
# --editbox      <file> <height> <width>
# --form         <text> <height> <width> <form height> <label1> <l_y1> <l_x1> <item1> <i_y1> <i_x1> <flen1> <ilen1>...
# --fselect      <filepath> <height> <width>
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

