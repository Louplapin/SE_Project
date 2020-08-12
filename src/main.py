#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
令和２年度春学期ソフトウェア工学Ⅱ長期課題「樹状整列」を行うプログラミング

目標性能：使用するフォントはSerif系の標準体（プレーン）で12ポイント
　　　　　ノードやリーフの整列間隔は横方向が25ピクセルで縦方向が2ピクセル
　　　　　マウスのドラッグ操作より軽快にスクロールできる
　　　　　マウスでクリックすることにより標準出力へ当該の名前を書き出す

制限事項：Pyrhon標準ライブラリ「Tkinter」を使用して開発を行う
　　　　　ダウンロード、開発したアプリケーションはLinuxやWindowsなどでも動作することができる
"""

__author__ = "Kawamura Rion, Saito Ryunosuke, Nobuta Katsuhito"
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
    """
	樹状整列を行うメインプログラム
	"""

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

