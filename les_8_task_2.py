
# 2. Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин,
# которые необходимо обойти.

from collections import deque


def dijkstra(graph, start):
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length
    cost[start] = 0
    min_cost = 0
    st = start
    while min_cost < float('inf'):
        is_visited[start] = True

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:
                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start
        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i
    print(f'parent {parent}')
    ws = [deque() for _ in range(length)]
    for i in range(length):
        if cost[i] == 0:
            ws[i].appendleft(st)
        elif cost[i] < float('inf'):
            ws[i].append(i)
            k = i
            while parent[k] != st:
                ws[i].appendleft(parent[k])
                k = parent[k]
            ws[i].appendleft(st)
        else:
            ws[i].appendleft(None)
    return (ws, cost)

g = [
    [0,0,1,1,9,0,0,0],
    [0,0,9,4,0,0,7,0],
    [0,9,0,0,3,0,6,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,0],
    [0,0,0,0,0,0,5,0],
    [0,0,7,0,8,1,0,0],
    [0,0,0,0,0,1,2,0]
]
st = int(input('Введите стартовую точку: '))
ways, costs = dijkstra(g,st)
for i in range(len(g)):
    print(f'Vertex: {i}, cost: {costs[i]},  \t way: {list(ways[i])}' )