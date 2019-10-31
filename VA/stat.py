import csv, maths
data = []
with open('VA/data.csv') as fin:
    f_csv = csv.reader(fin)
    headers = next(f_csv)
    for i in f_csv:
        data.append(list(i))

DFS_time = [float(i[2]) for i in data]
BFS_time = [float(i[3]) for i in data]
Eli_time = [float(i[4]) for i in data]
DFS_weight = [float(i[5]) for i in data]
BFS_weight = [float(i[6]) for i in data]

DFS_mean = maths.mean([(i, 1) for i in DFS_time])
DFS_sd = maths.sd([(i, 1) for i in DFS_time])

BFS_mean = maths.mean([(i, 1) for i in BFS_time])
BFS_sd = maths.sd([(i, 1) for i in BFS_time])

Eli_mean = maths.mean([(i, 1) for i in Eli_time])
Eli_sd = maths.sd([(i, 1) for i in Eli_time])

DFS_weight_mean = maths.mean([(i, 1) for i in DFS_weight])
DFS_weight_sd = maths.sd([(i, 1) for i in DFS_weight])

BFS_weight_mean = maths.mean([(i, 1) for i in BFS_weight])
BFS_weight_sd = maths.sd([(i, 1) for i in BFS_weight])

print('                     DFS               BFS                Elimination      DFS-weighted       BFS-weighted')
print('              mean: ', DFS_mean, BFS_mean, Eli_mean, DFS_weight_mean, BFS_weight_mean)
print('standard deviation: ', DFS_sd, BFS_sd, Eli_sd, DFS_weight_sd, BFS_weight_sd)
