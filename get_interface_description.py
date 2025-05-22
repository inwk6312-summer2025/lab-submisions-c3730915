from netmiko import ConnectHandler

# Define each router individually
r1 = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.101",
    "username": "student",
    "password": "Meilab123",
    "secret": "cisco",
    "port": "22"
}

r2 = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.102",
    "username": "student",
    "password": "Meilab123",
    "secret": "cisco",
    "port": "22"
}

r3 = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.103",
    "username": "student",
    "password": "Meilab123",
    "secret": "cisco",
    "port": "22"
}

# List of routers
routers = [r1, r2, r3]

# List of show commands to execute
commands = [
    "show interface description",
    "show ip interface brief",
    "show version"
]

for device in routers:
    print(f"\nConnecting to {device['ip']}...\n" + "-"*100)
    net_connect = ConnectHandler(**device)
    net_connect.enable()

    for cmd in commands:
        print(f"\n>> Output of '{cmd}':\n")
        output = net_connect.send_command(cmd)
        print(output)

    net_connect.disconnect()
    print("-"*100 + "\nDisconnected.\n")

