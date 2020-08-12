#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def fileReed():
    """
    ファイル名が与えられるとそのファイルの中身をtxtに代入し、
    「trees:」、「nodes:」、「branches:」のデータに
    それぞれ分割を行う。
    分割されたものに対して改行で分割を行いlistに格納する
    listの中から空の要素を取り除く
    """
    File_data = open(sys.argv[1], "r", encoding='utf-8')
    txt = File_data.read()

    tree=txt.split('trees:')[1].split('nodes:')[0]
    treelist = list(tree.split('\n'))
    treelist = [a for a in treelist if a != '']

    nodes= (txt.split('nodes:')[1]).split('branches:')[0]
    nodeslist = list(nodes.split('\n'))
    nodeslist = [a for a in nodeslist if a != '']

    branches=txt.split('branches:')[1]
    brancheslist = list(branches.split('\n'))
    brancheslist = [a for a in brancheslist if a != '']

    return treelist, nodeslist, brancheslist
