import requests
#get une web page
site=requests.get("http://pi-hole.local/admin/")
#if no connection error
if(site.status_code==200) :
    print("site reachable")
#if they are an error
else :
    print("site not reachable")
print("press enter to quit")
input()