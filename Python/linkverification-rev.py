#!python3

#Given the URL of a web page, will attempt to download every
#linked page on the page. The program should flag any pages that have a
#404"Not Found" status code and print them out as broken links.

#module & debug locale
import pyperclip as pyip
from urllib.parse import urlparse
import requests,bs4,logging,re,os
logging.basicConfig(level=logging.CRITICAL, format=' %(asctime)s -%(levelname)s -  %(message)s')

#gets the link from the user to check
print('Please copy the link you want to link-check to your clipboard. Then press enter to continue.')
doesntmatter=input()
urltocheck=pyip.paste()
logging.debug('URLTOCHECK='+str(urltocheck))

#check if url is valid, and then retreive all hrefs for parsing.
res=requests.get(str(urltocheck))
res.raise_for_status()
soup=bs4.BeautifulSoup(res.text, 'html.parser')
elems=soup.select('a[href]')
logging.debug('all hrefs='+str(elems))

#this baseurl will be used to for completing links for hrefs starting with /
baseurl=urlparse(urltocheck).scheme+'://'+urlparse(urltocheck).netloc
logging.debug('baseurl used to add ends to: '+str(baseurl))

# this block is in case there are hrefs linking to next/prev such as (...)
baseusedtosplit=os.path.basename(urltocheck)
logging.debug('snipping:'+str(baseusedtosplit)+' off so we can navigate to other pages on the same site.')
if baseusedtosplit!='':
    listformatofb=urltocheck.split(baseusedtosplit)
    origforbaseadd=listformatofb[0]
else:
    origforbaseadd=urltocheck
logging.debug('origforbaseadd='+str(origforbaseadd))

#counting num of hrefs so we know how many loops to do when grabbing links from hrefs
#and to have a digit to select list inidcies.
links=[]
numofelems=0
for c in elems:
    numofelems+=1
logging.debug('numofelems='+str(numofelems))

#grab 1 link item from href element
for b in range(numofelems):
    templist=[elems[b].get('href')]
    links=links+templist
logging.debug('links='+str(links))

#compile semifinal link list by skipping references (#), reformatting for requests module links starting with /, and adding already formatted pieces.
finallinks=[]
for d in links:
    firstchar=d[0]
    templist=[d]
    if firstchar=='#':
        continue
    if firstchar=='/':
        templist=[str(baseurl+d)]
        finallinks=finallinks+templist
    else:
        finallinks=finallinks+templist
    logging.debug('d='+str(d)+'...\nfirstchar='+str(firstchar)+'...\ntemplist='+str(templist)+'...\nfinallinks='+str(finallinks))

#compile final link list, if links are already good then add em, otherwise other types of links are just added onto origforbaseadd to format for requests.
actualfinallinks=[]
for x in finallinks:
    firstchar=x[0]
    templist=[x]
    if firstchar=='h' or firstchar=='/':
        #logging.debug('skippping: '+str(x))
        actualfinallinks=actualfinallinks+templist
    else:
        templist=[origforbaseadd+x]
        actualfinallinks=actualfinallinks+templist
    logging.debug('x='+str(x)+'...\nfirstchar='+str(firstchar)+'...\ntemplist='+str(templist)+'...\nactualfinallinks='+str(actualfinallinks))

#make contact with each link, if unreachable or there is an issue downloading report error code to user so they can see if its actually an issue or just denied by the site cuz,
#requests module
print('checking for broken links.....')
for q in actualfinallinks:
    res=requests.get(q)
    try:
        res.raise_for_status()
    except Exception as exc:
        print('link broken or just error?: %s' %(exc))
    print('...')


print('if no errors were displayed then all your links on this page are working just fine.')
print('press enter to exit.')
exit=input()
#------------------------------------------------------------------------------------------------
#test on 3 different formats of pages --DONE--
#group into less for loops. --DONE--
#debug--DONE-- annotate--DONE-- tidy--DONE--
