# -*- coding: utf-8 -*-

'''
 Название программы: Нахождение приближенных корней. Метод простых итераций.
 Автор: Пак Дмитрий, ИУ7-22Б

 Функционал: приближение корней функции на данном интервале методом простых
 итераций

 Используемые библиотеки: tkinter, matplotlib, numpy
'''


from tkinter import *
import math as m
from pylab import *
import matplotlib.pyplot as plt
import tkinter as tk
import numpy as np
from tkinter import messagebox

EPS = 1e-6
NO_ROOT = -1
MAX_ITER = -2
INTERVAL_WRONG = -3


# Заданная функция
def f(x):
    return sin(x)


# Приближение корней
def calculate():
    cleanList()
    cut = entryCut.get()
    step = entryStep.get()
    acc = entryAcc.get()
    it = entryIt.get()
    interval = proverkacut(cut)
    shag = proverkanum(step, 2)
    eps = proverkanum(acc, 3)

    iter = proverkanum(it, 4)

    if (iter == '0') or (shag == '0') or (eps == '0') or (interval == '0'):
        return

    currentLeft = interval[0]
    result = []
    cnt = 0

    right = interval[1]

    while currentLeft + eps < right:
        currentRight = min(currentLeft + shag, right)
        if currentRight + eps >= right:
            currentRight += 2 * eps

        cnt += 1

        result.append([cnt, [currentLeft, currentRight]]
                      + precise(currentLeft, currentRight, iter, eps))
        currentLeft += shag

    return result


# Возвращение ошибок
def precise(left, right, maxIter, eps):
    currentLeft = left
    currentRight = right - eps
    currentRoot = left
    cnt = 0

    if f(currentLeft) * f(currentRight) > 0:
        return [0, 0, 0, NO_ROOT]

    if abs(f(currentLeft)) < eps:
        return [currentLeft, f(currentLeft), 0, 0]

    if abs(f(currentRight)) < eps:
        return [currentRight, f(currentRight), 0, 0]

    while abs(f(currentRoot)) > EPS:
        if cnt >= maxIter:
            return [0, 0, 0, MAX_ITER]
        currentRoot = f(currentRoot) + currentRoot
        cnt += 1

    if currentRoot < left or currentRoot > right:
        return [0, 0, 0, INTERVAL_WRONG]

    return [currentRoot, f(currentRoot), cnt - 1, 0]


# Вывод результата в таблицу
def res():

    result = calculate()
    cnt = 0

    for line in result:
        if line[5] != NO_ROOT:
            cnt += 1
            listboxN.insert(END, '{:^4d}'.format(line[0]))
            listboxAb.insert(END,'{:^8.2f} : {:^8.2f}'.format(line[1][0],
                                                              line[1][1]))
            if line[5] == 0:
                listboxX.insert(END,'{:^3.5f}'.format(line[2]))
                listboxFx.insert(END,'{:^12.0e}'.format(line[3]))
                listboxIt.insert(END,'{:^5d}'.format(line[4]))
            else:
                listboxX.insert(END,'{:^8s}'.format('-' * 3))
                listboxFx.insert(END,'{:^12s}'.format('-' * 3))
                listboxIt.insert(END,'{:^5s}'.format('-' * 3))

            listboxIn.insert(END,'{:3d}'.format(line[5]))
            listboxN.insert(END, '-' * 23)
            listboxAb.insert(END, '-' * 30)
            listboxX.insert(END, '-' * 30)
            listboxFx.insert(END, '-' * 30)
            listboxIt.insert(END, '-' * 30)
            listboxIn.insert(END, '-' * 30)

    if cnt == 0:
        messagebox.showinfo('Ошибка', 'Корней на промежутке не найдено\n')
    scales.configure(to=listboxN.size())


# построение графика
def graphic():
    cut = entryCut.get()
    interval = proverkacut(cut)
    if interval == 0:
        return
    leftside = interval[0]
    rightside = interval[1]
    stepgraph = (rightside - leftside) / 200
    xpoints = np.arange(leftside, rightside, stepgraph)
    s = f(xpoints)
    ox = []
    oy = []
    for i in range(len(s) - 2):
        if (s[i] < s[i + 1] > s[i + 2]) or \
                (s[i] > s[i + 1] < s[i + 2]):
            ox.append(xpoints[i + 1])
            oy.append(s[i + 1])
    plt.scatter(ox, oy, s=40, c='purple', marker='o')
    lab1 = u"ext"
    lab2 = ''
    plt.legend((lab1,lab2), frameon=False)
    plt.xlabel(u'x')
    plt.ylabel(u'f(x)')
    plot(xpoints, s)
    title('f(x)')
    grid(True)
    show()


# очистка всех полей
def clean():
    listboxN.delete(0, END)
    listboxAb.delete(0, END)
    listboxX.delete(0, END)
    listboxFx.delete(0, END)
    listboxIt.delete(0, END)
    listboxIn.delete(0, END)
    entryIt.delete(0, END)
    entryStep.delete(0, END)
    entryAcc.delete(0, END)
    entryCut.delete(0, END)


# очистка листбоксов
def cleanList():
    listboxN.delete(0, END)
    listboxAb.delete(0, END)
    listboxX.delete(0, END)
    listboxFx.delete(0, END)
    listboxIt.delete(0, END)
    listboxIn.delete(0, END)


#очистка поля ввода границ интервала
def cleanentrycut():
    entryCut.delete(0, END)


