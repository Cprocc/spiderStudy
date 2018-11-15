import urllib.request
import urllib.parse
import random
import time
import hashlib
import json


def get_md(value):
    """md5加密"""
    m = hashlib.md5()
    # m.update(value)
    m.update(value.encode('utf-8'))
    return m.hexdigest()


def key_step(post_list):
    u = 'fanyideskweb'
    d = key
    f = str(int(time.time()) + random.randint(1, 10))
    # c = 'sr_3(QOHT)L2dx#uuGR@r'
    c = 'ebSeFb%=XZ%T[KZ)c(sy!'
    post_list["salt"] = f   # "1542258432160"  # 1542258506629
    post_list["sign"] = get_md(u + d + f + c)


key = input("Input the word which you want to translate:")


post_list = {
    "i": key,
    "from": "AUTO",
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    "salt": "1542202603712",
    "sign": "64ec9a8b87f82d8a3ca475a35b1e54db",
    "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_CLICKBUTTION",
    "typoResult": "false",
}

key_step(post_list)

request_list = {
    "Host": " fanyi.youdao.com",
    "Proxy-Connection": " keep-alive",
    # "Content-Length": " 202",
    "Accept": " application/json, text/javascript, */*; q=0.01",
    "Origin": "http//fanyi.youdao.com",
    "X-Requested-With": " XMLHttpRequest",
    "User-Agent": " Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
    # "Content-Type": " application/x-www-form-urlencoded; charset=UTF-8",
    "Referer": "http://fanyi.youdao.com/",
    # "Accept-Encoding": "gzip, deflate",
    "Accept-Language": " zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cookie": "OUTFOX_SEARCH_USER_ID=93133037@10.168.8.63; "
              "OUTFOX_SEARCH_USER_ID_NCOO=235117253.64860407; "
              "_ntes_nnid=c1718ef74309585d32658f4888f882da,1539506494696; "
              "JSESSIONID=aaa_ZfzTzyWnZ_DKvlsCw; ___rl__test__cookies=1542202603704"

}


if __name__ == '__main__':
    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    # url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    data = urllib.parse.urlencode(post_list).encode("utf-8")
    headers = urllib.parse.urlencode(request_list)
    request = urllib.request.Request(url=url, data=data, headers=request_list, method="POST")
    response = urllib.request.urlopen(request)
    context = response.read()
    # context = str(context)
    context = context.decode("utf-8", "ignore")
    context = json.loads(context)
    # print(context)
    print("There is the translate result " + '-'*10)
    print(context['translateResult'][0][0]['tgt'])
    print("There is the smart result " + '-'*10)
    try:
        print(context["smartResult"]["entries"])
    except KeyError:
        print("Sorry no smart for this word")

    # print(context['translateResult'][0][0]['smartResult'])
