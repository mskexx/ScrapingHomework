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
    """Client class """

    def get_webpage(self):
        """Obtain html in order to search the title after"""
        # get html
        url_page = "https://www.packtpub.com/packt/offers/free-learning/"
        web = urllib2.urlopen(url_page)
        htmlpage = web.read()
        web.close()
        return htmlpage

    def get_title(self, html):
        """html --> search title --> format title"""
        # search title
        bs = bs4.BeautifulSoup(html, "lxml")
        book_title = bs.find("div", "dotd-title").text

        # format title
        return book_title.lstrip().rstrip()  # Format: /t "title" /t

    def main(self):
        """main function"""
        web = self.get_webpage()
        title = self.get_title(web)
        print title


if __name__ == "__main__":
    fbook = Client()
    fbook.main()
