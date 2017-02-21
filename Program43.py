#write a script to make folders and files for HTML
import os


namesite = input("Site name")
author = input("Author")
folderjavascript = input("Do you want a folder for JavaScript?")
foldercss = input("Do you want a folder for CSS?")

if not os.path.exists(namesite):
    os.makedirs(namesite)
    if folderjavascript == 'y':
        os.makedirs(namesite + '\\js')
    if foldercss == 'y':
        os.makedirs(namesite + '\\css')
    file = open(namesite + '\\index.html', 'w+')
    file.write("<html><head><meta><meta name=\"author\" content=\""+author +"\">")
else:
    print("Already done!")