import WebCrawler


Crawler = WebCrawler.Crawler()

url_request = "http://"+str(input("Enter an address to crawl and fuck (e.g. www.noobs.com) : "))
Crawler.request_set(url_request)
print("FuckScrap just started crawling ...\n")

print("Sending the request ... \n")
Crawler.request_send()
Crawler.request_save()

Crawler.link_get()
print("--enumerating anchor tags . . .\n")
Crawler.link_enumerate()
print("--end of anchor tags enumeration--")

Crawler.recon_save()
print("---------------------------------\n")
print("--RESULT SAVE IN ReconFolder/ReconResults/ReconResults.html")
print("---------------------------------\n")

