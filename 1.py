import os
import re
import plotly.graph_objs as go
import pandas as pd


class LogAnalyzer:

    # во все функции передаем аргумент path - наш путь к папке с файлами логов
    def get_all_logs(self, path): # получаем тапл с названиями всех файлов логов
        return tuple(os.listdir(path))

    def get_all_session(self, path): # получаем общее кол-во сессий
        all_logs = self.get_all_logs(path)
        session_count = len(all_logs)
        return session_count

    def get_all_algorithms(self, path): # получаем список всех алгоритмов
        all_logs = self.get_all_logs(path)
        all_algorithms = []
        for i in all_logs:
            with open(f'{path}/{i}', 'r') as file:
                for row in file:
                    pattern = r'\[AlgorithmCompletedTime\]Algorithm\s+(\d+)\.' # используем регулярное выражение для поиска id алгоритма
                    if 'AlgorithmCompletedTime' in row:
                        all_algorithms.append(int(*re.findall(pattern, row)))
        return all_algorithms

    def get_uniq_algorithms(self, path): # получаем список уникальных алгоритмов
        all_algorithms = self.get_all_algorithms(path)
        uniq_algorithms = set(all_algorithms)
        return uniq_algorithms

    def get_count_algorithm_usage(self, path): # получаем словарь где key=id алгоритма, value=кол-во запусков
        all_algorithms = self.get_all_algorithms(path)
        pre_use_algorithms = {} # промежуточный словарь, без сортировки
        for i in self.get_uniq_algorithms(path):
            pre_use_algorithms[i] = all_algorithms.count(i)
        sorted_use_algorithms = sorted(pre_use_algorithms.items(), key=lambda x: x[1], reverse=True) # сортируем словарь по значениям от большего к меньшему
        use_algorithms = dict(sorted_use_algorithms) # преобразуем в словарь
        return use_algorithms

    def get_top_algorithms(self, path): # получаем топ-10 алгоритмов
        use_algorithms = self.get_count_algorithm_usage(path)
        top_algorithms = {}
        flag = True
        while flag is True: # получаем 10 первых значений из сортированного списка
            for i in use_algorithms:
                top_algorithms[i] = use_algorithms[i]
                if len(top_algorithms) == 10:
                    flag = False
                    break
        return top_algorithms

    def get_pie_chart(self, path): # получаем диаграмму использованных алгоритмов
        top_algorithms = self.get_top_algorithms(path)
        table = pd.Series(top_algorithms)
        fig = go.Figure()
        fig.add_trace(go.Pie(values=table, labels=table.index, sort=False, hole=0.5))
        fig.show()

# тестим
if __name__ == '__main__':
    my_logs = LogAnalyzer()
    path = 'C:\\Users\\33306\\pythonProject\\test_logs\\logs'
    print(my_logs.get_all_logs(path))
    print(my_logs.get_all_algorithms(path))
    print(my_logs.get_uniq_algorithms(path))
    print(my_logs.get_all_session(path))
    print(my_logs.get_top_algorithms(path))
    my_logs.get_pie_chart(path)