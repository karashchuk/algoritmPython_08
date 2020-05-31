# 1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу).
# Сколько рукопожатий было?

# Примечание. Решите задачу при помощи построения графа.

# Вариант 1.
# Зададим граф в виде матрицы смежности.
# Для случая когда есть N друзей, будет матрица N*N. Сам с собой не здороваются, и если k-ый друг поздоровался
# с m-ым другом, то m-ому другу не надо здороваться с k-ым
# Тогда матрицей смежности будет треуголня матрица с 1, и также диагонал = 0
import numpy as np
N = 15

Z = np.zeros((N,N), dtype=int)
for i in range(len(Z)-1):
    Z[i][i+1:] = 1
#print(Z)
# тогда количество ребер в графе будет равняться сумме элементов матрицы
print(f'Для N = {N} количество рукопожатий  = {sum(sum(Z))}  (Матрица смежности)')

# Вариант 2.
# Зададим граф в виде списка ребер.
edges = []
for p in range(N):
    for i in range(p):
        edges.append((p, i))
#Тогда количесство ребер это просто длина этого массива
print(f'Для N = {N} количество рукопожатий  = {len(edges)}  (Список ребер)')
#print(edges)
