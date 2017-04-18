import sys

def get_depth(id, depth_dict, parents):
    if id in depth_dict:
        return depth_dict[id]
    if parents[id] == -1:
        depth_dict[id] = 0
        return 0
    depth_dict[id] = 1 + get_depth(parents[id], depth_dict, parents)
    return depth_dict[id]

children = dict()
parents = dict()
depth_dict = dict()

n = int(input())

for i in range(n):
    parents[i] = -1

for i in range(n):
    input = sys.stdin.readline().split()
    id = int(input[0])
    children[id] = []
    for child in input[2:n+2]:
        children[id].append(int(child))
        parents[int(child)] = id

for i in range(n):
    if parents[i] == -1:
        node_type = "root"
    elif children[i] == []:
        node_type = "leaf"
    else:
        node_type = "internal node"

    depth = get_depth(i, depth_dict, parents)

    print("node {0}: parent = {1}, depth = {2}, {3}, {4}".format(i, parents[i], depth, node_type, children[i]))
