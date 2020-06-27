import sys
import tkinter as tk

root = tk.Tk()
root.title(u"SE_Projects")
root.geometry('600x400')

test_text='スーツケースを格安で購入する場合、皆さんならまずスーツケースのどの部分を見ますか？スーツケースを選ぶ際に抑えておきたいポイントは「デザイン」「重さ」「大きさ」「ブランド」の4つです。格安で購入するためにはその4つのポイントのどの点を妥協するか、ということになります。まずは、4つのポイントをそれぞれ説明しましょう。'

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

tree=txt.split('nodes:')[0]
treelist = list(tree.split('\n'))

nodes= (txt.split('nodes:')[1]).split('branches:')[0]
nodeslist = list(nodes.split('\n'))
nodeslist.remove('')

branches=txt.split('branches:')[1]
brancheslist = list(branches.split('\n'))

#横スクロール確認用-------------------------
Static = tk.Label(frame, text=test_text)
Static.pack(anchor='w',expand=1)
Static.bind("<Button-1>", lambda event: click_word(event))
#-----------------------------------------

for node in nodeslist:
    Static = tk.Label(frame, text=node, font=("MS Serif",12))
    Static.pack(anchor='w',expand=1)
    #イベントハンドラー
    Static.bind("<Button-1>", lambda event: click_word(event))

root.mainloop()