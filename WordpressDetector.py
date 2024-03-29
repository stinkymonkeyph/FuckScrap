import requests


class WordpressDetect:

    def __init__(self, url_request):
        self.is_wordpress_site = False
        self.has_admin_path = False
        self.has_login_path = False
        self.has_readme_path = False
        self.has_xmlrpc_path = False
        self.has_install_path = False
        self.wordpress_admin = str(url_request) + '/wp-admin'
        self.wordpress_readme = str(url_request) + '/readme.html'
        self.wordpress_xmlrpc = str(url_request) + '/xmlrpc.php'
        self.wordpress_login = str(url_request) + '/wp-login.php'
        self.wordpress_install = str(url_request) + '/wp-admin/install.php'

    def path_admin_check(self):
        url_check = requests.get(self.wordpress_admin)
        if url_check.status_code == 200:
            self.is_wordpress_site = True
            self.has_admin_path = True

    def path_readme_check(self):
        url_check = requests.get(self.wordpress_readme)
        if url_check.status_code == 200:
            url_check_text_rendered = url_check.text
            if url_check_text_rendered.find("Semantic Personal Publishing Platform") != -1:
                self.is_wordpress_site = True
                self.has_readme_path = True

    def path_xmlrpc_check(self):
        url_check = requests.get(self.wordpress_xmlrpc)
        if url_check.status_code == 200:
            self.is_wordpress_site = True
            self.has_xmlrpc_path = True

    def path_login_check(self):
        url_check = requests.get(self.wordpress_login)
        if url_check.status_code == 200:
            self.is_wordpress_site = True
            self.has_login_path = True

    def path_install_check(self):
        url_check = requests.get(self.wordpress_install)
        if url_check.status_code == 200:
            self.is_wordpress_site = True
            self.has_install_path = True

    def path_admin_get(self):
        if self.has_admin_path:
            return self.wordpress_admin

    def path_login_get(self):
        if self.has_login_path:
            return self.wordpress_login

    def path_readme_get(self):
        if self.has_readme_path:
            return self.wordpress_readme

    def path_xmlrpc_get(self):
        if self.has_xmlrpc_path:
            return self.wordpress_xmlrpc

    def path_install_get(self):
        if self.has_install_path:
            return self.wordpress_install

    def is_wordpress(self):
        self.path_admin_check()
        self.path_readme_check()
        self.path_xmlrpc_check()
        self.path_login_check()
        return self.is_wordpress_site
