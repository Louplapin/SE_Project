#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ここに、プログラム全体の説明を記載
"""

__author__ = "Author Name"
__version__ = "1.0"
__date__    = "06 August 2020"

import sys
import time
import tkinter as tk

class Data_tree:
    branch = []
    front = []
    def __init__(self, name):
        self.name = name.split(', ')[1]
        self.number = int(name.split(', ')[0])
    def addBranch(self, number):
        self.branch=number
    def addFronts(self, number):
        self.front=number
    def addHigh(self, number):
        self.high=number
    def addWidth(self, number):
        self.width=number
    def verticalView(self, roots):
        static = tk.Label(roots, text=self.name, relief="solid", font=("MS Serif",12))
        static.place(x = self.x, y = self.y)
        static.bind("<Button-1>", lambda event: click_word(event))
        roots.update_idletasks()
        self.addWidth(static.winfo_width())
        #########遅延##############
        root.after(20)
        root.update()
        #######################
    def xypoint(self, y, x):
        self.x = x;
        self.y = y;
    def fpoint(self):
        return self.x, self.y + 12
    def bpoint(self):
        return self.x + self.width, self.y + 12

class lines:
    def __init__(self, name):
        self.name = name
    def addpoints(self, bpoint, fpoint):
        self.bx = bpoint[0]
        self.by = bpoint[1]
        self.fx = fpoint[0]
        self.fy = fpoint[1]

root = tk.Tk()
root.title(u"SE_Projects")
root.geometry('600x400')

#--------クリックイベント--------#
def click_word(event) :
    """
    関数の説明
    """
    print(event.widget['text'])
#-------------------------------#

#---------線の描画---------------#
def drawline(l_data):
    for l_d in l_data:
        canvas.delete(canvas.find_withtag(l_d.name))
        canvas.create_line(l_d.bx, l_d.by, l_d.fx, l_d.fy, fill='black', tag = l_d.name)
        canvas.update()
#-------------------------------#

#-------------再描画-------------#
def treeXYWrite(data, high, height, width, num, children):
    x = height
    if len(data[num-1].front):
        data[num-1].xypoint(height, max(width, data[num-1].x))
    else:
        data[num-1].xypoint(min(height, data[num-1].y), max(width, data[num-1].x))

    root.after(10)
    if data[num-1].name != 'null':
        children[num-1].place(x=data[num-1].x,y=data[num-1].y)
        root.update()
        dr_l = [lines("{0}to{1}".format(num,nums)) for nums in data[num-1].branch] + [lines("{0}to{1}".format(nums,num)) for nums in data[num-1].front]
        [l_d.addpoints(data[int(l_d.name.split("to")[0])-1].bpoint(), data[int(l_d.name.split("to")[1])-1].fpoint()) for l_d in dr_l]
        drawline(dr_l)

    if len(data[num-1].branch) == 0: return x + 26
    for nums in data[num-1].branch:
        x = treeXYWrite(data, high + 1, x , width + data[num-1].width + 25, nums, children)
    data[num-1].xypoint(height+(x-height-24)/2, width)

    root.after(10)
    if data[num-1].name != 'null':
        children[num-1].place(x=data[num-1].x,y=data[num-1].y)
        root.update()
        dr_l = [lines("{0}to{1}".format(num,nums)) for nums in data[num-1].branch] + [lines("{0}to{1}".format(nums,num)) for nums in data[num-1].front]
        [l_d.addpoints(data[int(l_d.name.split("to")[0])-1].bpoint(), data[int(l_d.name.split("to")[1])-1].fpoint()) for l_d in dr_l]
        drawline(dr_l)

    return x
#-------------------------------#

#-----nullデータの作成-----------#
def makeTopData():
    t_data = Data_tree("0, null")
    t_data.addBranch([d.number for d in data if d.high == 0])
    t_data.addHigh(-1)
    t_data.addWidth(0)
    t_data.xypoint(0,-25)
    return t_data

#-------------------------------#

#----------スクロール------------#
scroll_canvas = tk.Canvas(root)

#縦方向スクロール
vertical_bar = tk.Scrollbar(root, orient=tk.VERTICAL)
vertical_bar.pack(side=tk.RIGHT, fill=tk.Y)
vertical_bar.config(command=scroll_canvas.yview)

#横方向スクロール
horizontal_bar = tk.Scrollbar(root, orient=tk.HORIZONTAL)
horizontal_bar.pack(side=tk.BOTTOM, fill=tk.X)
horizontal_bar.config(command=scroll_canvas.xview)

#スクロールの通知
scroll_canvas.config(yscrollcommand=vertical_bar.set, xscrollcommand=horizontal_bar.set)
#スクロールの範囲(x_min, y_min, x_max, y_max)
scroll_canvas.config(scrollregion=(0,0,2000,2000))
scroll_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

main_frame = tk.Frame(scroll_canvas)

scroll_canvas.create_window((0,0), window=main_frame, anchor=tk.NW, width=2000, height=2000)
#-------------------------------#

canvas = tk.Canvas(main_frame, width=2000, height=2000)
canvas.pack(fill=tk.BOTH)

File_data = open(sys.argv[1], "r", encoding='utf-8')
txt = File_data.read()

tree=txt.split('trees:')[1].split('nodes:')[0]
treelist = list(tree.split('\n'))
treelist = [a for a in treelist if a != '']

nodes= (txt.split('nodes:')[1]).split('branches:')[0]
nodeslist = list(nodes.split('\n'))

branches=txt.split('branches:')[1]
brancheslist = list(branches.split('\n'))
brancheslist = [a for a in brancheslist if a != '']

data = [Data_tree(node) for node in nodeslist if node != '']
[d.addBranch([int(br.split(', ')[1]) for br in brancheslist if br.startswith(str(d.number)+',')]) for d in data]
[d.addBranch([a for _,a in sorted(zip([data[nums-1].name for nums in d.branch],d.branch))]) for d in data]
[d.addFronts([int(br.split(', ')[0]) for br in brancheslist if br.endswith(' '+str(d.number))]) for d in data]
[d.addHigh([t.count('|--') for t in treelist if t.startswith(d.name) or t.endswith(' '+d.name)][0]) for d in data]
[d.xypoint((d.number-1)*24, 0) for d in data]
[d.verticalView(main_frame) for d in data]

l_data = [lines(lname) for lname in sum([["{0}to{1}".format(d.number,nums) for nums in d.branch] for d in data], [])]
[l_d.addpoints(data[int(l_d.name.split("to")[0])-1].bpoint(), data[int(l_d.name.split("to")[1])-1].fpoint()) for l_d in l_data]

drawline(l_data)

data.append(makeTopData())

children = main_frame.winfo_children()
del children[0]

treeXYWrite(data, -1, 0, -25, len(data),children)
max_x = max([d.bpoint()[0] for d in data]) + 26
max_y = max([d.bpoint()[1] for d in data]) + 26
scroll_canvas.config(scrollregion=(0,0,max_x,max_y))

root.mainloop()
