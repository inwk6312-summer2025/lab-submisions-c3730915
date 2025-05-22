from netmiko import Netmiko

# List of routers
devices = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.101",  # R1
        "username": "student",
        "password": "Meilab123",
        "secret": "cisco",
        "port": "22",
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.102",  # R2
        "username": "student",
        "password": "Meilab123",
        "secret": "cisco",
        "port": "22",
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.103",  # R3
        "username": "student",
        "password": "Meilab123",
        "secret": "cisco",
        "port": "22",
    }
]

print("Router Uptimes:\n")

for device in devices:
    net_connect = Netmiko(**device)
    net_connect.enable()

    output = net_connect.send_command("show version")
    net_connect.disconnect()

    # Extract uptime line
    for line in output.splitlines():
        if "uptime is" in line:
            print(f"{device['ip']} => {line.strip()}")

