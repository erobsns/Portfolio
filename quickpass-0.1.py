#!python3

#quickpass.py - manages passwords with shelve module,
#better then a txt file if you dont want to buy
#an encrypted manager.

#modules imported
import shelve,pyperclip
from datetime import date
import pyinputplus as pyip

#for datesaved tracking
today=date.today()

#pyinputplus makes sure the user enters one of the 4 selections
print('''
Would you like to:
1.) Load a password to the clipboard
2.) Save a password
3.) See all passwords and what they belong to
4.) Delete a password''')
initialselect=pyip.inputNum('\nPlease enter a number\n',max=4)

#establishes dictionaries for passwords and save-dates correlating
#to each password, depending on if this is a first time use.
shelfFile=shelve.open('qp')
if 'apw' not in shelfFile:
    tpw={}
else:
    tpw=shelfFile['apw']

if 'pd' not in shelfFile:
    tpd={}
else:
    tpd=shelfFile['pd']

#establishes lists to iterate over when displaying to user as requested.
keys=tpw.keys()
passwords=tpw.values()

#copies a password to the clipboard of the users choosing
if initialselect==1:
    print('\nWhich password would you like to load to the clipboard?')
    for x in tpw:
        print(x)
    whichpwordtoload=input()
    while whichpwordtoload not in tpw:
        print('That password has not been saved')
        whichpwordtoload=input()
    pyperclip.copy(tpw[whichpwordtoload])
    print('Password copied to clipboard.')

#Saves the password a user specifies.
if initialselect==2:
    print('\nWhat is this password for?')
    pbt=input()
    print('\nPlease input the password to save as '+str(pbt)+'.')
    tpw[pbt]=input()
    shelfFile['apw']=tpw
    tpd[pbt]=today
    shelfFile['pd']=tpd
    print('Password Saved.')

#displayes all passwords saved and when they were saved (in case checking if pwnd)
if initialselect==3:
    keys=tpw.keys()
    passwords=tpw.values()
    print('')
    for x in keys:
        print('Password for '+str(x)+' = '+str(tpw[x])+'\n ^^^Saved on: '+str(tpd[x]))

#deletes passwords as requests
if initialselect==4:
    print('\nWhich password would you like to delete?')
    for x in keys:
        print(str(x))
    wwtd=input()
    while wwtd not in tpw:
        print('That password has not been saved')
        wwtd=input()
    del tpw[wwtd]
    shelfFile['apw']=tpw
    print('Password deleted')

#allows the user to see the confirmation of operation complete prior to exiting.
shelfFile.close()
print('\nPlease press the \'enter\' key to exit.')
exit=input()

#-----------------------------------------------------------------
#Next update 0.2:
#if no password currently saved
#if password trying to save already exists
#def a function for prompting which to select for deletion/loadingtc

#Next update 0.3:
#make a warning prior to deleting and an exit strat
#Master password to access all the rest.
#
