from netmiko import Netmiko

# Device list
devices = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.101",
        "username": "student",
        "password": "Meilab123",
        "secret": "cisco",
        "port": "22",
    }
]

# Config commands to create Loopback10 with description
loopback_description = "Loopback created with Netmiko"
loopback_config = [
    "interface Loopback10",
    "ip address 10.10.10.1 255.255.255.255",
    f"description {loopback_description}",
    "no shutdown"
]

for device in devices:
    print(f"🔧 Connecting to {device['ip']} to configure Loopback10...")
    net_connect = Netmiko(**device)
    net_connect.enable()

    # Apply loopback config
    output = net_connect.send_config_set(loopback_config)
    print(output)

    net_connect.disconnect()
    print(f"✅ Configuration done for {device['ip']}.\n")

