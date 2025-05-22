import pexpect

# Router configuration parameters
routers = {
    "R1": "192.168.1.101",
    "R2": "192.168.1.102",
    "R3": "192.168.1.103",
    "R4": "192.168.1.104"
}

username = "student"
password = "Meilab123"
enable_password = "cisco"

for router_name, ip in routers.items():
    print(f"Connecting to {router_name} at {ip}...")

    try:
        child = pexpect.spawn(f"ssh {username}@{ip}", timeout=10)
        child.expect("password:")
        child.sendline(password)

        # Enter enable mode
        child.expect("#")
        child.sendline("enable")
        child.expect("Password:")
        child.sendline(enable_password)

        # Enter configuration terminal
        child.expect("#")
        child.sendline("configure terminal")
        child.expect("(config)#")

        # Extract router number
        router_number = ip.split('.')[-1]

        # Send configuration
        commands = [
            f"hostname R{router_number}",
            "no ip domain lookup",
            "enable password cisco",
            "ip domain name inwk.local",
            "username student privilege 15 secret Meilab123",
            "interface gigabitEthernet 1",
            f"ip address 192.168.1.10{router_number} 255.255.255.0",
            "no shutdown",
            "ip ssh version 2",
            "line con 0",
            "logging synchronous",
            "line vty 0 4",
            "login local",
            "transport input ssh",
            "end",
            "write memory"
        ]

        for cmd in commands:
            child.sendline(cmd)
            child.expect("#|>")

        print(f"{router_name} configured successfully.\n")

        child.sendline("exit")
        child.close()

    except Exception as e:
        print(f"Failed to configure {router_name}: {e}")

