import sys

class Data_tree:
    def __init__(self, name):
        self.name = name;
    def coordinate(self,x,y):
        self.x = x;
        self.y = y;
    def addList(self, child):
        self.child.append(child);
