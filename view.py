import sys
import tkinter as tk

root = tk.Tk()
root.title(u"SE_Projects")
root.geometry('600x400')

File_data = open(sys.argv[1], "r", encoding='utf-8')
txt = File_data.read()

tree=txt.split('nodes:')[0]
treelist = list(tree.split('\n'))

nodes= (txt.split('nodes:')[1]).split('branches:')[0]
nodeslist = list(nodes.split('\n'))
nodeslist.remove('')

branches=txt.split('branches:')[1]
brancheslist = list(branches.split('\n'))

for node in nodeslist:
    Static = tk.Label(text=node)
    Static.pack(anchor='w',expand=1)

root.mainloop()