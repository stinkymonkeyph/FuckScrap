
import requests
from lxml import html


class Crawler:

    def __init__(self):
        self.url_request = str()
        self.url_html = str()
        self.page_request = str()
        self.page_links = str()
        self.page_links_final = str()
        self.page_links_count = int()

    def request_set(self):

        self.url_request = "http://" + str(input("Enter URL (e.g. www.noobs.com) : "))

    def request_send(self):

        self.url_html = requests.get(str(self.url_request))

    def request_save(self):

        file = open("ReconFolder/DotText/SaveWeb.txt", "wb")
        file.write(self.url_html.text.encode('utf-8').strip())
        file.close()

    def link_get(self):

        self.page_request = html.fromstring(self.url_html.text)
        self.page_links = [anchor.attrib['href'] for anchor in self.page_request.cssselect('a')]

    def link_enumerate(self):

        print("--enumerating anchor tags . . .\n")

        self.page_links_count = 0

        for link in self.page_links:
            print("\t(" + str(self.page_links_count) + ") " + link + "\n")
            link = "&nbsp;&nbsp;<p>" + str(self.page_links_count) + ")&nbsp;" + link + "</p>"
            self.page_links_final = str(self.page_links_final) + str(link)
            self.page_links_count += 1
        print("--end of enumeration--")

    def recon_save(self):

        file = open("ReconFolder/ReconResults/ReconResults.html", "w")
        content = "<html><b><center><h3>Target : {0}</h3><h5>FuckScrap V.1</h5></center></b><hr>--<b>Found {1} URLs</b> \
                  --<br>{2}<html>". \
                  format(self.url_request, str(self.page_links_count), str(self.page_links_final))
        file.write(content)
        file.close()
