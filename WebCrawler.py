
import requests
import validators
from lxml import html


class Crawler:

    def __init__(self):
        self.url_request = str()
        self.url_html = str()
        self.page_request = str()
        self.page_links = str()
        self.page_links_final = str()
        self.page_links_count = int()
        self.linkrel_links = str()
        self.linkrel_links_final = str()
        self.linkrel_links_count = int()
        self.script_links = str()
        self.script_links_final = str()
        self.script_links_count = int()

    @staticmethod
    def validate_url(url):
        if not validators.url(url):
            return False
        else:
            return True

    def request_set(self, url_request):
        self.url_request = url_request

    def request_send(self):
        self.url_html = requests.get(str(self.url_request))

    def request_get(self):
        return self.url_request

    def request_save(self):
        file = open("ReconFolder/DotText/SaveWeb.txt", "wb")
        file.write(self.url_html.text.encode('utf-8').strip())
        file.close()

    def link_get(self):
        self.page_request = html.fromstring(self.url_html.text)
        self.page_links = set([anchor.attrib['href'] for anchor in self.page_request.cssselect('a')])

    def link_enumerate(self):
        self.page_links_count = 0
        for link in self.page_links:
            if link != '#' and link != '/':
                if not Crawler.validate_url(link):
                    link = self.url_request+link
                print("\t(" + str(self.page_links_count) + ") " + link + "\n")
                link = "&nbsp;&nbsp;<p>" + str(self.page_links_count) + ")&nbsp;" + link + "</p>"
                self.page_links_final = str(self.page_links_final) + str(link)
                self.page_links_count += 1

    def link_page_counts(self):
        return self.page_links_count

    def linkrel_links_get(self):
        self.linkrel_links = [linkrel.attrib['href'] for linkrel in self.page_request.cssselect('link')]

    def linkrel_links_enumerate(self):
        self.linkrel_links_count = 0
        for link in self.linkrel_links:
            if link != '#':
                if not Crawler.validate_url(link):
                    link = self.url_request+link
                print("\t(" + str(self.linkrel_links_count) + ") " + link + "\n")
                link = "&nbsp;&nbsp;<p>" + str(self.linkrel_links_count) + ")&nbsp;" + link + "</p>"
                self.linkrel_links_final = str(self.linkrel_links_final) + str(link)
                self.linkrel_links_count += 1

    def linkrel_links_counts(self):
        return self.linkrel_links_count

    def script_links_get(self):
        self.script_links = [scripts.attrib['src'] for scripts in self.page_request.cssselect('script[src]')]

    def script_links_enumerate(self):
        self.script_links_count = 0
        for link in self.script_links:
            if link != '#':
                if not Crawler.validate_url(link):
                    link = self.url_request+link
                print("\t(" + str(self.script_links_count) + ") " + link + "\n")
                link = "&nbsp;&nbsp;<p>" + str(self.script_links_count) + ")&nbsp;" + link + "</p>"
                self.script_links_final = str(self.script_links_final) + str(link)
                self.script_links_count += 1

    def script_links_counts(self):
        return self.script_links_count

    def recon_save(self):
        file = open("ReconFolder/ReconResults/ReconResults.html", "w")
        content = "<html>" \
                  "<b><center><h3>Target : {0}</h3><h5>FuckScrap V.1</h5></center></b><hr>" \
                  "--<b>Found {1} URLs</b>--<br>{2}<br>" \
                  "--<b>Found {3} included resources--<b>{4}<br>" \
                  "--<b>Found {5} scripts sources --</b>{6}<br>"\
                  "<html>". \
                  format(self.url_request, str(self.page_links_count), str(self.page_links_final),
                         str(self.linkrel_links_count), str(self.linkrel_links_final), str(self.script_links_count),
                         str(self.script_links_final))
        file.write(content)
        file.close()

