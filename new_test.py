File_data = open("forest.txt", "r", encoding='utf-8')
txt = File_data.read()

#tree
tree=txt.split('nodes:')[0]
treelist = list(tree.split('\n'))

#node
nodes= (txt.split('nodes:')[1]).split('branches:')[0]
nodeslist = list(nodes.split('\n'))
nodeslist.remove('')
nodeslist.remove('')
new_node = list(map(lambda name: name.split(', ')[1], nodeslist))

#branche
branchemap = {}
branches=txt.split('branches:')[1]
brancheslist = list(branches.split('\n'))
brancheslist.remove('')
def init(name):
    #print(name)
    if int(name[0]) not in branchemap:
        branchemap[int(name[0])] = []
    branchemap[int(name[0])].append(name[1])
    return name
bran = list(map(lambda name: init(name.split(', ')),brancheslist))
print(branchemap)
'''
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
#print(nodemap)

branchemap = {}
branches=txt.split('branches:')[1]
brancheslist = list(branches.split('\n'))
brancheslist.remove('')
for char in brancheslist:
    name = char.split(', ')
    key = name[0]
    value = name[1]
    if int(key) not in branchemap:
        branchemap[int(key)] = []
    branchemap[int(key)].append(value)

#print(branchemap.get(2))
print(branchemap)
'''