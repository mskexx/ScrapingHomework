#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
'''
Get free book title

@author: marcos.susin.mzn@gmail.com
'''
import urllib2
import bs4


class Client(object):

    def get_title(self):
        """ obtener html"""
        url_page = "https://www.packtpub.com/packt/offers/free-learning/"
        web = urllib2.urlopen(url_page)
        htmlpage = web.read()
        web.close()

        """ buscar titulo """
        bs = bs4.BeautifulSoup(htmlpage, "lxml")
        title = bs.find("div", "dotd-title").text
        title.lstrip().rstrip()
        print title


if __name__ == "__main__":
    fbook = Client()
    fbook.get_title()
