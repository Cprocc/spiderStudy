import random

ua_list = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
           "(KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
           "Mozilla/5.0 (Windows NT 6.1; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
           "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
           "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
           "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 "
           "(KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
           ]

our_headers = {
    "User-Agent": random.choice(ua_list)
}
