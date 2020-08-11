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
import view

def main():

    root = view.createGeometry("SE_Projects",'600x400')

    scroll_canvas, main_frame = view.createScroll(root, 2000, 2000)

    canvas = view.createCanvas(main_frame, 2000, 2000)

    treelist, nodeslist, brancheslist = input.fileReed()

    data = DataControl.makeData(treelist, nodeslist, brancheslist, main_frame)
    
    top_data = trees.tree(len(data))
    top_data.addBranch([d.number for d in data if d.high == 0])
    data.append(top_data)
    
    DataControl.drowVerticals(data, main_frame, canvas)
    
    DataControl.drowTrees(data, -1, 0, -25, len(data), len(data[-1].branch), main_frame, canvas)
    
    max_x = max([d.bpoint()[0] for d in data]) + 26
    max_y = max([d.bpoint()[1] for d in data]) + 26
    view.canvasConfig(scroll_canvas, max_x, max_y)

    root.mainloop()

if __name__ == '__main__':
    main()

