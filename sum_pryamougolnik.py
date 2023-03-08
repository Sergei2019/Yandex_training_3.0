"""
Вам необходимо ответить на запросы узнать сумму всех элементов числовой матрицы N×M в прямоугольнике с левым верхним углом (x1, y1) и правым нижним (x2, y2)

Формат ввода
В первой строке находится числа N, M размеры матрицы (1 ≤ N, M ≤ 1000) и K — количество запросов (1 ≤ K ≤ 100000). 
Каждая из следующих N строк содержит по M чисел`— элементы соответствующей строки матрицы (по модулю не превосходят 1000).
Последующие K строк содержат по 4 целых числа, разделенных пробелом x1 y1 x2 y2 — запрос на сумму элементов матрице в прямоугольнике (1 ≤ x1 ≤ x2 ≤ N, 1 ≤ y1 ≤ y2 ≤ M)

Формат вывода
Для каждого запроса на отдельной строке выведите его результат — сумму всех чисел в элементов матрице в прямоугольнике (x1, y1), (x2, y2)



Ввод	
3 3 2
1 2 3
4 5 6
7 8 9
2 2 3 3
1 1 2 3

Вывод
28
21

"""
N, M, k = list(map(int, input().split(' ')))
z, mat = [], []
aux = [[0 for x in range(M)] for y in range(N)] 
for i in range(N):
    mat.append(list(map(int, input().strip().split(' '))))

for i in range(M):
    aux[0][i] = mat[0][i]
for i in range(1, N):
    for j in range(0, M, 1):
        aux[i][j] = mat[i][j] + aux[i - 1][j]
    
for i in range(N):
    for j in range(1, M, 1):
        aux[i][j] += aux[i][j - 1]

for i in range(k):
    m = list(map(int, input().strip().split(' ')))
    tli, tlj, rbi, rbj = m[0]-1, m[1]-1, m[2]-1, m[3]-1
    
    res = aux[rbi][rbj]
    
    if (tli > 0):
        res = res - aux[tli - 1][rbj]
    if (tlj > 0):
        res = res - aux[rbi][tlj - 1]
    if (tli > 0 and tlj > 0):
    	res = res + aux[tli - 1][tlj - 1]
    z.append(res)


for el in z:
    print(el)