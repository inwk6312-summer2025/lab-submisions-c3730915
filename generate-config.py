from jinja2 import Environment, FileSystemLoader
import yaml

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('interface-template.j2')

with open('interface-data.yml') as f:
    data = yaml.safe_load(f)

output = template.render(routers=data['routers'])

print(output)

