import os


# обявляем функцию для определения размера файла или папки
def get_size(start_path='.'):
    total_size = 0
    # обьявляем переменную total_size и правниваем ее к 0
    if '.' in start_path:
        # если путь содержит точку то это файл возврашаем размер этого файла
        return os.path.getsize(start_path)
    else:
        # в противном случае это папка определяем размер папки вкулючая подпапки
        for dirpath, dirnames, filenames in os.walk(start_path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                if not os.path.islink(fp):
                    total_size += os.path.getsize(fp)

    return total_size


# создаем словарь  statistic и обявляем све его значения как 0
statistic = {
    0: 0,
    10: 0,
    100: 0,
    1000: 0,
    10000: 0,
    100000: 0
}
# определяем путь к интересующей нас папке
path = os.getcwd() + "\\my_project"
# path="D:\\"  # для  диска D у меня такая статистика {0: 2, 10: 1, 100: 2, 1000: 1, 10000: 1, 100000: 8}
# в зависимости от размера значения функции get_size для кажой папки или файла заполняем словарь
for dir_or_file in os.listdir(path=path):
    size = get_size(path + '\\' + dir_or_file)
    if 0 <= size < 10:
        statistic[0] += 1
    elif 10 <= size < 100:
        statistic[10] += 1
    elif 100 <= size < 1000:
        statistic[100] += 1
    elif 1000 <= size < 10000:
        statistic[1000] += 1
    elif 10000 <= size < 100000:
        statistic[10000] += 1
    else:
        statistic[100000] += 1
# выводим результат
print(statistic)
