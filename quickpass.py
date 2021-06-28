#!python3

#quickpass.py - manages passwords for when stubborn freinds/family
#wont buy a real password manager with encryption, but this is
#better than writing passwords into a text file.

#modules imported
import shelve
import pyperclip
import pyinputplus as pyip

#pyinputplus makes sure the user enters one of the 3 selections
print('please input the number of your selection')
print('''Would you like to:
1.) Load a password to the clipboard
2.) Save a password
3.) See all passwords and what they belong to''')
initialselect=pyip.inputNum('Please enter a number\n',max=3)

opw=shelve.open('opw')

#to load a password the user must type in which he wants
#after all the keys are shown to him, then it is copied to the
#clipboard to paste into his password needing app
if initialselect==1:
    print('Which password would you like to load to the clipboard?')
    print(list(opw.keys()))
    whichpwordtoload=input()
    while whichpwordtoload not in list(opw.keys()):
        print('That password has not been saved')
        whichpwordtoload=input()
    pyperclip.copy(opw[whichpwordtoload])
    print('Password copied to clipboard.')

#saving password pretty self explanitory code
if initialselect==2:
    print('What is this password for?')
    pbt=input()
    print('Please input the password to save as '+str(pbt)+'.')
    opw[pbt]=input()
    print('Password Saved.')

#cant iterate through opw well because its shelve so instead do
#it this way
if initialselect==3:
    keys=list(opw.keys())
    passwords=list(opw.values())
    for x in keys:
        print('Password for '+str(x)+' = '+str(opw[x]))
opw.close()

print('enter any key to exit.')
exit=input()

#-----------------------------------------------------------------
#To update:

#make output prettier.
#add delete pword function
#
