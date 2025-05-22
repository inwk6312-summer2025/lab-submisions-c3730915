from netmiko import Netmiko
import os

# TextFSM template path (already exported via shell)
os.environ["NET_TEXTFSM"] = "ntc-templates/ntc_templates/templates"  # Optional in-script

# List of router devices
routers = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.101",
        "username": "student",
        "password": "Meilab123",
        "secret": "cisco",
        "port": "22"
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.102",
        "username": "student",
        "password": "Meilab123",
        "secret": "cisco",
        "port": "22"
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.103",
        "username": "student",
        "password": "Meilab123",
        "secret": "cisco",
        "port": "22"
    }
]

for device in routers:
    print(f"\n🔗 Connecting to {device['ip']}...")

    net_connect = Netmiko(**device)
    net_connect.enable()

    # Use TextFSM to parse 'show ip interface brief'
    output = net_connect.send_command("show ip interface brief", use_textfsm=True)
    net_connect.disconnect()

    if isinstance(output, list):
        print(f"✅ Interfaces on {device['ip']}:")
        for interface in output:
            print(f"  - {interface['intf']}")
    else:
        print(f"❌ Failed to parse TextFSM output from {device['ip']}")

    print("-" * 60)

