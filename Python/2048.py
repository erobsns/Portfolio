#!python3

#Program Goal:
#2048 is a simple game where you combine tiles by sliding them up, down, left, or
#right with the arrow keys. You can actually get a fairly high score by repeatedly
#sliding in an up, right, down, and left pattern over and over again. Write a program
#that will open the game at https://gabrielecirulli.github.io/2048/ and keep sending up,
#right, down, and left keystrokes to automatically play the game.
#DONE

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pathlib import Path
import sys,logging
#Path just for ease of use with pathing
#selenium keys need to input game controls
#selenium webdriver need for browser control functions
#sys for exit at end
#logging for debug

logging.basicConfig(level=logging.CRITICAL, format=' %(asctime)s -%(levelname)s -  %(message)s')
#log level at CRITICAL currently

basedir2048=Path.cwd()
logging.info('CWD is '+str(basedir2048))
datacheckdir=basedir2048/'2048.txt'
logging.info('directory to txt file is '+str(datacheckdir))
#directory for the text file we'll be using for record tracking even after program ends
#Shelve module would just eat more resources and this is simple enough that its
#unneeded.

if datacheckdir.exists()==False:
    currentrecord=open('2048.txt','w')
    currentrecord.write('0')
    currentrecord.close()
    currentrecord=open('2048.txt')
else:
    currentrecord=open('2048.txt')
#If our text file doesnt exist already, create it next to the script itself.
#Prepare current record score text file for reading in both cases.

logging.info('current status of current record variable-post existcheck'+str(currentrecord))
browser=webdriver.Firefox()
logging.info('current browser variable '+str(browser))
browser.get('https://play2048.co/')
#define the browser well be using with selen
#open the link to the game

htmlElem = browser.find_element_by_tag_name('html')
logging.info('element we have selected, should be whole page '+str(htmlElem))
for x in range(300):
    htmlElem.send_keys(Keys.UP)
    htmlElem.send_keys(Keys.RIGHT)
    htmlElem.send_keys(Keys.DOWN)
    htmlElem.send_keys(Keys.LEFT)
currentscore=browser.find_elements_by_class_name('score-container')
logging.info('what we have selected to pull our current score for this run from: '+str(currentscore))
#selecting whole page for sending keys to play the game
#send this key combination over and over 300 times (which is well over
#what we would ever get to in number of moves.)
#acquire the current score displayed at the end of the game.

logging.info('the .text we are pulling from the currentrun score element: '+currentscore[0].text)
print('This play\'s score is: %s' %(currentscore[0].text))

if int(currentscore[0].text)>int(currentrecord.read()):
    print('New record!')
    currentrecord.close()
    currentrecord=open('2048.txt','w')
    currentrecord.write(currentscore[0].text)
    currentrecord.close()
    currentrecord=open('2048.txt')
    logging.info('currentrecord variable status after beating old record: '+str(currentrecord))
else:
    currentrecord.close()
    currentrecord=open('2048.txt')
    logging.info('currentrecord variable status if didnt beat record:'+str(currentrecord))
#if the current score is higher than what we have logged in our text file as our highest
#then print "new record!", write our new high score to the text, and prepare it for re-
#read for display of current record.
#otherwise if we didnt beat our record just prepare the current record for a display
#in the next line.

print('Current record is: '+currentrecord.read())
browser.quit()
print('Press Enter to quit')
quitprompt=input()
#quit the browser so the user doesnt have to
#but leave everything else open so the user can see the score and record.
#until they are ready.

sys.exit()
#then exit the program.


#--------------------------------------------------------------------------------
#quit browser after--DONE--
#only quit after confirmation to see score--DONE--
#debug--DONE-- annotate--DONE-- tidy--DONE--
