'''
Created on Nov 2, 2012

@author: Vukosi Marivate
'''

import urllib2
import sys
from bs4 import BeautifulSoup

def ScrapeXML(soup_file, tag):
    
    result = soup_file.findAll(tag)
    if len(result) == 1:
        print "unique solution found! :)"
    elif len(result) > 1:
        print "many solutions found! :D"
    else:
        print "no solutions :("
        
    '''Get the strings in the tag'''
    final_result = []
    for items in result:
        final_result.append(items.string)
    return final_result
         
def RunXMLScrape(file, tag):
    soup = BeautifulSoup(file, "xml")
    return ScrapeXML(soup, tag)

def RunWebXMLScrape(xml_url, tag):
    source = urllib2.urlopen(xml_url)
    return RunXMLScrape(source, tag)

if __name__ == '__main__':
    
    if len(sys.argv) < 2:
        url = "http://feeds.news24.com/articles/News24/Columnists/Khaya-Dlanga/rss"
        tag = "link"
    else:
        url = sys.argv[1]
        tag = sys.argv[2]
        
    RunWebXMLScrape(url, tag)
    
    
