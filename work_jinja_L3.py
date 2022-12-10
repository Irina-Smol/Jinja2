from jinja2 import Template
# sum для вычисления суммы определенной коллекции
# sum(iterable, attribute=None, start=0)

cars = [
    {'model': 'Ауди', 'price': 23000},
    {'model': 'Шкода', 'price': 17300},
    {'model': 'Вольво', 'price': 44300},
    {'model': 'Фольксваген', 'price': 21300}
]

tpl = "Суммарная цена автомобилей {{ cs | sum(attribute='price') }}"  # использование фильтра
tm = Template(tpl)
msg = tm.render(cs=cars)
print(msg)

print('------------------------------')

# макс. стоимость
tpl2 = "Автомобиль: {{ cs | max(attribute='price')  }}"
tm2 = Template(tpl2)
msg2 = tm2.render(cs=cars)
print(msg2)

print('------------------------------')

# выбор отдельного поля
tpl3 = "Автомобиль: {{ (cs | max(attribute='price')).model  }}"
tm3 = Template(tpl3)
msg3 = tm3.render(cs=cars)
print(msg3)

print('------------------------------')

# Выбор случайного значения из последовательности
tpl4 = "Автомобиль: {{ cs | random  }}"
tm4 = Template(tpl4)
msg4 = tm4.render(cs=cars)
print(msg4)

print('------------------------------')

# Замена малой буквы ‘о’ на заглавную
tpl5 = 'Автомобиль: {{ cs | replace("о", "О") }}'
tm5 = Template(tpl5)
msg5 = tm5.render(cs=cars)
print(msg5)

print('------------------------------')

# суммирование чисел из списка
the_list = [1, 2, 3, 4, 5]

tpl6 = 'Сумма: {{ tl | sum }}'
tm6 = Template(tpl6)
msg6 = tm6.render(tl=the_list)
print(msg6)

print('------------------------------')

# Блок filter
# {{% filter <название фильтра> %}
# <фрагмент для применения фильтра>
# {% endfilter %}

# вывести имена людей заглавными буквами
persons = [
    {"name": "Алексей", "old": 18, "weight": 78.5},
    {"name": "Николай", "old": 28, "weight": 82.3},
    {"name": "Иван", "old": 33, "weight": 94.0}
]

tpl7 = '''
{%- for u in users -%}
{% filter upper %}{{u.name}}{% endfilter %}
{% endfor -%}
'''

tm7 = Template(tpl7)
msg7 = tm7.render(users=persons)
print(msg7)

print('------------------------------')

# Макроопределения

# Модуль Jinja поддерживает макроопределения для шаблонов, которые полезны, чтобы избежать
# повторяемых определений в соответствии с принципом DRY – Don’t Repeat Yourself (не повторяйся)

# необходимо создать несколько полей ввода input в шаблоне HTML-документа
html = '''
{% macro input(name, value='', type='text', size=20) -%}
    <input type="{{ type }}" name="{{ name }}" value="{{ value|e }}" size="{{ size }}">
{%- endmacro %}

{{ input('username') }}
{{ input('email') }}
{{ input('password') }}
'''
tm8 = Template(html)   # с помощью ключевого слова macro задано
msg8 = tm8.render()    # макроопределение с именем input и набором параметров
print(msg8)

print('------------------------------')

# Вложенные макросы – call

#{% call[(параметры)] <вызов макроса> %}
#<вложенный шаблон>
#{% endcall %}

#На уровне HTML-документа это выглядит так:
#<ul>
#<li>Алексей
#    <ul>
#    <li>age:
#    <li>weight: 78.5
#    </ul>
#<li>Николай
#    <ul>
#    <li>age:
#    <li>weight: 82.3
#    </ul>
#<li>Иван
#    <ul>
#    <li>age:
#    <li>weight: 94.0
#    </ul>
#</ul>


persons = [
    {"name": "Алексей", "old": 18, "weight": 78.5},
    {"name": "Николай", "old": 28, "weight": 82.3},
    {"name": "Иван", "old": 33, "weight": 94.0}
]

#определим макрос, который генерирует начальный список из имен
html2 = '''
{% macro list_users(list_of_user) -%}
<ul>
{% for u in users -%}
    <li>{{u.name}} 
{%- endfor %}
</ul>
{%- endmacro %}

{{list_users(users)}}
'''

tm9 = Template(html2)
msg9 = tm9.render(users=persons)
print(msg9)

print('------------------------------')

# для каждого человека добавим вложенный список с его возрастом и весом
html3 = '''
{% macro list_users(list_of_user) -%}
<ul>
{% for u in list_of_user -%}
    <li>{{u.name}} {{caller(u)}}
{%- endfor %}
</ul>
{%- endmacro %}

{% call(user) list_users(users) %}
    <ul>
    <li>age: {{user.old}}
    <li>weight: {{user.weight}}
    </ul>
{% endcall -%}
'''
tm10 = Template(html3)
msg10 = tm10.render(users=persons)
print(msg10)