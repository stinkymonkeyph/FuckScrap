import requests
import validators
from lxml import html


class CMSDetect:

    def __init__(self):
        self.is_wordpress = False
        self.is_joomla = False
        self.is_drupal = False


    def check_wordpress(self):




