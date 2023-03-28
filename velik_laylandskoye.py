"""
Лайнландия представляет из себя одномерный мир, являющийся прямой, на котором располагаются N городов, последовательно пронумерованных от 0 до N - 1 . Направление в сторону от первого города к нулевому названо западным, а в обратную — восточным.
Когда в Лайнландии неожиданно начался кризис, все были жители мира стали испытывать глубокое смятение.
По всей Лайнландии стали ходить слухи, что на востоке живётся лучше, чем на западе.
Так и началось Великое Лайнландское переселение.
Обитатели мира целыми городами отправились на восток, покинув родные улицы,
и двигались до тех пор, пока не приходили в город, в котором средняя цена проживания была меньше, чем в родном.

10
1 2 3 2 1 4 2 5 3 1
-1 4 3 4 -1 6 9 8 9 -1

"""

n = int(input())
a = list(map(int, input().split()))
 
ans = [-1] * n
b = [0]
 
for i in range(1,n):   
    while len(b)>0 and a[i] < a[b[-1]]:
        ans[b.pop()] = i
    b.append(i)

str1 = ' '.join(str(x) for x in ans)
print(str1)