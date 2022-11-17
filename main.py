import json
import datetime
from tabulate import tabulate

result_run = []


def time(start, finish):
    t = datetime.datetime.strptime(finish[2], '%H:%M:%S,%f') - datetime.datetime.strptime(start[2], '%H:%M:%S,%f')
    result_run.append((start[0], str((t))))

with open('results_RUN.txt', 'r', encoding='UTF-8-sig') as res, \
        open('competitors2.json', 'r', encoding='UTF-8') as comp:
    r = [i.strip().split() for i in res]
    c = json.load(comp)

for i in range(0, len(r), 2):
    time(r[i], r[i + 1])

result_run = sorted(result_run, key=lambda x: x[1])
head = ('Занятое место', 'Нагрудный номер', 'Имя', 'Фамилия', 'Результат')
result = []

for i in range(len(result_run)):
    result.append([i + 1, result_run[i][0], c[str(result_run[i][0])]["Surname"], c[str(result_run[i][0])]["Name"], result_run[i][1][2:-4]])
print(tabulate(result, headers=head, tablefmt="grid"))
