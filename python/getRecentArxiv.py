# -*- coding: utf-8 -*-
# Hongwei Qin @2017.02.22
# Used to download the arxiv papers of cs.cv
# results in pdfs, paper url and title list, abstract list, and papers on detection
# to download paper at 07:30 everyday, type `crontab -e` in shell, and add the following line
# 30 7 * * * python your_absolute_cvToolbox_path/python/getRecentArxiv.py >> ~/download.log 2>&1

import requests
from lxml import etree
import os
import time
#import re
#from multiprocessing.dummy import Pool

def getHtml(url):
    html = requests.get(url).content
    selector = etree.HTML(html)
    return selector

def getContent(htm, xpathStr):
    selector = htm
    content = selector.xpath(xpathStr)
    return content

def getDownPdf(cons, title, folder):
    fn = '%s' % title
    pa = os.path.abspath('.') + '/' + 'arxiv' + '/%s' % folder
    #pa = os.path.dirname(__file__) + '/' + 'arxiv' + '/%s' % folder
    if not os.path.exists(pa):
        os.makedirs(pa)
    fl = pa + '/%s.pdf' % fn
    if not os.path.exists(fl):
        r = requests.get(cons)
        with open(fl, "wb") as code:
            code.write(r.content)
    else:
        print('pdf already exists, continue...\n')

if __name__ == '__main__':
    url_recent = 'http://arxiv.org/list/cs.CV/recent'
    print url_recent
    # xpath of each page
    xp1 = '//dl[1]//*[@class="list-identifier"]//a[2]//@href'  # pdf href list
    xp2 = '//dl[1]//*[@class="list-title mathjax"]/text()'  # Title
    url_abstract = '//dl[1]//*[@class="list-identifier"]//a[1]//@href'  # abstract href list
    xp_date = '//*[@id="dlpage"]/h3[1]/text()'  # date->folder

    htm0 = getHtml(url_recent)
    cons1 = getContent(htm0, xp1)  # get pdfs' href
    cons2 = getContent(htm0, xp2)  # get papers' title
    cons_date = getContent(htm0, xp_date) # get date
    cons_abstract = getContent(htm0, url_abstract)  # get papers' abstract

    folder = time.strftime("%Y-%m-%d", time.strptime(cons_date[0], "%a, %d %b %Y")) # get date string and convert to yyyy-mm-dd

    print folder + ': there are %s' % len(cons1) + '  papers'
    print 'downloading pdfs...'

    if not os.path.exists('arxiv'):
        os.mkdir('arxiv')
    list_title = 'arxiv/' + folder + '_title.txt'
    list_abstract = 'arxiv/' + folder + '_abstract.md'
    list_detection = 'arxiv/' + folder + '_detection_related.md'
    f_title = open(list_title, 'w')
    f_abstract = open(list_abstract, 'w')
    f_detection = open(list_detection, 'w')

    for indx in range(0, len(cons1)):
        # download pdf and write title
        href = 'http://arxiv.org' + cons1[indx]
        title = cons2[2 * indx + 1]
        paper_info = '%s.' % (1 + indx) + ' ' + href + ' ' + title
        print '%s.' % (1 + indx) + ' ' + href + ' ' + title
        getDownPdf(href, title, folder)
        f_title.write(paper_info)

        # write abstract and authors
        abstract_href = 'http://arxiv.org' + cons_abstract[indx]
        htm_abstract = getHtml(abstract_href)
        abstract_field = '//*[@class="abstract mathjax"]/text()'  # abstract
        authors_field = '//*[@name="citation_author"]//@content' # authors
        paper_abstract = getContent(htm_abstract, abstract_field)  # get papers' abstract
        paper_authors = getContent(htm_abstract, authors_field)  # get papers' authors
        abstract_info = '%s.' % (1 + indx) + ' [' + title[1:-1] + '](' + abstract_href + ')\n'
        f_abstract.write(abstract_info)
        for author in paper_authors:
            f_abstract.write(author.encode('utf-8') + '; ')
        f_abstract.write('\n\n' + paper_abstract[1][1:] + '\n\n')

        # write abstract in the topic of detection
        if ('detection' in title) or ('Detection' in title) or ('Detecting' in title) or ('detecting' in title):
            f_detection.write(abstract_info)
            for author in paper_authors:
                f_abstract.write(author.encode('utf-8') + '; ')
            f_detection.write('\n\n' + paper_abstract[1][1:] + '\n\n')

    f_title.close()
    f_abstract.close()
    f_detection.close()
