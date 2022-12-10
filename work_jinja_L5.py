# при создании сайтов страницу делят, как минимум на три части:
# заголовок, контент, футер
# Это связано с тем, что у всех страниц шапка (заголовок) сайта,
# как правило, одинакова и потому ее нужно просто подключить к нужному шаблону.

# это можно реализовать с помощью специального блока
# {% include <путь к файлу шаблона> %}

from jinja2 import Environment, FileSystemLoader

file_loader = FileSystemLoader('')
env = Environment(loader=file_loader)

tm = env.get_template('work_jinja_L5_page.html')
msg = tm.render()

print(msg)

print('------------------------------')

# если указан неверный файл (например, заголовка), то можно, не обрабатывая исключений,
# игнорировать то, что файла не существует:
# {% include 'header.html' ignore missing %}

# вызывая шаблон 'work_jinja_L5_header2.html' передавать ему домен и заголовок для каждой страницы

file_loader2 = FileSystemLoader('')
env2 = Environment(loader=file_loader2)

tm2 = env2.get_template('work_jinja_L5_page2.html')
msg2 = tm2.render(domain='http://proproprogs.ru', title="Про Jinja")

print(msg2)

print('------------------------------')

# import
# Если в блоке include требуется подключить сразу несколько файлов, то их следует указать в виде списка:
# {% include ['page1.htm', 'page2.htm'] ignore missing %}

file_loader3 = FileSystemLoader('')
env3 = Environment(loader=file_loader2)

tm3 = env3.get_template('work_jinja_L5_page3.html')
msg3 = tm3.render(domain='http://proproprogs.ru', title="Про Jinja")

print(msg3)

print('------------------------------')

# Смотрите, благодаря импорту мы можем обратиться к макросу dialog_1 и создать вид диалогового окна. Причем,
# во избежание конфликтов имен, в конце после ключевого слова as можно прописать алиас, через который будет
# происходить обращение к элементам шаблона dialogs.htm.
#
# Или же, воспользоваться такой конструкцией:

# {% include 'header.htm' ignore missing  %}
# {% from 'dialogs.htm' import dialog_1 as dlg %}
# Содержимое страницы
# {{ dlg('Внимание', 'Это тестовый диалог') }}
# {% include 'footer.htm' %}
# Тогда обращение к макросу будет происходить по имени dlg.