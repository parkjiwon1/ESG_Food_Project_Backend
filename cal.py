import csv


def cal_similarity(img_ingredients):
    length = 33
    f = open('output.csv', 'r', encoding='cp949')
    read = list(csv.reader(f))

    for idx, line in enumerate(read[1:]):
        score = 0
        for i in range(2, length + 2):
            score += int(img_ingredients[i - 2]) & int(line[i])
        line.append(idx)
        if sum(map(int, line[2:-1])) != 0:
            score_ = score / sum(map(int, line[2:-1]))
        else:
            score_ = 0
        line.append(score_)

    sorted_list = sorted(read[1:], key=lambda x: x[-1], reverse=True)
    output_list = []
    indices = []
    for el in sorted_list:
        output_list.append(el[:2] + [el[-1]])
        indices.append(el[-2])

    detected_ingredients = []
    for i in range(length):
        if int(img_ingredients[i]) == 1:
            detected_ingredients.append(read[0][i + 2])

    return [indices[:5], detected_ingredients]

#
# if __name__ == '__main__':
#     idx_ingredients = cal_similarity([1] + [0] * 32)
#     print(idx_ingredients)
