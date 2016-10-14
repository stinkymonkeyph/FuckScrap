import requests


class WordpressDetect:
    def __init__(self, url_request):
        self.is_wordpress_site = False
        self.wordpress_admin = str(url_request) + '/wp-admin'
        self.wordpress_changelogs = str(url_request) + '/changelogs.txt'
        self.wordpress_xmlrpc = str(url_request) + '/xmlrpc.php'
        self.wordpress_login = str(url_request) + '/wp-login.php'
        self.wordpress_install = str(url_request) + '/wp-admin/install.php'

    def check_admin_path(self):
        url_check = requests.get(self.wordpress_admin)
        if url_check.status_code == 200:
            self.is_wordpress_site = True

    def check_changelogs_path(self):
        url_check = requests.get(self.wordpress_changelogs)
        if url_check.status_code == 200:
            self.is_wordpress_site = True

    def check_xmlrpc_path(self):
        url_check = requests.get(self.wordpress_xmlrpc)
        if url_check.status_code == 200:
            self.is_wordpress_site = True

    def check_login_path(self):
        url_check = requests.get(self.wordpress_login)
        if url_check.status_code == 200:
            self.is_wordpress_site = True

    def is_wordpress(self):
        self.check_admin_path()
        self.check_changelogs_path()
        self.check_xmlrpc_path()
        self.check_login_path()
        return self.is_wordpress_site
