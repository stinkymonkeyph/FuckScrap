import WebCrawler

Crawler = WebCrawler.Crawler()

url_request = "http://"+str(input("Enter url to crawl and fuck (e.g. www.noobs.com) : "))
Crawler.request_set(url_request)
print("\nFuck Scrap just started crawling ...\n")

print("Sending request ...")
Crawler.request_send()
Crawler.request_save()
Crawler.link_get()

print("\n** enumerating anchor tags ** \n")
Crawler.link_enumerate()
print("\n---> Found "+str(Crawler.link_page_counts())+" links on this page\n")
print("\n** end enumerating anchor tags **\n")

print("\n** enumerating link rel resources **\n")
Crawler.linkrel_links_get()
Crawler.linkrel_links_enumerate()
print("\n---> Found "+str(Crawler.linkrel_links_counts())+" resources included in this page")
print("\n** end enumerating link rel resources **\n")

Crawler.recon_save()
print("******************************************\n")
print("ReconResult save at : ReconFolder/ReconResults/ReconResults.html")
print("\n******************************************\n")