'''Задача:

Используя данные телеметрии, определить топ 10 самых популярных сценариев запуска алгоритмов
в рамках одной сессии.
Визуализировать полученные данные на дэшборде. Инструмент и тип графиков на усмотрение автора.

В ответе необходимо указать:

- Общее количество сессий.
- Количество выполнений каждого сценария из топ 10 списка.
- Последовательность запуска алгоритмов для каждого сценария из топ 10.

Структура данных

[ApplicationStarted] – Начало сессии
[ApplicationClosed] — Окончание сессии
[AlgorithmStarted] — Был запущен алгоритм
[AlgorithmCompletedTime] — Алгоритм завершен
Algorithm {id} — Название алгоритма'''

import os
import re

# функция create_list
# создаем тапл с названиями всех лог-файлов
path = r'C:\Users\33306\pythonProject\test_logs\logs'
all_logs = tuple(os.listdir(path))
# конец функции

# считываем все алгоритмы, получаем список существующих алгоритмов
all_algorithms = []
for i in all_logs:
    with open(f'{path}\\{i}', 'r') as file:
        for row in file:
            pattern = r'\[AlgorithmCompletedTime\]Algorithm\s+(\d+)\.'
            if 'AlgorithmCompletedTime' in row:
                all_algorithms.append(int(*re.findall(pattern, row)))
uniq_algorithms = set(all_algorithms)
# конец функции


# считаем кол-во сценариев
use_algorithms = {}
for i in uniq_algorithms:
    use_algorithms[i] = all_algorithms.count(i)
sorted_use_algorithms = sorted(use_algorithms.items(), key=lambda x: x[1], reverse=True)
use_algorithms = dict(sorted_use_algorithms)

top_algorithms = {}
count = 0
while count != 10:
    for i in use_algorithms:
        top_algorithms[i] = use_algorithms[i]
        count += 1
print(top_algorithms)

