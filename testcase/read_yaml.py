import yaml
with open('case.yaml', encoding='utf-8') as f:
     datas = yaml.safe_load(f)

print(datas)
# data1 = datas['homepage'][0]
# data2 = data1['cases']
# print(data2)
# data3 = data2[0]
# data4 = data3['name']
# print(data4)
