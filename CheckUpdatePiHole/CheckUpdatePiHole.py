import requests
site=requests.get("http://pi-hole.local/admin/")
if(site.status_code==200) :
    print("site reachable")
else :
    print("site not reachable")
print("press enter to quit")
input()