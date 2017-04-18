import sys

def get_depth(id, depth_dict, parents):
    if parents[id] == -1:
        return 0
    if id in depth_dict:
        return depth_dict[id]
    depth_dict[id] = 1 + get_depth(parents[id], depth_dict, parents)
    depth_dict[sibling[id]] = depth_dict[id]
    return depth_dict[id]

def get_height(id, depth_dict, children):
    if id in height_dict:
        return height_dict[id]
    if len(children[id]) == 0:
        return 0
    if len(children[id]) == 1:
        height_dict[id] = 1 + get_height(children[id][0], height_dict, children)
        return height_dict[id]
    height_dict[id] = 1 + max(get_height(children[id][0], height_dict, children), get_height(children[id][1], height_dict, children))
    return height_dict[id]

parents = dict()
sibling = dict()
children = dict()
depth_dict = dict()
height_dict = dict()

n = int(input())

for i in range(n):
    input = sys.stdin.readline().split()
    id = int(input[0])
    left = int(input[1])
    right = int(input[2])
    children[i] = []
    if left != -1:
        children[i].append(left)
    if right != -1:
        children[i].append(right)
    parents[left] = id
    parents[right] = id
    sibling[left] = right
    sibling[right] = left

for id in range(n):
    node_type = "internal node"
    if not id in parents:
        node_type = "root"
        parents[id] = -1
    elif len(children[id]) == 0:
        node_type = "leaf"

    depth = get_depth(id, depth_dict, parents)
    height = get_height(id, depth_dict, children)

    if not id in sibling:
        sibling[id] = -1

    print('node {0}: parent = {1}, sibling = {2}, degree = {3}, depth = {4}, height = {5}, {6}'.format(id, parents[id], sibling[id], len(children[id]), depth, height, node_type))
