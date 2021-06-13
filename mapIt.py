#!python3
#mapIt.py - Launches a map in the browser using an address/name of place from the
#clipboard, you could add it to a hotbar etc for quick mapping.
import webbrowser,pyperclip

#get address/name of place from clipboard
address=pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/'+address)
