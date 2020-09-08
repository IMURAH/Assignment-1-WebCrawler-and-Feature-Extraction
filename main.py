# Project:      Assignment-1-WebCrawler-and-Feature-Extraction
# Program name: main.py
# Author:       James Browning (jlb0181) and Le Cai
# Date created: September 2020
# Purpose:      Demonstrate understanding of iterative deepening depth-first search, web crawling, and feature
#               extraction.

import os
import urllib.request


def fetch_html(url):
    filename = "output/" + "".join(filter(str.isalpha, url))
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    file = open(filename + ".txt", "wb")
    file.write(urllib.request.urlopen(url).read())
    file.close()


fetch_html("https://en.wikipedia.org/wiki/GW190521")
fetch_html("https://en.wikipedia.org/wiki/2020_Montenegrin_parliamentary_election")
