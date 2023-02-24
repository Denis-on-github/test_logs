import os
import re

# функция create_list
# создаем тапл с названиями всех лог-файлов (сессий), считаем общее кол-во сессий
path = r'C:\Users\33306\pythonProject\test_logs\logs' # указываем путь к папке с файлами логов
all_logs = tuple(os.listdir(path)) # список сессий
session_count = len(all_logs) # общее кол-во сессий
# конец функции

# считываем все алгоритмы, получаем список существующих алгоритмов
all_algorithms = [] # создадим список всех алгоритмов
for i in all_logs:
    with open(f'{path}\\{i}', 'r') as file:
        for row in file:
            pattern = r'\[AlgorithmCompletedTime\]Algorithm\s+(\d+)\.' # используем регулярные выражения для поиска id алгоритма
            if 'AlgorithmCompletedTime' in row: # по завершению алгоритма понимаем, что он был выполнен
                all_algorithms.append(int(*re.findall(pattern, row))) # добавляем найденный id алгоритма в список
uniq_algorithms = set(all_algorithms) # список уникальных алгоритмов
# конец функции

# считаем кол-во запусков алгоритмов
use_algorithms = {} # создаем словарь key=алгоритм, value=кол-во запусков
for i in uniq_algorithms:
    use_algorithms[i] = all_algorithms.count(i)
sorted_use_algorithms = sorted(use_algorithms.items(), key=lambda x: x[1], reverse=True) # сортируем по значениям от большего к меньшему
use_algorithms = dict(sorted_use_algorithms) # создаем отсортированный словарь
# конец функции

# функция находит топ-10 алгоритмов
top_algorithms = {} # создадим словарь с топ-10 алгоритмов
flag = True
while flag is True:
    for i in use_algorithms:
        top_algorithms[i] = use_algorithms[i]
        if len(top_algorithms) == 10:
            flag = False
            break
# конец функции

#создаем круговую диаграмму
import plotly.graph_objs as go
import pandas as pd

table = pd.Series(top_algorithms) # представляем словарь в виде таблицы

fig = go.Figure()
fig.add_trace(go.Pie(values=table, labels=table.index, sort=False, hole=0.5))
fig.show()
# конец функции