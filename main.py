import requests, json, re, os

session = requests.session()
# 配置用户名（一般是邮箱）
email = os.environ.get('EMAIL')
# 配置用户名对应的密码 和上面的email对应上
passwd = os.environ.get('PASSWD')
#微信推送完整链接
WXPUSHER = os.environ.get('WXPUSHER')

login_url = 'https://ikuuu.eu/auth/login'
check_url = 'https://ikuuu.eu/user/checkin'
info_url = 'https://ikuuu.eu/user/profile'

header = {
        'origin': 'https://ikuuu.eu',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}
data = {
        'email': email,
        'passwd': passwd
}
try:
    print('进行登录...')
    response = json.loads(session.post(url=login_url,headers=header,data=data).text)
    print(response['msg'])
    # 获取账号名称
    info_html = session.get(url=info_url,headers=header).text
#     info = "".join(re.findall('<span class="user-name text-bold-600">(.*?)</span>', info_html, re.S))
#     print(info)
    # 进行签到
    result = json.loads(session.post(url=check_url,headers=header).text)
    print(result['msg'])
    content = result['msg']
    # 进行推送
    if WXPUSHER != '':
        push_url = '{}{}'.format(WXPUSHER, content)
        print(push_url)
        requests.get(url=push_url)
        print('推送成功')
except:
    content = '签到失败'
    print(content)
    if WXPUSHER != '':
        push_url = push_url ='{}{}'.format(WXPUSHER, content)
        requests.get(url=push_url)
