# 导入 Jinja2 和 PyYAML 库
from jinja2 import Environment, FileSystemLoader
import yaml

# 声明模板环境（当前目录）
ENV = Environment(loader=FileSystemLoader('.'))

# 自定义过滤器函数：根据接口名称返回 Mbps 速率
def get_interface_speed(interface_name):
    """
    get_interface_speed 根据接口名称返回默认 Mbps 速度，
    通过检测名称中是否包含 'gigabit' 或 'fast' 关键词。
    """
    if 'gigabit' in interface_name.lower():
        return 1000
    if 'fast' in interface_name.lower():
        return 100
    return 'unknown'

# 将函数注册为 Jinja2 过滤器（注意：传的是函数名，不是函数调用）
ENV.filters['get_interface_speed'] = get_interface_speed

# 加载模板文件
template = ENV.get_template("template-task8.j2")

# 加载 YAML 数据文件
with open("data-task7.yml") as f:
    interfaces = yaml.load(f, Loader=yaml.SafeLoader)

# 渲染模板并输出结果
print(template.render(interface_list=interfaces))

