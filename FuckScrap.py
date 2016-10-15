import WebCrawler
import CMSDetector

Crawler = WebCrawler.Crawler()


def request_init():
    url_request = "http://" + str(input("Enter url to crawl and fuck (e.g. www.noobs.com) : "))
    Crawler.request_set(url_request)
    print("\nFuck Scrap just started crawling ...\n")
    print("Sending request ...")
    Crawler.request_send()
    Crawler.request_save()
    Crawler.link_get()


def link_list():
    print("\n** enumerating anchor tags ** \n")
    Crawler.link_enumerate()
    print("\n---> Found "+str(Crawler.link_page_counts())+" links on this page\n")
    print("\n** end enumerating anchor tags **\n")


def linkrel_list():
    print("\n** enumerating link rel resources **\n")
    Crawler.linkrel_links_get()
    Crawler.linkrel_links_enumerate()
    print("\n---> Found "+str(Crawler.linkrel_links_counts())+" resources included in this page")
    print("\n** end enumerating link rel resources **\n")


def script_list():
    print("\n** enumerating scripts sources **\n")
    Crawler.script_links_get()
    Crawler.script_links_enumerate()
    print("\n---> Found "+str(Crawler.script_links_counts())+" scripts included in this page")
    print("\n** end enumerating scripts sources ** \n")


def detect_cms():
    print("\n** Detecting CMS **")
    cms_detector = CMSDetector.CMSDetect(Crawler.request_get())
    if cms_detector.is_wordpress():
        print("\n\tFound : The website is running on wordpress")
        print("\n\t-->Enumerating verified URLs\n")
        print("\t Admin Path : "+str(cms_detector.wordpress_admin_path()))
        print("\t Readme Path : "+str(cms_detector.wordpress_readme_path()))
        print("\t xmlrpc path : "+str(cms_detector.wordpress_xmlrpc_path()))
        print("\t Install path : "+str(cms_detector.wordpress_install_path()))
        print("\t Login path : "+str(cms_detector.wordpress_login_path()))
    else:
        print("\n\tThe website may not be running on a CMS ")
    print("\n** end detecting CMS")


def recon_close():
    Crawler.recon_save()
    print("******************************************\n")
    print("ReconResult save at : ReconFolder/ReconResults/ReconResults.html")
    print("\n******************************************\n")


request_init()
link_list()
linkrel_list()
script_list()
detect_cms()
recon_close()