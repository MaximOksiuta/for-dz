ls = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = []
result = [ls[i] for i in range(1, len(ls)) if ls[i]>ls[i-1]]
print(result)