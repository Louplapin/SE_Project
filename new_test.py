File_data = open("forest.txt", "r", encoding='utf-8')
txt = File_data.read()

tree=txt.split('nodes:')[0]
treelist = list(tree.split('\n'))

#creat nodelist and map
#init map
nodemap = {}
#cut string
nodes= (txt.split('nodes:')[1]).split('branches:')[0]
#creat list
nodeslist = list(nodes.split('\n'))
#delete space
nodeslist.remove('')
nodeslist.remove('')
#creat map
for index,char in enumerate(nodeslist):
    name = char.split()
    nodemap.update({index:name[1]})
#output map example
print(nodemap[1])

branchemap = {}
branches=txt.split('branches:')[1]
brancheslist = list(branches.split('\n'))
brancheslist.remove('')
for char in brancheslist:
    name = char.split(', ')
    key = name[0]
    value = name[1]
    if key not in branchemap:
        branchemap[key] = []
    branchemap[key].append(value)
print(branchemap)

    #branchemap.update({index:name[1]})

