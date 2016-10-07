import WebCrawler

Crawler = WebCrawler.Crawler()

url_request = "http://"+str(input("Enter url to crawl and fuck (e.g. www.noobs.com) : "))
Crawler.request_set(url_request)
print("\nFuck Scrap just started crawling ...\n")

print("Sending request ...")
Crawler.request_send()
Crawler.request_save()
Crawler.link_get()

print("\n----enumerating anchor tags ...")
Crawler.link_enumerate()
print("\n----end enumerating anchor tags\n")

Crawler.recon_save()
print("------------------------------------\n")
print("ReconResult save at : ReconFolder/ReconResults/ReconResults.html")
print("------------------------------------\n")