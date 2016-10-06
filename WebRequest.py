
"""

Web Scanner

"""

import requests


class Crawler:

    def __init__(self):
        self.url_request = str()
        self.url_html = str()

    def request_set(self):
        self.url_request = "http://"+str(input("Enter URL (e.g. www.noobs.com) : "))

    def request_send(self):
        self.url_html = requests.get(str(self.url_request))

    def request_save(self):
        file = open("ReconFolder/DotText/SaveWeb.txt", "wb")
        file.write(self.url_html.text.encode('utf-8').strip())
        file.close()


Crawler = Crawler()
Crawler.request_set()
Crawler.request_send()
Crawler.request_save()
