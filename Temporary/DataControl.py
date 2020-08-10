#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import time
import tkinter as tk
import treeClass as trees
import lineClass as lines
import input
import view

"""
描画を行う前段階であったり、描画に必要なデータを用意する
"""

def makeData(treelist, nodeslist, brancheslist, frame):
    """
    inputで読み込んだデータを整理するとともに、見えない位置にlabelの描画を行い、labelの幅を得る
    """
    data = [trees.tree(a) for a in range(1, len(nodeslist) + 1)]
    [d.addName([node.split(', ')[1] for node in nodeslist if node.startswith(str(d.number)+',')][0]) for d in data]
    [d.addBranch([int(br.split(', ')[1]) for br in brancheslist if br.startswith(str(d.number)+',')]) for d in data]
    [d.addBranch([a for _,a in sorted(zip([data[nums-1].name for nums in d.branch],d.branch))]) for d in data]
    [d.addFronts([int(br.split(', ')[0]) for br in brancheslist if br.endswith(' '+str(d.number))]) for d in data]
    [d.addHigh([t.count('|--') for t in treelist if t.startswith(d.name) or t.endswith(' '+d.name)][0]) for d in data]
    [d.xypoint(-26, 0) for d in data]
    [d.addWidth(view.temporary(d,frame)) for d in data]
    return data

def drowVerticals(data, frame, canvas):
    """
    縦一列の描画を行う。
    """
    [d.xypoint((d.number-1)*24, 0) for d in data if d.high != -1]
    [view.moveLabel(d, frame) for d in data if d.high != -1]
    
    l_data = [lines.line(lname) for lname in sum([["{0}to{1}".format(d.number,nums) for nums in d.branch] for d in data if d.high != -1], [])]
    [l_d.addpoints(data[int(l_d.name.split("to")[0])-1].bpoint(), data[int(l_d.name.split("to")[1])-1].fpoint()) for l_d in l_data]
    [view.drawline(l_d, canvas) for l_d in l_data]

def drowTrees(data, high, height, width, num, frame, canvas):
    """
    木の描画を再起的に行う
    """
    y = height
    if data[num-1].x == 0:
        data[num-1].xypoint(height, max(width, data[num-1].x))
    else:
        data[num-1].xypoint(min(height, data[num-1].y), max(width, data[num-1].x))

    view.moveLabel(data[num-1], frame)
    dr_l = [lines.line("{0}to{1}".format(num,nums)) for nums in data[num-1].branch if data[num-1].high != -1] + [lines.line("{0}to{1}".format(nums,num)) for nums in data[num-1].front]
    [l_d.addpoints(data[int(l_d.name.split("to")[0])-1].bpoint(), data[int(l_d.name.split("to")[1])-1].fpoint()) for l_d in dr_l]
    [view.drawline(l_d, canvas) for l_d in dr_l]

    if len(data[num-1].branch) == 0: return y + 26
    for nums in data[num-1].branch:
        y = drowTrees(data, high + 1, y , width + data[num-1].width + 25, nums, frame, canvas)
    data[num-1].xypoint(height+(y-height-24)/2, width)

    view.moveLabel(data[num-1], frame)
    dr_l = [lines.line("{0}to{1}".format(num,nums)) for nums in data[num-1].branch if data[num-1].high != -1] + [lines.line("{0}to{1}".format(nums,num)) for nums in data[num-1].front]
    [l_d.addpoints(data[int(l_d.name.split("to")[0])-1].bpoint(), data[int(l_d.name.split("to")[1])-1].fpoint()) for l_d in dr_l]
    [view.drawline(l_d, canvas) for l_d in dr_l]

    return y

