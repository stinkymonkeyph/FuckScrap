import requests


class JoomlaDetect:

    def __init__(self, url_request):
        self.is_joomla = False
        self.joomla_admin = str(url_request) + "/administrator"
        self.joomla_login = str(url_request) + "/login"

    def admin_path(self):
        url_request = requests.get(self.joomla_admin)
        if url_request.status_code == 200:
            self.is_joomla = True

    def login_path(self):
        url_request = requests.get(self.joomla_login)
        if url_request.status_code == 200:
            self.is_joomla = True
