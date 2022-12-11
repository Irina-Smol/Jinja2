from jinja2 import Environment, FileSystemLoader

file_loader = FileSystemLoader('')
env = Environment(loader=file_loader)

template = env.get_template('work_jinja_L6_about.html')

output = template.render()
print(output)

# здесь используется новый тип блоков – именованные блоки, которые в
# самом простом случае записываются по синтаксису:
# {% block <имя блока> %}  
# {% endblock %}