from collections import defaultdict
from collections import OrderedDict
from operator import itemgetter
#for c, v2 in g.get(v1, ()):
g = defaultdict(list)
nodelist = []
visited = []
class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

def goNode(genode):
    print "genode.data ---> ", genode.data
    visited.append(genode.data)
    for child in g.get(genode.data,[]):
        print child
    for child in g.get(genode.data,[]):
        if child not in visited:
            print "sucessful child addn -->", child
            Nodechild = Node(child)
            genode.add_child(Nodechild)
    print "out of for"
    for childa in genode.children:
        print "genode.children data --> " , childa.data
        goNode(childa)

    #for child in g.get(genode.data):


def main():
    N, E = map(int, raw_input().strip(" ").split())
    for i in xrange(E):
        nodelist.append(map(int, raw_input().strip().split()))
    print nodelist
    for a, b in nodelist:
        g[a].append(b)
        g[b].append(a)
    print g.items()
    #for child in g.get(1,[]):
     #   print child
    root = Node(1)
    goNode(root)
    testNode = Node(8)
    print "FL"
    for c in testNode.children:
        print "C data"
        print c.data



if __name__ == '__main__':
    main()
