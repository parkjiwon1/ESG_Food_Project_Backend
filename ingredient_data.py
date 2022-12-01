import csv
import re

p = re.compile(r"'(.*?)'")
igd_group = []
igd_dict = {}
result_arr = []

f2 = open('ingredients_list.txt', 'r', encoding='utf-8')
for line in f2.readlines():
    igd_group.append(p.findall(line))

categories = ['name', 'address']
for i, group in enumerate(igd_group):
    categories.append(group[0])
    for el in group:
        igd_dict[el] = i

f1 = open('2000recipe_ver2.csv', 'r', encoding='cp949')
reader = csv.reader(f1)
for line in reader:
    sub_group = [line[0], line[1]]
    check_list = ['0'] * (len(categories) - 2)
    for el in line[2:]:
        if el not in igd_dict.keys():
            continue
        check_list[igd_dict[el]] = '1'
    result_arr.append(sub_group + check_list)


# print(categories)
# for i in result_arr:
#     print(i)

# for i in igd_group:
#     print(i)

for line in result_arr:
    ans = [line[0], line[1]]
    for i, el in enumerate(line):
        if el == '1':
            ans.append(categories[i])
    print(ans)

# f3 = open('output.csv', 'w', encoding='cp949', newline='')
# writer = csv.writer(f3)
# writer.writerows([categories] + result_arr)

f1.close()
f2.close()
