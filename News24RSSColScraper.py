'''
Created on Nov 2, 2012

@author: Vukosi Marivate
'''
import SimpleXMLScrape as sxml
import urllib2
import sys
from bs4 import BeautifulSoup
from pytagcloud import create_html_data, make_tags
from pytagcloud.lang.counter import get_tag_counts

def GetBodyHTML(soup_file):    
    tag = soup_file
    result = soup_file.find_all("p", "clr_left") 
    final_result = " "
    if len(result) == 1:
        print "unique solution found! :)"
        print result[0]
        final_result = str(result[0])
    elif len(result) > 1:
        print "many solutions found! :'("
    else:
        print "no solutions :("
        
    '''Get the strings in the tag'''

    return final_result

def CreateTagCloud(text):
    tags = make_tags(get_tag_counts(text), maxsize=120)
    create_html_data(tags, size=(900, 600), fontname='Lobster')

def GetTextFromWebPages(urls):
    text = ""
    for url in urls:
        source = urllib2.urlopen(url)
        soup = BeautifulSoup(source, "html")
        text += " " 
        text += GetBodyHTML(soup)
        
    return text

def RunDefault():
    url = "http://feeds.news24.com/articles/News24/Columnists/Khaya-Dlanga/rss"
    tag = "link"
    result_urls = sxml.RunWebXMLScrape(url, tag)
    result_text = GetTextFromWebPages(result_urls)
    SaveText(result_text)

def SaveText(text):
    text_file = open("result.txt", "w")
    text_file.write(text)
    text_file.close()
    
if __name__ == '__main__':
    if len(sys.argv) < 2:
        RunDefault()
        
    
    
    
    
