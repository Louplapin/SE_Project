File_data = open("forest.txt", "r", encoding='utf-8')
txt = File_data.read()

tree=txt.split('nodes:')[0]
treelist = list(tree.split('\n'))
print(treelist)



nodes= (txt.split('nodes:')[1]).split('branches:')[0]
nodeslist = list(nodes.split('\n'))
nodeslist.remove('')
print(nodeslist)


branches=txt.split('branches:')[1]
brancheslist = list(branches.split('\n'))
print(brancheslist)
#print(tree , nodes, branches)

