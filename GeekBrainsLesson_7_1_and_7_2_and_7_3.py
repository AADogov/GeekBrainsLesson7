# 1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
#
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp


# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); как лучше хранить
# конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект; можно ли будет
# при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?

# ----------Решение-------------


import os
import shutil


# обьявляем функцию которвая будет создавать директроию и файлы в ней на вход функция принимает кортеж из 2 значений
# название название исходной папки и список дочернинх папок и файлов
def new_dirs_and_files(path):
    if not os.path.isdir(path[0]):
        # проверяем если исходной папки нет, то создаем
        os.makedirs(path[0])
    for directory_or_file in path[1]:
        # для каждой дириктроии или файла  провереяем существование пути если не сушествует то,
        if not os.path.isdir(path[0] + "\\" + directory_or_file):
            # проверяем наличии точки в названии если есть то это файл если нет то папка
            if '.' in directory_or_file:
                fp = open(path[0] + "\\" + directory_or_file, 'w')
                fp.close()
            else:
                os.makedirs(path[0] + "\\" + directory_or_file)


structure_my_project = ('my_project',
                        ['settings', 'mainapp', 'adminapp', 'authapp'])

new_dirs_and_files(structure_my_project)

# 2. * (вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:

# ----------Решение-------------
structure_settings = ('my_project\\settings', ['__init__.py', 'dev.py', 'prod.py'])
structure_mainapp = ('my_project\\mainapp', ['__init__.py', 'models.py', 'views.py', 'templates'])
structure_mainapp_templates = ('my_project\\mainapp\\templates', ['mainapp'])
structure_mainapp_templates_mainapp = ('my_project\\mainapp\\templates\\mainapp', ['base.html', 'index.html'])
structure_authapp = ('my_project\\authapp', ['__init__.py', 'models.py', 'views.py', 'templates'])
structure_authapp_templates = ('my_project\\authapp\\templates', ['authapp'])
structure_authapp_templates_authapp = ('my_project\\authapp\\templates\\authapp', ['base.html', 'index.html'])

new_dirs_and_files(structure_settings)
new_dirs_and_files(structure_mainapp)
new_dirs_and_files(structure_mainapp_templates)
new_dirs_and_files(structure_mainapp_templates_mainapp)
new_dirs_and_files(structure_authapp)
new_dirs_and_files(structure_authapp_templates)
new_dirs_and_files(structure_authapp_templates_authapp)

# 3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates, например:

# |--my_project
#    ...
#   |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html

# ----------Решение-------------

# Определяем путь к шаблону проекта
path = os.getcwd() + "\\my_project"

# определяем список всех папок в шаблоне проекта
for dir in os.listdir(path=path):
    # для каждой папки в шаблоне проекта создаем так называемый источник, просто обавляя к названию папки \\templates'
    source_path = path + '\\' + dir + '\\templates'
    # если он существует
    if os.path.exists(source_path):
        # перемешаем его в папку path + '\\templates'
        shutil.move(source_path, path + '\\templates')
