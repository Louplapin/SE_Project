#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
windowの作成やlabelの描画、移動など描画を行う関数
"""

import tkinter as tk

def createGeometry(title, size):
    """
    最初のwindowのサイズとタイトルを指定して作成させる
    """
    root = tk.Tk()
    root.title(title)
    root.geometry(size)
    return root

def createScroll(layer, x, y):
    """
    縦と横のスクロールバーを作成する
    scroll_canvasとmain_frameを返す
    """
    scroll_canvas = tk.Canvas(layer)
    
    vertical_bar = tk.Scrollbar(layer, orient=tk.VERTICAL)
    vertical_bar.pack(side=tk.RIGHT, fill=tk.Y)
    vertical_bar.config(command=scroll_canvas.yview)

    horizontal_bar = tk.Scrollbar(layer, orient=tk.HORIZONTAL)
    horizontal_bar.pack(side=tk.BOTTOM, fill=tk.X)
    horizontal_bar.config(command=scroll_canvas.xview)
    
    scroll_canvas.config(yscrollcommand=vertical_bar.set, xscrollcommand=horizontal_bar.set)
    
    scroll_canvas.config(scrollregion=(0,0,x,y))
    scroll_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    main_frame = tk.Frame(scroll_canvas)

    scroll_canvas.create_window((0,0), window=main_frame, anchor=tk.NW, width=x, height=y)
    
    return scroll_canvas, main_frame
    
def createCanvas(layer, x, y):
    """
    指定したframeに対してcanvasを作成する
    """
    canvas = tk.Canvas(layer, width=2000, height=2000)
    canvas.pack(fill=tk.BOTH)
    
    return canvas

def canvasConfig(layer, x, y):
    """
    canvasのサイズを変更する
    """
    layer.config(scrollregion=(0,0,x,y))

def click_word(event) :
    """
    labelがクリックされたときにそのラベルのtextを標準出力する
    """
    print(event.widget['text'])

def temporary(datas, frame):
    """
    labelを仮配置する。その際にイベント設定とlabelの幅を得る
    """
    static = tk.Label(frame, text=datas.name, relief="solid", font=("MS Serif",12))
    static.place(x = datas.x, y = datas.y)
    static.bind("<Button-1>", lambda event: click_word(event))
    frame.update_idletasks()
    frame.update()
    return static.winfo_width()

def moveLabel(data, frame):
    """
    labelを移動させる
    """
    child = frame.winfo_children()
    if data.high == -1: return
    child[data.number].place(x=data.x,y=data.y)
    frame.update()

def drawline(l_d, canvas):
    """
    label間の線を描く
    """
    canvas.delete(canvas.find_withtag(l_d.name))
    canvas.create_line(l_d.bx, l_d.by, l_d.fx, l_d.fy, fill='black', tag = l_d.name)
    canvas.update()
