# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""

def _read(csv):
    # Чтение данных из строки
    return [i.split(";") for i in csv.split("\n")]

    # Сортировка по возрасту по возрастанию

def _sort(data):
    return [{"name": i[0], "age": int(i[1])} for i in sorted(data, key=lambda x: int(x[1]))]

    # Фильтрация
def _filter(f):
    return [i for i in f if i["age"] > 10]


if __name__ == '__main__':
    print(_filter(_sort(_read(csv))))
