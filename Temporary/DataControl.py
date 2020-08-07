#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import tkinter as tk

def createGeometry(title, size):
    root = tk.Tk()
    root.title(title)
    root.geometry(size)
    return root

def createScroll(layer, x, y):
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
    canvas = tk.Canvas(layer, width=2000, height=2000)
    canvas.pack(fill=tk.BOTH)
    
    return canvas

def canvasConfig(layer, x, y):
    layer.config(scrollregion=(0,0,x,y))

