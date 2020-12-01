from collections import defaultdict
from sys import setrecursionlimit

def dfs_fix(node, parent, parents, graph):
    parents[node] = parent
    for key in graph[node].keys():
        if key != parent:
            dfs_fix(key, node, parents, graph)

def change_weight(way_number, new_weight):
    a, b = ways[way_number]
    graph[a][b] = new_weight
    graph[b][a] = new_weight

def find_result(node):
    biciaki = set()
    parent = parents[node]
    while parent != 0:
        new_biciak = graph[parent][node]
        biciaki.add(new_biciak)
        node, parent = parent, parents[parent]
    return len(biciaki)

def do_graph(i):
    ways = [0]
    graph = defaultdict(defaultdict)
    for _ in range(i):
        a, b, c = map(int, input().split())
        ways.append((a, b))
        graph[a][b] = c
        graph[b][a] = c

    parents = [0 for _ in range(n + 1)]
    for key in graph[1].keys():
        dfs_fix(key, 1, parents, graph)

    return graph, ways, parents

if __name__ == "__main__":
    setrecursionlimit(10000000)
    n, m, z = map(int, input().split())
    graph, ways, parents = do_graph(n-1)

    for _ in range(z):
        data = input().split()
        if data[0] == 'Z':
            print(find_result(int(data[1])))
        else:
            change_weight(int(data[1]), int(data[2]))
