## 一个基于 Dialog 的 Python TUI
[ENGLISH](README_EN.MD) - **By Google Translate**

通过把 Dialog 的各种参数抽象到 Python 的函数中
在 Python 中更方便的调用
本质还是通过运行 Dialog 命令并附加参数然后通过管道获取输出的内容

支持平台: Linux,Unix,macOS

### 目前支持
- MessageBox (--msgbox)
- InfoBox (--infobox)
- TextBox (--textbox)
- YesNoBox (--yesno)
- Menu (--menu)
- InputBox (--inputbox)
- PasswordBox (--passwordbox)
  - 默认启用 * 来代替输入的字符显示 (--insecure)
- TwoChoseList (--buildlist)
- DataChose (--calendar)
- CheckList (--checklist)
- DirectoryChose (--dselect)
- EditBox (--editbox)
- FileSelect (--fselect)

### 如何使用?
请先安装 Dialog 在你的运行或开发环境中

然后将 [DialogTUI.py](./DialogTUI.py) 复制到你的项目中

然后在同级目录创建一个Python文件，键入
```python
import DialogTUI as ui

out = ui.Window(
  'Window Title',
  20, 
  30 # 
).MessageBox(
  'Hello World!'# 文本
) 
print(out) # 在命令执行完成后返回一个状态码 
```

### 指南
[一个小例子](./example.py)

| 状态码 | 含义  |
|-----|-----|
| 0   | 确认  |
| 1   | 取消  |
| 255 | ESC |

### License
[MIT](License.txt)
