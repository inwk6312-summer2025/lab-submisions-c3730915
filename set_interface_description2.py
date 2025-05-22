from netmiko import Netmiko
import logging

# Optional: Enable logging to stdout for debugging
# logging.basicConfig(filename="netmiko.log", level=logging.DEBUG)

# Define the device(s)
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

for device in devices:
    print(f"\n🔧 Connecting to {device['ip']} to apply config from file...\n")
    net_connect = Netmiko(**device)
    net_connect.enable()

    # Read and apply configuration commands from file
    output = net_connect.send_config_from_file("changes.txt")
    print(output)

    net_connect.disconnect()
    print(f"✅ Configuration completed on {device['ip']}.\n")

