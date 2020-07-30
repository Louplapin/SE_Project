import sys
import tkinter as tk

class Data_tree:
    branch = []
    def __init__(self, name):
        self.name = name.split(', ')[1]
        self.number = name.split(', ')[0]
    def addBranch(self, number):
        self.branch=number
    def addHigh(self, number):
        self.high=number




root = tk.Tk()
root.title(u"SE_Projects")
root.geometry('600x400')

#--------クリックイベント--------#
def click_word(event) :
    print(event.widget['text'])
#-------------------------------#

#----------------------------------------------------------------------------------#
canvas = tk.Canvas(root)

#縦方向スクロール
vertical_bar = tk.Scrollbar(root, orient=tk.VERTICAL)
vertical_bar.pack(side=tk.RIGHT, fill=tk.Y)
vertical_bar.config(command=canvas.yview)

#横方向スクロール
horizontal_bar = tk.Scrollbar(root, orient=tk.HORIZONTAL)
horizontal_bar.pack(side=tk.BOTTOM, fill=tk.X)
horizontal_bar.config(command=canvas.xview)

#Canvasのサイズ変更をScrollbarに通知
canvas.config(yscrollcommand=vertical_bar.set, xscrollcommand=horizontal_bar.set)
#スクロールの範囲(x_min, y_min, x_max, y_max)
canvas.config(scrollregion=(0,0,1500,2000))
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Frame Widgetを生成
frame = tk.Frame(canvas)

# Frame Widgetを Canvas Widget上に配置（）
canvas.create_window((0,0), window=frame, anchor=tk.NW, width=2000, height=2000)
#----------------------------------------------------------------------------------#

File_data = open(sys.argv[1], "r", encoding='utf-8')
txt = File_data.read()

tree=txt.split('trees:')[1].split('nodes:')[0]
treelist = list(tree.split('\n'))
treelist = [a for a in treelist if a != '']

nodes= (txt.split('nodes:')[1]).split('branches:')[0]
nodeslist = list(nodes.split('\n'))

branches=txt.split('branches:')[1]
brancheslist = list(branches.split('\n'))
brancheslist = [a for a in brancheslist if a != '']

data = [Data_tree(node) for node in nodeslist if node != '']
[d.addBranch([br.split(', ')[1] for br in brancheslist if br.startswith(d.number+',')]) for d in data]
[d.addHigh([t.count('|--') for t in treelist if t.endswith(d.name)][0]) for d in data]
for d in data: print(d.number, d.name, d.branch, d.high)

for d in data:
    Static = tk.Label(frame, text=d.name, relief="solid", font=("MS Serif",12))
    Static.pack(anchor='w',expand=1)
    #イベントハンドラー
    Static.bind("<Button-1>", lambda event: click_word(event))


root.mainloop()
