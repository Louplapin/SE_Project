#import treeClass
import sys

class Data_tree:
    child = []
    high = 0
    def __init__(self, name):
        self.name = name;
    def coordinate(self,x,y):
        self.x = x;
        self.y = y;
    def addList(self, child):
        self.child.append(child);
    def write(self,num,h):
        while(num < len(treelist)):
            if(treelist[num].count('|--') == h):
                self.addList(Data_tree(treelist[num].split(' ')[h]))
                high = h
                num += 1
            elif(treelist[num].count('|--') == h + 1):
                num = self.child[-1].write(num,h+1);
            else:
                return num
    def xywrite(self, ):
    


File_data = open(sys.argv[1], "r", encoding='utf-8')
txt = File_data.read()

tree=(txt.split('trees:')[1]).split('nodes:')[0]
treelist = list(tree.split('\n'))
treelist.remove('')
print(treelist)

nodes= (txt.split('nodes:')[1]).split('branches:')[0]
nodeslist = list(nodes.split('\n'))
nodeslist.remove('')
#print(nodeslist)

branches=txt.split('branches:')[1]
brancheslist = list(branches.split('\n'))
#print(brancheslist)
#print(tree , nodes, branches)

tree = Data_tree(treelist[0])
tree.write(0,0)

