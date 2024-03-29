import requests
from   requests.auth import HTTPDigestAuth
import json

username    = '12345678'                 # Use any MyEnergi device serial number e.g Eddi or Zappi
password    = 'hXhP3qmzUJ9p73JwtbOsVtS8' # Your MyEnergi API key from the Web portal (this is an example!)
eddi_url    = 'https://s18.myenergi.net/cgi-jstatus-E' # Eddi report
zappi_url   = 'https://s18.myenergi.net/cgi-jstatus-Z' # Zappi report
harvi_url   = 'https://s18.myenergi.net/cgi-jstatus-H' # Hub report
status_url  = 'https://s18.myenergi.net/cgi-jstatus-*' # Everything
dayhour_url = 'https://s18.myenergi.net/cgi-jdayhour-Znnnnnnnn-YYYY-MM-DD # put your Zappi code in here Z12345678 and a date 2022-08-12

print("Accessing MyEnergi System")

#define a function to access the server using a parsed URL 
def access_server(url_request):
    headers = {'User-Agent': 'Wget/1.14 (linux-gnu)'}
    r = requests.get(url_request, headers = headers, auth=HTTPDigestAuth(username, password), timeout=10)
    if (r.status_code == 200):
        print ("") #"Login successful..") 
    elif (r.status_code == 401):
        print ("Login unsuccessful!!! Please check username, password or URL..")
        quit()
    #print (r.json())
    return r.json()

# end-of-function definition

# Display STATUS response data
print ("STATUS")
response_data = access_server(status_url)
print (json.dumps(response_data, sort_keys=False, indent=3))

# Display DAYHOUR response data
print ("DAYHOUR")
response_data = access_server(dayhour_url)
print (json.dumps(response_data, sort_keys=False, indent=3))

# Display HARVI response data
print ("HARVI")
response_data = access_server(harvi_url)
print (json.dumps(response_data, sort_keys=False, indent=3))

# Display EDDI response data
print("EDDI")
response_data = access_server(eddi_url)
print (json.dumps(response_data, sort_keys=False, indent=3))

# Display ZAPPI response data
print ("ZAPPI")
response_data = access_server(zappi_url)
print (json.dumps(response_data, sort_keys=False, indent=3))
for item in response_data['zappi']:
    print ("Zappi Serial number: ", item['sno'])
    print ("Query date: ", item['dat'])
    print ("Query time: ", item['tim'])


# Typical Zappi response
#'{"zappi":[{"sno":12345678,"dat":"12-08-2022","tim":"08:28:08",
#  "ectp2":-2,"ectp3":3,"ectt1":"Internal Load","ectt2":"None","ectt3":"None",
#  "bsm":0,"bst":0,"cmt":254,"dst":1,"div":0,"frq":49.94,"fwv":"3560S3.142",
#  "gen":148,"grd":274,"pha":1,"pri":1,"sta":1,"tz":0,"vol":2406,"che":1.02,
#  "bss":0,"lck":16,"pst":"A","zmo":3,"pwm":5300,"zs":258,"rdc":1,"rac":3,
#  "zsh":1,"zsl":2,"ectp4":8,"ectt4":"None","ectt5":"None","ectt6":"None",
#  "mgl":50,"sbh":17,"sbk":5}]}'
