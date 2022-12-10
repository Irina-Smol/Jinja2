from jinja2 import Template
from markupsafe import escape

data = '''Модуль Jinja вместо
определения {{ name }}
подставляет соответствующее значение'''

tm = Template(data)
msg = tm.render(name='Федор')

print(msg)

print('------------------------------')

# Блок {% raw %}  {% endraw %} все, что внутри этого блока преобразовано не будет

data = '''{% raw %} Модуль Jinja вместо
определения {{ name }}
подставляет соответствующее значение {% endraw %}'''

tm1 = Template(data)
msg1 = tm1.render(name='Федор')

print(msg1)

print('------------------------------')
# Экранирование символов

link = '''В HTML-документе ссылки определяются так: 
<a href="#">Ссылка</a>'''

tm2 = Template("{{ link }}")
msg2 = tm2.render(link=link)   # будет выходить в HTML-документе в виде ссылки

print(msg2)

print('------------------------------')

# надо сделать так, чтобы надпись выходила точно также, без тега "ссылка" в HTML-документе
# надо использовать экранирование

tm3 = Template("{{ link | e }}")
msg3 = tm3.render(link=link)   # чтобы увидеть именно определение тега <a> вместо самой ссылки, используется
                               # флаг e – escape (экранирование)
print(msg3)

print('------------------------------')

# в модуле markupsafe существует специальный класс escape, который на выходе выдает строку с экранированными символами
# импортируем escape

print(escape(link))

print('------------------------------')

# Выражение for

# {% for <выражение> %}
#     <повторяемый фрагмент>
# {% endfor %}

# позволяет формировать список на основе любого итерируемого объекта, например, упорядоченного списка

cities = [{'id': 1, 'city': 'Москва'},
          {'id': 5, 'city': 'Тверь'},
          {'id': 7, 'city': 'Минск'},
          {'id': 8, 'city': 'Смоленск'},
          {'id': 11, 'city': 'Калуга'}]

link = '''<select name="cities">
{% for c in cities %}
    <option value="{{c['id']}}">{{c['city']}}</option>
{% endfor %}
</select>'''

tm5 = Template(link)
msg5 = tm5.render(cities=cities)

print(msg5)

print('------------------------------')

# чтобы все строки шли друг за другом, ставится - перед знаком процента в конце
link = '''<select name="cities">
{% for c in cities -%}
    <option value="{{c['id']}}">{{c['city']}}</option>
{% endfor -%}
</select>'''

tm6 = Template(link)
msg6 = tm6.render(cities=cities)

print(msg6)

# Выражение if

# вывести те данные, где id > 6
link = '''<select name="cities">
{% for c in cities -%}
{% if c.id > 6 -%}
    <option value="{{c['id']}}">{{c['city']}}</option>
{% endif -%}
{% endfor -%}
</select>'''

tm7 = Template(link)
msg7 = tm7.render(cities=cities)

print(msg7)
print('------------------------------')

# записать данные, которые не подошли под условие в формате названия города
link = '''<select name="cities">
{% for c in cities -%}
{% if c.id > 6 -%}
    <option value="{{c['id']}}">{{c['city']}}</option>
{%else -%}
    {{c['city']}}
{% endif -%}
{% endfor -%}
</select>'''

tm8 = Template(link)
msg8 = tm8.render(cities=cities)

print(msg8)

print('------------------------------')

# добавление elif

link = '''<select name="cities">
{% for c in cities -%}
{% if c.id > 6 -%}
    <option value="{{c['id']}}">{{c['city']}}</option>
{%elif c.city == "Москва" -%}
    <option>{{c['city']}}</option>
{%else -%}
    {{c['city']}}
{% endif -%}
{% endfor -%}
</select>'''

tm9 = Template(link)
msg9 = tm9.render(cities=cities)

print(msg9)