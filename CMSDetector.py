import WordpressDetector


class CMSDetect:

    def __init__(self, url_request):
        self.wordpress_detector = WordpressDetector.WordpressDetect(url_request)
        self.is_wordpress_site = False
        self.is_joomla = False
        self.is_drupal = False

    def is_wordpress(self):
        self.is_wordpress_site = self.wordpress_detector.is_wordpress()
        return self.is_wordpress_site

    def wordpress_admin(self):
        return self.wordpress_detector.path_admin_get()

    def wordpress_changelogs(self):
        return self.wordpress_detector.path_changelogs_get()

    def wordpress_xmlrpc(self):
        return self.wordpress_detector.path_xmlrpc_get()

    def wordpress_login(self):
        return self.wordpress_detector.path_login_get()

    def wordpress_install(self):
        return self.wordpress_detector.path_install_get()