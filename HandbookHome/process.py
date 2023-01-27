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

    with open ('HandbookHome\data.csv', 'a', encoding='utf-8') as file:
        for ind in range(5):
            file.write(res[ind] + '\n')
        file.write(res[5])
