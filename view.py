import sys
import tkinter as tk

root = tk.Tk()
root.title(u"SE_Projects")
root.geometry('600x400')

#----------------------------------------------------------------------------------#
canvas = tk.Canvas(root)

bar = tk.Scrollbar(root, orient=tk.VERTICAL)
bar.pack(side=tk.RIGHT, fill=tk.Y)
bar.config(command=canvas.yview) # ScrollbarでCanvasを制御

# Canvas Widget をTopWidget上に配置
canvas.config(yscrollcommand=bar.set) # Canvasのサイズ変更をScrollbarに通知
canvas.config(scrollregion=(0,0,500,2000)) #スクロール範囲
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Frame Widgetを生成
frame = tk.Frame(canvas)

# Frame Widgetを Canvas Widget上に配置（）
canvas.create_window((0,0), window=frame, anchor=tk.NW, width=2000, height=2000)

#----------------------------------------------------------------------------------#

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
    Static = tk.Label(frame, text=node)
    Static.pack(anchor='w',expand=1)

root.mainloop()