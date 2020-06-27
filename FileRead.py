import sys

File_data = open(sys.argv[1], "r", encoding='utf-8')
txt = File_data.read()

tree=txt.split('nodes:')[0]
nodes= (txt.split('nodes:')[1]).split('branches:')[0]
branches=txt.split('branches:')[1]
print(tree , nodes, branches)