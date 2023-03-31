#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
#Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#       py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#       py.exe mcb.pyw list - Loads all keywords to clipboard.
#       py.exe mcb.pyw delete - Deletes all keywords from shelve
import shelve, pyperclip, sys
print('Please input your usage details')
x=input()
y=x.split()
mcbShelf=shelve.open('mcb')
if len(y)==2 and y[0].lower()=='save':
    mcbShelf[y[1]]=pyperclip.paste()
elif len(y)==1:
    if y[0].lower()=='list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    if y[0].lower()=='delete':
        mcbShelf.close()
        mcbShelf=shelve.open('mcb','n')
        mcbShelf.close()
        mcbShelf=shelve.open('mcb')
    elif y[0] in mcbShelf:
        pyperclip.copy(mcbShelf[y[0]])
mcbShelf.close()
sys.exit()
