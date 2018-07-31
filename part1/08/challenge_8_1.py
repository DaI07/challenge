import statistics
import random

list = []

for i in range(0, 15):
    list.append(random.randint(0, 20))

print(list)
print("平均値は{}です。".format(statistics.mean(list)))
print("中央値は{}です。".format(statistics.median(list)))
try:
    print("最頻値は{}です。".format(statistics.mode(list)))
except statistics.StatisticsError:
    print("最頻値が複数存在しています。")
