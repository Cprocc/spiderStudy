import our_random_UserAgent
import urllib.request
import urllib.parse

our_headers = our_random_UserAgent.our_headers
url = "http://tieba.baidu.com/home/main?un=%E4%BD%A0%E7%9A%84%E8%83%BD%E5%8A%9B%E" \
      "5%A5%BD%E5%BC%BA%E6%98%AF&id=57a2e4bda0e79a84e883bde58a9be5a5bde5bcbae698af7f4e?t=1" \
      "409235716&fr=index&red_tag=w1788638741"

headers = {
    "Host": "tieba.baidu.com",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": 1,
    "User-Agent": our_headers,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    # "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cookie": "BAIDUID=85F462EE77BEAA4E003B23877B325163:FG=1; BIDUPSID=AB3B79CE218079E86B2F85034A321CD5; "
              "PSTM=1529058510; TIEBAUID=010f689d0181af53382d6906; TIEBA_USERTYPE=91d2c8f77ac67d83cfecd6f0; "
              "bdshare_firstime=1532863257977; BDUSS=nRVSUZaSklySGR5dGdZWGN2SX5KbnBaS2NzM3g5Q2U4MmV2c3FXeVgyTTZw"
              "UEpiQVFBQUFBJCQAAAAAAAAAAAEAAABXon9OxOO1xMTcwaa6w8e~yscAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
              "AAAAAAAAAAAAAAAAAAAAAADoXy1s6F8tbd; STOKEN=b97667906f371c74721feb724b30aa6528614a73ea04e1aa09852bb75bf"
              "b5ff6; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; MCITY=-%3A; H_PS_PSSID=1466_21095_18559_26350; delPer=0;"
              " BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; pgv_pvi=325387264; pgv_si=s6670657536; "
              "BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; PSINO=1; "
              "Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1542026389,1542190013,1542288449,1542290700; "
              "Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1542290815"
}

our_headers = our_random_UserAgent.our_headers

request = urllib.request.Request(url=url, headers=our_headers)
context = urllib.request.urlopen(request)
context = context.read()
context = context.decode('utf-8')
print(context)
