#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class tree:
    """
    クラスの説明
    入力データを整理する。
    また、labelに関する座標などを保存する
    """
    branch = []
    front = []
    def __init__(self, number):
        self.number = number
        self.addName("null")
        self.addHigh(-1)
        self.addWidth(0)
        self.xypoint(0,-25)
        
    def addName(self, name):
        self.name = name
    def addBranch(self, number):
        self.branch=number
    def addFronts(self, number):
        self.front=number
    def addHigh(self, number):
        self.high=number
    def addWidth(self, number):
        self.width=number
    def xypoint(self, y, x):
        self.x = x;
        self.y = y;
    def fpoint(self):
        return self.x, self.y + 12
    def bpoint(self):
        return self.x + self.width, self.y + 12
