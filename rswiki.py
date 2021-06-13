#python3
#rswiki.py
#this script opens a prompt for the user to input a term to search the osrswiki for.
#This script then opens the page of the most relevant result.
#a quick-wiki per se. an alternative to opening/tabbing to your browser and opening a new tab, googling your item/monster to wiki, selecting the correct relevant result.
#Myself along with freinds who play this game all use it on our taskbar and find it very useful.
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

    #importing modules and establishing debugging locale.
import requests,sys,webbrowser,bs4,logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -%(levelname)s -  %(message)s')
logging.disable(logging.CRITICAL)

    #obtaining searchterms
print('Please enter what youd like to search the osrs wiki for.')
searchterms=input()
logging.debug(str(searchterms))

    #displays text while downloading the search result page
print('Searching...')
res=requests.get('https://oldschool.runescape.wiki/w/Special:Search?search='+searchterms+'&profile=default&fulltext=1&searchToken=7adyonii8c7vdjg7pm9qipdm'+searchterms)
logging.debug(res)

    #make sure there were no issues with the dl and stops program if so, because that could lead to the wrong result beig displayed etc.
res.raise_for_status()

    #soups up the page for parsing
soup=bs4.BeautifulSoup(res.text,'html.parser')

    #finds the first search result (always in this location).
    #easiest like this because js.
linkElems=soup.select('.mw-search-results > li:nth-child(1) > div:nth-child(1) > a:nth-child(1)')
logging.debug('elements matched:'+str(linkElems))

    #This is for just in case there are no search results for what they searched for (horrible spelling etc)
while linkElems==[]:
    print('There are no results when searching for that, please try again.')
    searchterms=input()
    logging.debug(str(searchterms))
    print('Searching...')
    res=requests.get('https://oldschool.runescape.wiki/w/Special:Search?search='+searchterms+'&profile=default&fulltext=1&searchToken=7adyonii8c7vdjg7pm9qipdm'+searchterms)
    logging.debug(res)
    res.raise_for_status()
    soup=bs4.BeautifulSoup(res.text,'html.parser')
    linkElems=soup.select('.mw-search-results > li:nth-child(1) > div:nth-child(1) > a:nth-child(1)')
    logging.debug('elements matched:'+str(linkElems))

    #since its js we cant 'get' it so i just converted the whole thing to a string and split it until only the end of the search result url remained.
pageExtpresplit=str(linkElems)

logging.debug('Pulling url for first search result out of js manually')
logging.debug(pageExtpresplit)

pageExt1stsplit=pageExtpresplit.split(' ')
logging.debug(pageExt1stsplit)

pageExt2ndsplit=str(pageExt1stsplit[2])
logging.debug(pageExt2ndsplit)

pageExt3rdsplit=pageExt2ndsplit.strip('href=')
logging.debug(pageExt3rdsplit)

pageExt=pageExt3rdsplit.strip('/"')
logging.debug(pageExt)

    #and finally opens url to the wiki'd page
urlToOpen='https://oldschool.runescape.wiki/'+pageExt
print('Opening', urlToOpen)
webbrowser.open(urlToOpen)
#macenabled--Done--
