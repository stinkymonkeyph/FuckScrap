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



