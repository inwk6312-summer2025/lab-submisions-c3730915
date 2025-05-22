import yaml
from jinja2 import Environment, FileSystemLoader
from netmiko import Netmiko

# Load YAML files
hosts = yaml.load(open('hosts.yml'), Loader=yaml.SafeLoader)
interfaces = yaml.load(open('interfaces.yml'), Loader=yaml.SafeLoader)

# Load Jinja2 template
env = Environment(
    loader=FileSystemLoader('.'),
    trim_blocks=True,
    lstrip_blocks=True
)
template = env.get_template('interfaces_config_template.j2')

# Render the loopback configuration
loopback_config = template.render(data=interfaces)

# Push config to each host
for host in hosts["hosts"]:
    print(f"🔗 Connecting to {host['name']}...")
    net_connect = Netmiko(
        host=host["name"],
        username=host["username"],
        password=host["password"],
        port=host["port"],
        device_type=host["type"]
    )

    print(f"✅ Logged into {host['name']} successfully")

    output = net_connect.send_config_set(loopback_config.splitlines())
    print(f"📤 Pushed config to {host['name']}:\n{output}")

    net_connect.disconnect()
    print(f"🔌 Disconnected from {host['name']}\n")

print("🎉 All done!")

