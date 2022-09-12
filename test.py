#!/bin/python
# *-- coding:utf-8 --*
import DialogTUI as ui

window = ui.Window('Test Title', 20, 30)

test_fun = window.TwoChoseList('Test Msg', 10, {'tag1': ['name1', 'Off'],'tag2':['name2','On']})
print(test_fun)  # Return
