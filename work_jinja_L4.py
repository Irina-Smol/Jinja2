from jinja2 import Environment, FileSystemLoader, FunctionLoader

persons = [
    {"name": "Алексей", "old": 18, "weight": 78.5},
    {"name": "Николай", "old": 28, "weight": 82.3},
    {"name": "Иван", "old": 33, "weight": 94.0}
]

file_loader = FileSystemLoader('')  # получение всех шаблонов с корневой папки
env = Environment(loader=file_loader)

tm = env.get_template('work_jinja_L4.html')  # получение нужного шаблона, ссылается на экземлпяр Template
msg = tm.render(users=persons)

print(msg)

print('------------------------------')

# Помимо FileSystemLoader, который отвечает за загрузку шаблонов непосредственно из файловой системы,
# в Jinja есть еще несколько предопределенных загрузчиков:

# PackageLoader – для загрузки шаблонов из пакета;
# DictLoader – для загрузки шаблонов из словаря;
# FunctionLoader – для загрузки на основе функции;
# PrefixLoader – загрузчик, использующий словарь для построения подкаталогов;
# ChoiceLoader – загрузчик, содержащий список других загрузчиков (если один не сработает, выбирается следующий);
# ModuleLoader – загрузчик для скомпилированных шаблонов.

# Определим функцию, которая будет возвращать шаблон
def loadTpl(path):
    if path == "index":
        return '''Имя {{u.name}}, возраст {{u.old}}'''
    else:
        return '''Данные: {{u}}'''


file_loader2 = FunctionLoader(loadTpl)
env2 = Environment(loader=file_loader2)

tm2 = env2.get_template('index')
msg2 = tm2.render(u=persons[0])
print(msg2)