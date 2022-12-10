from jinja2 import Template

name = 'Ира'

tm = Template('Привет {{ name }}')
msg = tm.render(name=name)

msg2 = f"Привет {name}"
print(msg, msg2, sep="\n")

#конструкции, которые можно писать внутри шаблона:
# {% %} - спецификатор шаблона
# {{ }} - выражение для вставки конструкций Python в шаблон
# {# #} - блок комментариев
#   # ## - строковый комментарий

name = 'Федор'
age = 30

templ = Template('Я {{ n }} и мне {{ a }} лет')
message = templ.render(n=name, a=age) # формируется словарь из двух значений
print(message)

templ1 = Template('Я {{ n.upper() }} и мне {{ a * 2 }} лет')
message1 = templ1.render(n=name, a=age)
print(message1)

# ИСПОЛЬЗОВАНИЕ КЛАССА

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

per = Person('Иришка', 20)

templ2 = Template('Я {{ p.name }} и мне {{ p.age }} лет')
message2 = templ2.render(p=per)
print(message2)

templ3 = Template('Я {{ p.getName() }} и мне {{ p.getAge() }} лет') # использование геттеров
message3 = templ2.render(p=per)
print(message3)

# ПЕРЕДАЧА ДАННЫХ С ПОМОЩЬЮ СЛОВАРЯ

person = {'name': 'Миша', 'age': 40}

templ4 = Template('Я {{ p.name }} и мне {{ p.age }} лет')
message4 = templ2.render(p=person)
print(message4)

templ5 = Template("Я {{ p['name'] }} и мне {{ p['age'] }} лет")
message5 = templ2.render(p=person)
print(message5)