# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны,
# по алгоритму поиска в глубину (Depth-First Search).

# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.

def dfs(graph, start,visited = None):
    if visited == None:
        visited = [False]*len(graph)
    visited[start] = True
    #print(visited)
    for next in graph[start]:
        if not visited[next]:
            dfs(graph, next, visited)
    return visited

# Результат функции выдается в виде списка булевых значений по каждой вершине

#Зададим граф в виде списка смежности для графа, указанного на видеоуроке
gr = [
    [1,3,4],
    [2,5],
    [1,6],
    [1,5,7],
    [2,6],
    [6],
    [5],
    [7]
]

gr2 = [
    [1,3],
    [2,5],
    [1,6],
    [1,5,7],
    [2,6],
    [6],
    [5],
    [7]
]

st_vertex = int(input('Введите стартовую вершину для проверки: '))
v1 = dfs(gr,st_vertex)
v2 = dfs(gr2,st_vertex)
print(f'При старте с вершины {st_vertex}\n графа {gr }\nпосещение вершин выглядит {dfs(gr,st_vertex)}')
print(f'При старте с вершины {st_vertex}\n графа {gr2 }\nпосещение вершин выглядит {dfs(gr2,st_vertex)}')

# или если перевести просто в номера вершин:
print("*"*100)
visited_vertexs1 = []
for i in range(len(gr)):
    if v1[i]:
        visited_vertexs1.append(i)
print(f'Для первого графа посещены вершины: {visited_vertexs1}')

visited_vertexs2 = []
for i in range(len(gr)):
    if v2[i]:
        visited_vertexs2.append(i)
print(f'Для второго графа посещены вершины: {visited_vertexs2}')