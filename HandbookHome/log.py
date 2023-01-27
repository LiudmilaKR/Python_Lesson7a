import datetime

def log_cash(rezh, result):
    with open('HandbookHome\log.txt', 'a', encoding='utf-8') as file:
        if rezh == 1:
            file.write(f'Поиск по фамилии <<{result}>> в справочнике. Время запроса: {str(datetime.datetime.now())} \n')
        elif rezh == 2:
            file.write(f'<<{result}>> внесен в справочник. Время запроса: {str(datetime.datetime.now())} \n')