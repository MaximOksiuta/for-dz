# from re import findall
#
#
# def numbers_from_string(data):
#     result = findall(r'\d+', data)
#     return result
#
#
# with open('save.txt', 'r', encoding='utf-8') as f:
#
#     content = f.readlines()
#     ls = []
#     content = str(content)[2:-2]
#     work = numbers_from_string(content)
#     print(work)
#     # for i in range(0, len(work)):
#     print(content)
#     for i in content.split(f'{work[0]}'):
#         ls.append(i)
#     print('hey')
#     print(ls)
#     print(ls.pop())
#     for i in ls.pop().split(f'{work[1]}'):
#         ls.append(i)
#     print(ls)
#     # for i in range(0, len(content) - 1):
#     #     if content[i].isdigit:
#     #         ls.append(content[:i])
#     # for n in range(i, len(content) - 1):
#     #     if content[i].isdigit:
#     #         pass
#     #     else:
#     #         ls.append(content[i:n])
# print(ls)
with open('save.txt', 'r', encoding='utf-8') as f:
    content = f.readline()
    ls = content.split('/')
print(ls)
for n in range(0, len(ls)//5):
    for i in ls[5*n:5*n+5]:
        print(i)
    print('new')
        #ot.warehouses.append(Warehouse(ls[n*4+1+n], ls[n*4+2+n], ls[n*4+3+n], ls[n*4+4+n], ls[n*4+n]))

money = int(ls.pop())