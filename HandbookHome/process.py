def search (sn):
    res_list = []
    with open ('HandbookHome\data.txt', 'r', encoding='utf-8') as file:
        while True:
            my_book = file.readline()
            if not my_book:
                if not file.readline():
                    break
            if my_book.rstrip().lower() == sn.lower():
                res_list.append(my_book.rstrip())
                for _ in range(1, 5):
                    res_list.append(file.readline().rstrip())
                res_list.append('')
        if len(res_list) > 0:
            return res_list
        else:
            return 'Таких людей не найдено'


def export (res):
    path = 'HandbookHome\data.txt'
    with open (path, 'a', encoding='utf-8') as file:
        for ind in range(5):
            file.write(res[ind] + '\n')
        file.write(res[5])


# def delete_item (sn):
#     with open ('Handbook\data.txt', 'r', encoding='utf-8') as file:
#         while True:
#             my_book = file.readline()
#             if not my_book:
#                 if not file.readline():
#                     break   
            
#             num = file.readlines()             
#             ind = [x for x in range(len(num)) if 'Иванов' in num[x]]
#             print('index', ind)

#             for i, line in enumerate(file.readlines()):
#                 if line == 'Иванов':
#                     print('i=', i)

# # lines = [x for x in content if search_str in content]

#             if my_book.rstrip().lower() == sn[0].lower():
#                 print('фамилию нашла')

#                 # print(file.index(my_book))
#                 # print(type(my_book.index))
#                 # file.__getattribute__(my_book)
#                 # print('s=', int(s))
#                 # s = file[my_book]
#                 # print('s=', int(s))
#                 # linecache.getline(my_book, Nu)
#                 # s = file.seek(my_book)
#                 # print(s)
#                 if file.readline().rstrip().lower() == sn[1].lower():
#                     print('имя нашла')
#                     # print(file.readline().index())
#                 else:
#                     print('имя не нашла!')
#         else:
#             pass
#             # return 'Таких людей не найдено'