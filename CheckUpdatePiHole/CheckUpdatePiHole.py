import requests
import os
import xml.etree.ElementTree as ElementTree
#get une web page
site=requests.get("http://pi-hole.local/admin/")
#if no connection error
if(site.status_code==200) :
    #get html
    sitehtml=site.text
    #search in the html if update is available
    result=sitehtml.find("Update available!")
    #if update available write it
    if(result != -1) :
        print("Update available!")
#if they are an error
else :
    print("site not reachable")
print("press enter to quit")
input()