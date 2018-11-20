from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import json


def tencent_social():
    url = "https://hr.tencent.com/"
    request = urllib.request.Request(url + 'position.php?&start=10#a')
    response = urllib.request.urlopen(request)
    res_html = response.read()

    out_put = open('tencent.json', 'w')
    html = BeautifulSoup(res_html, 'lxml')

    result = html.select('tr[class="even"]')
    result2 = html.select('tr[class="odd"]')
    result += result2

    items = []
    for site in result:
        item = {}

        name = site.select('td a')[0].get_text()
        detail_link = site.select('td a')[0].attrs['href']
        cata_log = site.select('td')[1].get_text()
        recruit_number = site.select('td')[2].get_text()
        work_location = site.select('td')[3].get_text()
        publish_time = site.select('td')[4].get_text()

        item['name'] = name
        item['detail_link'] = detail_link
        item['cata_log'] = cata_log
        item['recruit_number'] = recruit_number
        item['work_location'] = work_location
        item['publish_time'] = publish_time

        items.append(item)

    line = json.dumps(items, ensure_ascii=False)

    out_put.write(line)
    out_put.close()


if __name__ == '__main__':
    tencent_social()
