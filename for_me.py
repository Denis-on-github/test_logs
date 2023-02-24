import os
import re

class Algorithms:
    def create_log_list(self, path: str): # передаем в функцию путь к папке с файлами логов
        all_logs = list(os.listdir(path)) # список сессий
        return all_logs

    def all_session(self, all_logs):

        session_count = len(create_log_list) # общее кол-во сессий
        return session_count

    def create_algo_list(self, all_logs): # считываем все алгоритмы, получаем список существующих алгоритмов
        global path
        all_algorithms = [] # создадим список всех алгоритмов
        for i in all_logs:
            with open(f'{path}\\{i}', 'r') as file:
                for row in file:
                    pattern = r'\[AlgorithmCompletedTime\]Algorithm\s+(\d+)\.' # используем регулярные выражения для поиска id алгоритма
                    if 'AlgorithmCompletedTime' in row: # по завершению алгоритма понимаем, что он был выполнен
                        all_algorithms.append(int(*re.findall(pattern, row))) # добавляем найденный id алгоритма в список
        return all_algorithms

    def uniq_algos(self, create_algo_list):
        uniq_algorithms = set(all_algorithms) # список уникальных алгоритмов
        return uniq_algorithms

    def algos_use(self):
        global uniq_algorithms, all_algorithms # считаем кол-во запусков алгоритмов
        use_algorithms = {} # создаем словарь key=алгоритм, value=кол-во запусков
        for i in uniq_algorithms:
            use_algorithms[i] = all_algorithms.count(i)
        sorted_use_algorithms = sorted(use_algorithms.items(), key=lambda x: x[1], reverse=True) # сортируем по значениям от большего к меньшему
        use_algorithms = dict(sorted_use_algorithms) # создаем отсортированный словарь
        return use_algorithms

    def top_algos(self, algos_use): # функция находит топ-10 алгоритмов
        global use_algorithms
        top_algorithms = {} # создадим словарь с топ-10 алгоритмов
        flag = True
        while flag is True:
            for i in use_algorithms:
                top_algorithms[i] = use_algorithms[i]
                if len(top_algorithms) == 10:
                    flag = False
                    break
        return top_algorithms

#создаем круговую диаграмму
import plotly.graph_objs as go
import pandas as pd

table = pd.Series(top_algorithms) # представляем словарь в виде таблицы

fig = go.Figure()
fig.add_trace(go.Pie(values=table, labels=table.index, sort=False, hole=0.5))
fig.show()
# конец функции