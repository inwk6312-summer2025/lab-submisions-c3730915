import logging
import requests
from requests.auth import HTTPBasicAuth
import json

# 日志设置
logging.basicConfig(level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')

# 设备登录信息与地址
HOST = '192.168.1.101'
USER = 'student'
PASS = 'Meilab123'

# 构建基础 URL
BASE_URL = f'http://{HOST}/restconf/api/running/'

# 定义获取接口的函数
def get_interfaces(append_url):
    url = BASE_URL + append_url
    auth = HTTPBasicAuth(USER, PASS)
    headers = {'Accept': 'application/vnd.yang.data+json'}  # 请求返回 JSON 格式
    logging.info(f"URL ==> {url}")
    
    response = requests.get(url, auth=auth, headers=headers)
    
    if response.status_code == 200:
        logging.info(f"Request was successful on {HOST}, Code: {response.status_code}")
        return json.dumps(response.json(), sort_keys=True, indent=4)
    else:
        logging.error(f"Error encountered during request on {HOST}, Code: {response.status_code}")
        return response.text

# 执行函数，打印接口信息
print(get_interfaces('interfaces'))