#очистка поля ввода точности
def cleanentryacc():
    entryAcc.delete(0, END)


#очистка поля ввода шага
def cleanentrystep():
    entryStep.delete(0, END)


#очистка поля кол-ва итераций
def cleanentryit():
    entryIt.delete(0, END)


#проверка поля ввода границ интервала
def proverkacut(str):
    str.lstrip()
    str.rstrip()
    interval = str.split()

    if len(interval) != 2:
        error(1)
        return '0'

    if proverkanum(interval[0], 1) == '0':
        return '0'
    if proverkanum(interval[1], 1) == '0':
        return '0'
    interval[0] = float(interval[0])
    interval[1] = float(interval[1])
    if (interval[0] == 0) and (interval[1] == 0):
        return '0'
    return interval


# проверка других полей ввода
def proverkanum(victim, n):
    if n == 4:
        try:
            num = int(victim)
        except ValueError:
            error(n)
            return '0'
        return int(victim)
    else:
        try:
            num = float(victim)
        except ValueError:
            error(n)
            return '0'
    if float(victim) == '0':
        return '0'
    else:
        return float(victim)


# вывод ошибки ввода
def error(n):
    if n == 1:
        entryCut.delete(0, END)
        entryCut.insert(0, "Ошибка ввода")
        current.after(1000, cleanentrycut)
    elif n == 2:
        entryStep.delete(0, END)
        entryStep.insert(0, "Ошибка ввода")
        current.after(1000, cleanentrystep)
    elif n == 3:
        entryAcc.delete(0, END)
        entryAcc.insert(0, "Ошибка ввода")
        current.after(1000, cleanentryacc)
    elif n == 4:
        entryIt.delete(0, END)
        entryIt.insert(0, "Ошибка ввода")
        current.after(1000, cleanentryit)


# тестовая функция
def test():
    clean()
    entryCut.insert(0, "-10 10")
    entryStep.insert(0, "2")
    entryAcc.insert(0, "1e-5")
    entryIt.insert(0, "200")


# функция скроллинга
def scroll(x):
    listboxN.see(x)
    listboxX.see(x)
    listboxFx.see(x)
    listboxAb.see(x)
    listboxIt.see(x)
    listboxIn.see(x)


# основная функция, создание GUI
if __name__ == "__main__":
    current = Tk()
    current.geometry('1400x600')
    current.title('Нахождение приближенных корней. Метод простых итераций.')
    current.configure(background='white')
    current.resizable(False, False)

    labN = Label(text='N', font="Helvetica 18")
    labN.grid(column=1, row=1)
    listboxN = Listbox(current, width=10, height=20)
    listboxN.grid(column=1, row=2, rowspan=10)
    labAb = Label(text='[Xi;Xi+1]', font="Helvetica 18")
    labAb.grid(column=2, row=1)
    listboxAb = Listbox(current, width=20, height=20)
    listboxAb.grid(column=2, row=2)
    labX = Label(text='X', font="Helvetica 18")
    labX.grid(column=3, row=1)
    listboxX = Listbox(current, width=20, height=20)
    listboxX.grid(column=3, row=2)
    labFx = Label(text='F(X)', font="Helvetica 18")
    labFx.grid(column=4, row=1)
    listboxFx = Listbox(current, width=20, height=20)
    listboxFx.grid(column=4, row=2)
    labIt = Label(text='Итерации', font="Helvetica 18")
    labIt.grid(column=5, row=1)
    listboxIt = Listbox(current, width=20, height=20)
    listboxIt.grid(column=5, row=2)
    labIn = Label(text='Код ошибки', font="Helvetica 18")
    labIn.grid(column=6, row=1)
    listboxIn = Listbox(current, width=20, height=20)
    listboxIn.grid(column=6, row=2)

    labFunc = Label(text='Функция:\nsin(x)', font="Helvetica 18")
    labFunc.place(x=1050, y=5)
    labCut = Label(text='Границы интервала', font="Helvetica 18")
    labCut.place(x=1050, y=55)
    entryCut = Entry(current)
    entryCut.place(x=1050, y=85)
    labStep = Label(text='Шаг разбиения', font="Helvetica 18")
    labStep.place(x=1050, y=130)
    entryStep = Entry(current)
    entryStep.place(x=1050, y=165)
    labAcc = Label(text='Точность', font="Helvetica 18")
    labAcc.place(x=1050, y=210)
    entryAcc = Entry(current)
    entryAcc.place(x=1050, y=245)
    labIt = Label(text='Число итераций', font="Helvetica 18")
    labIt.place(x=1050, y=290)
    entryIt = Entry(current)
    entryIt.place(x=1050, y=335)

    btnClean = tk.Button(text='Очистить всё', command=clean)
    btnClean.place(x=1050, y=380)
    btnSolve = tk.Button(text='Уточнить', command=res)
    btnSolve.place(x=1050, y=420)
    btnGraph = tk.Button(text='Построить график', command=graphic)
    btnGraph.place(x=1050, y=460)
    btnGraph = tk.Button(text='Тест', command=test)
    btnGraph.place(x=1050, y=500)

    scales = Scale(current, from_=0, orient=HORIZONTAL, command=scroll,
                   length=180)
    scales.grid(column=3, row=15)

    labAcc = Label(text = "Code: \n \
0 - Программа работает правильно \n \
-1 - Недостаточно итераций \n \
-2 - Превышение количества корней \n \
-3 - Выход из интервала\n")
    labAcc.place(x=550, y=400)

    current.mainloop()
