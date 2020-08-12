#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class line:
    """
    クラスの説明
    label間の線を引く際に必要なデータを用意する
    """
    def __init__(self, name):
        self.name = name
    def addpoints(self, bpoint, fpoint):
        self.bx = bpoint[0]
        self.by = bpoint[1]
        self.fx = fpoint[0]
        self.fy = fpoint[1]
