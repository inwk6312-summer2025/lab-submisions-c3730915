import logging
import requests
from requests.auth import HTTPBasicAuth
import json

# 设置日志格式
logging.basicConfig(level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')

# RESTCONF 设备信息
HOST = '192.168.1.101'
USER = 'student'
PASS = 'Meilab123'
BASE_URL = 'http://{0}/restconf/api/running/'.format(HOST)

# 更新接口配置
def set_interfaces(append_url, interface_name):
    url = BASE_URL + append_url + interface_name
    auth = HTTPBasicAuth(USER, PASS)
    headers = {
        'Accept': 'application/vnd.yang.data+json',
        'Content-Type': 'application/vnd.yang.data+json'
    }

    # 构建要发送的数据
    data = {
        "ietf-interfaces:interface": {
            "name": "GigabitEthernet3",
            "description": "Changed through Restconf",
            "type": "iana-if-type:ethernetCsmacd",
            "enabled": True,
            "ietf-ip:ipv4": {
                "address": [
                    {
                        "ip": "10.0.10.3",
                        "netmask": "255.255.255.0"
                    }
                ]
            },
            "ietf-ip:ipv6": {}
        }
    }

    # 发送 PUT 请求
    response = requests.put(url, auth=auth, headers=headers, data=json.dumps(data))

    # 响应结果
    if response.status_code == 204:
        logging.info(f"Request was successful on {HOST}, Code: {response.status_code}")
        return "success!"
    else:
        logging.error(f"Error encountered during request on {HOST}, Code: {response.status_code}")
        return response.text

# 执行配置函数
print(set_interfaces("interfaces/interface/", "GigabitEthernet3"))

