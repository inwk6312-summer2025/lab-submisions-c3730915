from netmiko import Netmiko

# List of all devices in the topology
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

# Loop through each device and get its prompt
for device in devices:
    print(f"\nConnecting to {device['ip']}...")
    net_connect = Netmiko(**device)

    print(f"Default prompt: {net_connect.find_prompt()}")
    
    net_connect.send_command_timing("disable")
    print(f"Disable command: {net_connect.find_prompt()}")
    
    net_connect.enable()
    print(f"Enable command: {net_connect.find_prompt()}")
    
    net_connect.disconnect()

