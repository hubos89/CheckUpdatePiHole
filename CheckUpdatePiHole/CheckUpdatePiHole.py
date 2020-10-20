import requests
import subprocess
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
        print("install now ?")
        keyboard=input()
        if(keyboard=='y' or keyboard=='o' or keyboard == 'yes' or keyboard == 'oui') :
            #open ssh connection with powershell
            print(">>> pihole -up <<<")
            process=subprocess.run([r'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe','ssh pi@pi-hole.local'])
#if they are an error
else :
    print("site not reachable")
    input()