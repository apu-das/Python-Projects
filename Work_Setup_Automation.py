import webbrowser as wb
import os

def workauto():
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    edge_path = 'c:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s'
   
    URLs= ('github.com/apu-das',      #opening automatically some frequently used websites
           'stackoverflow.com',
           'youtube.com',
           'mail.google.com')
    for url in URLs:                 #it'll open the websites in both google chrome and microsoft edge 
        wb.get(chrome_path).open(url)
        wb.get(edge_path).open(url)
workauto()


#to get input from user

# url= input('Enter website URL')
# wb.get(chrome_path).open(url)
