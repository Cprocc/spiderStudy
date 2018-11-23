import threading
from queue import Queue
from lxml import etree
import requests
import json
import time
from url2.our_random_UserAgent import our_headers

CRAWL_EXIT = False
PARSE_EXIT = False


class ThreadCrawler(threading.Thread):
    def __init__(self, thread_name, page_queue, data_queue):
        super(ThreadCrawler, self).__init__()
        self.thread_name = thread_name
        self.page_queue = page_queue
        self.data_queue = data_queue
        self.headers = our_headers

    def run(self):
        print("Start" + self.thread_name)
        while not CRAWL_EXIT:
            try:
                page = self.page_queue(False)
                url = "http://www.qiushibaike.com/8hr/page/" + str(page) + "/"
                content = requests.get(url, headers=self.headers).text
                time.sleep(1)
                self.data_queue.put(content)
            except:
                pass
        print("ending" + self.thread_name)


class ThreadParse(threading.Thread):
    def __init__(self, thread_name, data_queue, file_name, lock):
        super(ThreadParse, self).__init__()
        self.thread_name = thread_name
        self.data_queue = data_queue
        self.file_name = file_name
        self.lock = lock

    def run(self):
        print("start" + self.thread_name)
        while not PARSE_EXIT:
            try:
                html = self.data_queue.get(False)
                self.parse(html)
            except:
                pass
        print("exit" + self.thread_name)

    def parse(self, html):
        html = etree.HTML(html)
        node_list = html.xpath('//div[contains(@id, "qiushi_tag")]')

        for node in node_list:
            # //div[@class="author clearfix"]/a[@href]/h2
            username = node.xpath('.//div[@class="author clearfix"]/a[@href]/h2')[0].text
            image = node.xpath('.//div[@class="thumb"]//@src')
            content = node.xpath('.//div[@class="content"]/span')[0].text
            zan = node.xpath('.//i')[0].text
            comments = node.xpath('.//i')[0].text

            items = {
                "username": username,
                "image": image,
                "content": content,
                "zan": zan,
                "comments": comments,
            }

            with self.lock:
                self.file_name.write(json.dumps(items, ensure_ascii=False))


def main():
    page_queue = Queue(10)
    for i in range(1, 11):
        page_queue.put(i)

    # 采集结果的队列，每一页的html源码
    data_queue = Queue()

    file_name = open("duanzi_thread.json", "a")
    lock = threading.Lock()

    crawl_list = ["crawler_thread-1", "crawler_thread-2", "crawler_thread-3"]
    thread_crawl = []
    for thread_name in crawl_list:
        thread = ThreadCrawler(thread_name, page_queue, data_queue)
        thread.start()
        thread_crawl.append(thread)

    parse_list = ['parse_thread-1', 'parse_thread-2', 'parse_thread-3']
    thread_parse =[]
    for thread_name in parse_list:
        thread = ThreadParse(thread_name, data_queue, file_name, lock)
        thread.start()
        thread_parse.append(thread)

    #
    while not page_queue.empty():
        pass

    global CRAWL_EXIT
    CRAWL_EXIT = True

    print("page_queue is empty")

    for thread in thread_crawl:
        thread.join()
        print("1")

    #
    while not data_queue.empty():
        pass

    global PARSE_EXIT
    PARSE_EXIT = True

    for thread in thread_parse:
        thread.join()
        print("2")

    #
    with lock:
        file_name.close()
    print("thanks for using")


if __name__ == '__main__':
    main()
