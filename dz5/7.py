from json import dump
with open("text_7.txt", 'r', encoding='utf-8') as f:
    content = f.readlines()
    dictionary = {}
    aver_profit = 0
    c = 0
    for i in content:
        ls = i.split()
        profit = int(ls[2])-int(ls[3])
        dictionary.update({ls[0]: profit})
        if profit >= 0:
            aver_profit += profit
            c += 1
    aver_profit = {'average_profit': aver_profit / c}
itog = [dictionary, aver_profit]
with open("text_77.json", 'w') as f:
    dump(itog, f)