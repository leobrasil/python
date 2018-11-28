#!/usr/bin/python3

#import urllib2 
import urllib.request
from bs4 import BeautifulSoup
#   from urlparse import urljoin
from urllib.parse import urlparse
from urllib.parse import urljoin
import sqlite3 as sqlite
import re

ignoreWords=set(['the','of', 'to','and','a','in', 'is', 'it'])

class crawler:
    def __init__(self, dbname):
        self.con = sqlite.connect(dbname)
    
    def __del__(self):
        self.con.close()
    
    def dbcommit(self):
        self.con.commit()
    
    def addToIndex(self, url,soup):
        if self.isIndexed(url):return

        print('indexando %s'%url)
        text = self.getTextOnly(soup)
        words=self.separateWords(text)

        urlid = self.getEntryId('urllist','url',url)

        for i in range(len(words)):
            word = words[i]
            if word in ignoreWords: continue
            wordid=self.getEntryId('wordlist','word',word)
            self.con.execute("insert into wordlocation(urlid,wordid,location) values (%d,%d,%d)"%(urlid,wordid,i))
    
    def getEntryId(self, table, field, value, createnew=True):
        return None
    
    #extrai o texto de uma pagina html - removendo tag
    def getTextOnly(self,soup):
        v=soup.string
        if v==None:
            c = soup.contents
            resulttext=''
            for t in c:
                subtext=self.getTextOnly(t)
                resulttext+=subtext+'\n'
            return resulttext
        else:
            return v.strip()
    
    #separa as palavras de caracteres que seja possivel de imprimir
    def separateWords(self, text):
        splitter = re.compile('\\W*')
        return [s.lower() for s in splitter.split(text) if s!='']
    
    def isIndexed(self, url):
        return False
    
    def addLinkRef(self,urlFrom, urlTo,linkText):
        pass
    
    def crawl(self,pages,depth=2):
        for i in range(depth):
            newpages=set()
            for page in pages:
                try:
                    c=urllib.request.urlopen(page)
                except:
                    print('nao foi possivel abrir a pagina %s'%page)
                    continue
                
                soup=BeautifulSoup(c.read())
                self.addToIndex(page,soup)
                
                links=soup('a')
                for link in links:
                    if ('href' in dict(link.attrs)):
                        url=urljoin(page,link['href'])
                        if url.find("'") !=-1: continue
                        url=url.split('#')[0]
                        if url[0:4]=='http' and not self.isIndexed(url):
                            newpages.add(url)
                        linkText=self.getTextOnly(link)
                        self.addLinkRef(page,url,linkText)
                    self.dbcommit()
                pages=newpages

    def createIndexTables(self):
        self.con.execute('create table urllist(url)')
        self.con.execute('create table wordlist(word)')
        self.con.execute('create table wordlocation(urlid,wordid,location)')
        self.con.execute('create table link(fromid integer, toid integer)')
        self.con.execute('create table linkwords(wordid,linkid)')
        self.con.execute('create index wordidx on wordlist(word)')
        self.con.execute('create index wordurlidx on wordlocation(wordid)')
        self.con.execute('create index urlidx on link(toid)')
        self.con.execute('create index urlfromidx on link(fromid')
        self.dbcommit()