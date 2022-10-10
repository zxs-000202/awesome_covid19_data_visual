import os
import csv
path = input('请输入文件路径(如果在根目录下可以直接输入文件名):')
while not os.path.exists(path):
    print('路径错误')
    path = input('请输入文件路径(如果在根目录下可以直接输入文件名):')
with open(path) as f:
    data = list(csv.reader(f))[1:]
ranks = {}
for each in data:
    date = each[0]
    if date in ranks:
        ranks[date].append({'name':each[1],'value':[int(each[2]), float(each[4]),each[1]]})
    else:
        ranks[date] = [{'name':each[1],'value':[int(each[2]), float(each[4]),each[1]]}]
data = ranks

res = []
for key in data:
    dic = {}
    date = key
    sdata = data[key]
    dic["time"] = date
    dic["data"] = sdata
    res.append(dic)
print(res)



