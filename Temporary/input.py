#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ここに、プログラム全体の説明を記載
"""

def InputFile():
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
