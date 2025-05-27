import logging
import requests
from requests.auth import HTTPBasicAuth
import json

# 设置日志格式
logging.basicConfig(level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')

# 设备基本信息
HOST = '192.168.1.101'
USER = 'student'
PASS = 'Meilab123'
BASE_URL = 'http://{0}/restconf/api/running/'.format(HOST)

# 获取接口信息
def get_interfaces(append_url, interface_name):
    # 拼接完整 URL
    url = BASE_URL + append_url + interface_name
    auth = HTTPBasicAuth(USER, PASS)
    headers = {'Accept': 'application/vnd.yang.data+json'}

    # 附加参数：用于调试/调深输出等
    params = {'deep': True}
    logging.info(f"URL ==> {url}")

    # 发起 GET 请求
    response = requests.get(url, auth=auth, headers=headers, params=params)

    # 响应处理
    if response.status_code == 200:
        logging.info(f"Request was successful on {HOST}, Code: {response.status_code}")
        return json.dumps(response.json(), sort_keys=True, indent=4)
    else:
        logging.error(f"Error encountered during request on {HOST}, Code: {response.status_code}")
        return response.text

# 调用函数，获取某个接口的详细信息
print(get_interfaces("interfaces/interface/", "GigabitEthernet1?verbose"))

