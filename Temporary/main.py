#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ここに、プログラム全体の説明を記載
"""

__author__ = "Author Name"
__version__ = "1.0"
__date__    = "06 August 2020"

import time
import tkinter as tk
import treeClass as trees
import lineClass as lines
import input
import DataControl

#root = DataControl.createGeometry("SE_Projects",'600x400')

#--------クリックイベント--------#
def click_word(event) :
    """
    関数の説明
    """
    print(event.widget['text'])
#-------------------------------#

#---------縦に描画---------------#
def verticalView(datas, roots, root):
    static = tk.Label(roots, text=datas.name, relief="solid", font=("MS Serif",12))
    static.place(x = datas.x, y = datas.y)
    static.bind("<Button-1>", lambda event: click_word(event))
    roots.update_idletasks()
    #########遅延##############
    root.after(20)
    root.update()
    #######################
    return static.winfo_width()
#-------------------------------#

#---------線の描画---------------#
def drawline(l_data, canvas):
    for l_d in l_data:
        canvas.delete(canvas.find_withtag(l_d.name))
        canvas.create_line(l_d.bx, l_d.by, l_d.fx, l_d.fy, fill='black', tag = l_d.name)
        canvas.update()
#-------------------------------#

#-------------再描画-------------#
def treeXYWrite(data, high, height, width, num, children, canvas, root):
    x = height
    if data[num-1].x == 0:
        data[num-1].xypoint(height, max(width, data[num-1].x))
    else:
        data[num-1].xypoint(min(height, data[num-1].y), max(width, data[num-1].x))

    root.after(10)
    if data[num-1].name != 'null':
        children[num-1].place(x=data[num-1].x,y=data[num-1].y)
        root.update()
        dr_l = [lines.line("{0}to{1}".format(num,nums)) for nums in data[num-1].branch] + [lines.line("{0}to{1}".format(nums,num)) for nums in data[num-1].front]
        [l_d.addpoints(data[int(l_d.name.split("to")[0])-1].bpoint(), data[int(l_d.name.split("to")[1])-1].fpoint()) for l_d in dr_l]
        drawline(dr_l, canvas)

    if len(data[num-1].branch) == 0: return x + 26
    for nums in data[num-1].branch:
        x = treeXYWrite(data, high + 1, x , width + data[num-1].width + 25, nums, children, canvas, root)
    data[num-1].xypoint(height+(x-height-24)/2, width)

    root.after(10)
    if data[num-1].name != 'null':
        children[num-1].place(x=data[num-1].x,y=data[num-1].y)
        root.update()
        dr_l = [lines.line("{0}to{1}".format(num,nums)) for nums in data[num-1].branch] + [lines.line("{0}to{1}".format(nums,num)) for nums in data[num-1].front]
        [l_d.addpoints(data[int(l_d.name.split("to")[0])-1].bpoint(), data[int(l_d.name.split("to")[1])-1].fpoint()) for l_d in dr_l]
        drawline(dr_l, canvas)

    return x
#-------------------------------#

def main():

    root = DataControl.createGeometry("SE_Projects",'600x400')

    scroll_canvas, main_frame = DataControl.createScroll(root, 2000, 2000)

    canvas = DataControl.createCanvas(main_frame, 2000, 2000)

    treelist, nodeslist, brancheslist = input.fileReed()

    data = [trees.tree(a) for a in range(1, len(nodeslist) + 1)]
    [d.addName([node.split(', ')[1] for node in nodeslist if node.startswith(str(d.number)+',')][0]) for d in data]
    [d.addBranch([int(br.split(', ')[1]) for br in brancheslist if br.startswith(str(d.number)+',')]) for d in data]
    [d.addBranch([a for _,a in sorted(zip([data[nums-1].name for nums in d.branch],d.branch))]) for d in data]
    [d.addFronts([int(br.split(', ')[0]) for br in brancheslist if br.endswith(' '+str(d.number))]) for d in data]
    [d.addHigh([t.count('|--') for t in treelist if t.startswith(d.name) or t.endswith(' '+d.name)][0]) for d in data]
    [d.xypoint((d.number-1)*24, 0) for d in data]
    [d.addWidth(verticalView(d,main_frame, root)) for d in data]

    l_data = [lines.line(lname) for lname in sum([["{0}to{1}".format(d.number,nums) for nums in d.branch] for d in data], [])]
    [l_d.addpoints(data[int(l_d.name.split("to")[0])-1].bpoint(), data[int(l_d.name.split("to")[1])-1].fpoint()) for l_d in l_data]
    drawline(l_data, canvas)

    top_data = trees.tree(0)
    top_data.addBranch([d.number for d in data if d.high == 0])
    data.append(top_data)

    children = main_frame.winfo_children()
    del children[0]

    treeXYWrite(data, -1, 0, -25, len(data),children, canvas, root)
    max_x = max([d.bpoint()[0] for d in data]) + 26
    max_y = max([d.bpoint()[1] for d in data]) + 26
    DataControl.canvasConfig(scroll_canvas, max_x, max_y)

    root.mainloop()

if __name__ == '__main__':
    main()

