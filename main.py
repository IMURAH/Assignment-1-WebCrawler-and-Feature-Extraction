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


def extract_features(filename):
    file = open("output/" + filename + ".txt", "rb").read()
    file_data = file.decode()
    features = {}
    for n in file_data:
        keys = features.keys()
        if n in keys:
            features[n] += 1
        else:
            features[n] = 1
    print(features)


def main(root_url, depth):
    print(root_url, depth)
    # Add root URL to FIFO queue with a depth of 0.
    # Dequeue root URL, decrement global depth, fetch, save, and feature extract HTML, parse any links into FIFO queue.
    # For (depth):
    #   Add children of first item in queue to back of queue, with local depth of parent + 1.
    #   If local depth is higher than global depth, skip.


fetch_html("https://en.wikipedia.org/wiki/GW190521")
fetch_html("https://en.wikipedia.org/wiki/2020_Montenegrin_parliamentary_election")

extract_features("httpsenwikipediaorgwikiGW")
