import requests
import base64

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53',
}
session = requests.session()
session.headers.update(headers)

captchaurl = 'https://authserver.nju.edu.cn/authserver/captcha.html'
captcha = session.get(captchaurl, timeout=5).content
captcha = base64.b64encode(captcha).decode('utf-8')

import time
st = time.time()
ret = session.post('https://xxx.xxx.xxx.xxx/api', data={'captcha': captcha})
print(time.time() - st)
print(ret, ret.text)
