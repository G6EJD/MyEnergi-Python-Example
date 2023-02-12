import requests
from   requests.auth import HTTPDigestAuth
from   datetime import datetime

Zappi_SN    = 'your Zappi Serial Number Here'
Eddi_SN     = 'your Eddi Serial Number Here'

Hub_SN      = 'Your Hub Serial Number Here'
API_Key     = 'Your API key here'

username    = Hub_SN  # Use any MyEnergi device serial number e.g Hub, Eddi or Zappi
password    = API_Key # Your MyEnergi API key from the Web portal

#Example calls to the API
eddi_url    = 'https://s18.myenergi.net/cgi-jstatus-E' # Eddi report
zappi_url   = 'https://s18.myenergi.net/cgi-jstatus-Z' # Zappi report
harvi_url   = 'https://s18.myenergi.net/cgi-jstatus-H' # Hub report
status_url  = 'https://s18.myenergi.net/cgi-jstatus-*' # Everything
dayhour_url = 'https://s18.myenergi.net/cgi-jdayhour-Z' + Zappi_SN #  -CCYY-MM-DD

print("Creating Report\n")

#define a function to access the server using a parsed URL 
def access_server(url_request):
    headers = {'User-Agent': 'Wget/1.14 (linux-gnu)'}
    r = requests.get(url_request, headers = headers, auth=HTTPDigestAuth(username, password), timeout=10)
    if (r.status_code == 200):
        pass
        #print ("Login success") #"Login successful..") 
    elif (r.status_code == 401):
        print ("Login unsuccessful!!! Please check username, password or URL..")
        quit()
    #print (r.json())
    return r.json()

#define a function to retrieve data for a day
def day_results(day, month, year):
    failed = "false"
    response_data = access_server(dayhour_url + '-' + str(year) + '-' + str(month) + '-' + str(day))
    #print(dayhour_url + '-' + str(year) + '-' + str(month) + '-' + str(day))
    ChargeAmount = 0
    ImportAmount = 0
    ExportAmount = 0
    GeneraAmount = 0
    #print (json.dumps(response_data, sort_keys=False, indent=2))
    try:
        response_data['U' + Zappi_SN]
    except:
        failed = "true"
        pass
    if (failed == "false"):
        for item in response_data['U' + Zappi_SN]:
            try:
                #print ("Query Month: ", item['dow'], item['yr'], item['mon'], item['dom'], item['hr'], item['h1d'], item['imp'], item['gep'])
                ChargeAmount += item['h1d']
                ImportAmount += item['imp']
                ExportAmount += item['exp']
                GeneraAmount += item['gep']
            except:
                pass
         #End of for loop
    #print ("%.2f" % (total/3600/1000),"kWh")
    ChargeMonthResults[day] = (ChargeAmount/3600/1000)
    ImportMonthResults[day] = (ImportAmount/3600/1000)
    ExportMonthResults[day] = (ExportAmount/3600/1000)
    GeneraMonthResults[day] = (GeneraAmount/3600/1000)

# end-of-function definitions

## Now get the data for each day
ImportMonthResults = [0.0] * 32 # Space for 31-days/month
ImportYearResults  = [0] * 10 # Sets a 10-year maximum of results, could be more or less
ExportMonthResults = [0] * 32 # Space for 31-days/month
ExportYearResults  = [0] * 10 # Sets a 10-year maximum of results, could be more or less
GeneraMonthResults = [0] * 32 # Space for 31-days/month
GeneraYearResults  = [0] * 10 # Sets a 10-year maximum of results, could be more or less
ChargeMonthResults = [0] * 32 # Space for 31-days/month
ChargeYearResults  = [0] * 10 # Sets a 10-year maximum of results, could be more or less
StartYear     = 2021 # System installed October 2021
EndYear       = 2023

BOLD_ON  = '\033[1m'
BOLD_OFF = '\033[0m'

today = datetime.now()
CurrentMonth = int(today.strftime("%m"))
CurrentYear  = int(today.strftime("%y")) + 2000

for Year in range(StartYear, EndYear + 1):
    print ("\nProducing Monthly History for year: " + str(Year))
    print("{0:>10}".format("Month") + "{0:>10}".format("Charge") + "{0:>10}".format("Import") + "{0:>10}".format("Export") + "{0:>14}".format("Generation"))
    for Month in range(1, 13):
        if (Year == CurrentYear and Month > CurrentMonth):
            pass
        else:
            total_charge = 0
            total_import = 0
            total_export = 0
            total_genera = 0
            for Day in range(1, 31):
                day_results(Day, Month, Year)
                if (ChargeMonthResults[Day] != 0):
                    total_charge += ChargeMonthResults[Day]
                    total_import += ImportMonthResults[Day]
                    total_export += ExportMonthResults[Day]
                    total_genera += GeneraMonthResults[Day]
                #print(Day, ("%.1d" % ChargeMonthResults[Day] + "kWh")))
            print(BOLD_ON, end='')
            print("{0:10}".format(Month), end='')
            print("{:8.1f}".format(total_charge),  end='')
            print("{:11.1f}".format(total_import), end='')
            print("{:8.1f}".format(total_export), end='')
            print("{:10.1f}".format(total_genera))
            print(BOLD_OFF, end='')
    
            ChargeYearResults[Year - StartYear] += total_charge
            ImportYearResults[Year - StartYear] += total_import
            ExportYearResults[Year - StartYear] += total_export
            GeneraYearResults[Year - StartYear] += total_genera
    #End of month
    print(BOLD_ON, end='')
    print("Yearly Total [" + str(Year) + "] (kWh)\n", end='')
    print('{:18.1f}'.format(ChargeYearResults[Year - StartYear]), end='')
    print('{:11.1f}'.format(ImportYearResults[Year - StartYear]), end='')
    print('{:8.1f}'.format(ExportYearResults[Year - StartYear]), end='')
    print('{:10.1f}'.format(GeneraYearResults[Year - StartYear]))
    print(BOLD_OFF, end='')
  #End of year

print(BOLD_ON, end='')
print("\nSummary of Charge Energy per-year (kWh)")
for Year in range(StartYear, EndYear + 1): 
    print("Total for Year [" + str(Year) + "] = " + str('{:5.1f}'.format(ChargeYearResults[Year - StartYear])))

print("\n   Total of all Years =" + str('{:6.1f}'.format(sum(ChargeYearResults))) + " kWh")
print("              Savings =" + str(" £"+'{:5.2f}'.format(sum(ChargeYearResults)*0.34)))
print(BOLD_OFF, end='')
