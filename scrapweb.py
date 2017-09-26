import requests
#from bs4 import BeautifulSoup as bs
from lxml import html
#import pandas as pd

def scrap1(url):
    page1 = requests.get(url)
    #soup1 = bs(page1.content, 'html.parser')
    tree1 = html.fromstring(page1.content)
    titles1 = tree1.xpath('//title/text()')
    links1 = tree1.xpath('//guid/text()')
    authors1 = tree1.xpath('//creator/text()')
    s11 = pd.Series(titles1[2:])
    s12 = pd.Series(links1)
    s13 = pd.Series(authors1)
    o
    print(s11, s12, s13)

def scrap2(url):
    page2 = requests.get(url)
    #soup1 = bs(page1.content, 'html.parser')
    tree2 = html.fromstring(page2.content)
    titles2 = tree2.xpath('//title/text()')
    links2 = tree2.xpath('//guid/text()')
    authors2 = tree2.xpath('//creator/text()')
    s21 = pd.Series(titles2[2:])
    s22 = pd.Series(links2)
    s23 = pd.Series(authors2)
    
    print(s21, s22, s23)
    
def scrap3(url):
    page3 = requests.get(url)
    #soup1 = bs(page1.content, 'html.parser')
    tree3 = html.fromstring(page3.content)
    titles3 = tree3.xpath('//title/text()')
    links3 = tree3.xpath('//guid/text()')
    authors3 = tree3.xpath('//creator/text()')
    s31 = pd.Series(titles3[2:])
    s32 = pd.Series(links3)
    s33 = pd.Series(authors3)

    print(s31, s32, s33)

scrap1('https://www.sindonews.com/feed')
scrap2('http://wartakota.tribunnews.com/rss')
scrap3('http://www.tribunnews.com/rss')
