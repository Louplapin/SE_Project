#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ここに、プログラム全体の説明を記載
て
す
と
"""

__author__ = "Author Name"
__status__ = "SE_Project"
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
def drawline(data):
    for d in data:
        b_point = d.bpoint()
        branches = d.branch
        for branch in branches:
            f_point = data[branch-1].fpoint()
            canvas.create_line(b_point[0], b_point[1], f_point[0], f_point[1], fill='black')
            canvas.update()
#-------------------------------#

#-------------再描画-------------#
def treeXYWrite(data, high, height, width, number, children):
    if high != data[number-1].high:
        return height + 24
    x = height
    data[number-1].xypoint(height, max(width, data[number-1].x))

    root.after(10)
    if data[number-1].name != 'null':
        children[number-1].place(x=data[number-1].x,y=data[number-1].y)
        root.update()
    canvas.delete("all")
    drawline(data)

    if len(data[number-1].branch) == 0: return x + 24
    for num in data[number-1].branch:
        x = treeXYWrite(data, high + 1, x , width+data[number-1].width + 25, num, children)
    data[number-1].xypoint(height+(x-height-24)/2, width)

    root.after(10)
    if data[number-1].name != 'null':
        children[number-1].place(x=data[number-1].x,y=data[number-1].y)
        root.update()
    canvas.delete("all")
    drawline(data)

    return x
#-------------------------------#

#-----nullデータの作成-----------#
def makeTopData(data):
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
scroll_canvas.config(scrollregion=(0,0,1500,2000))
scroll_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

main_frame = tk.Frame(scroll_canvas)

scroll_canvas.create_window((0,0), window=main_frame, anchor=tk.NW, width=2000, height=2000)
#-------------------------------#

canvas = tk.Canvas(main_frame, width=1000, height=1200)
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

drawline(data)

data.append(makeTopData(data))

children = main_frame.winfo_children()
del children[0]

treeXYWrite(data, -1, 0, -25, len(data),children)
m = max([d.bpoint()[1] for d in data])
# 領域の最大値ください。 → ＋20pxぐらい足しゃーいいよ -> mが領域の最大値になってると思う(横幅)
# 高さの方は、listの数(data)x26くらいでいい感じになると思うよ
# scroll_canvas.config(scrollregion=(0,0,x_max,y_max))
scroll_canvas.config(scrollregion=(0,0,1200,1200))

root.mainloop()
