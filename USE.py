

#The user should download the csv file and add their token and timestamp,
#I couldn't make it work to calculate the current timestamp
#Besides these points it posts to the Gamebus address the activity 
import csv
import requests, time, calendar;

from datetime import datetime
now = datetime.now()
year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")
date = " " + year + "-" + month + "-" + day;

url = "https://api3.gamebus.eu/v2/activities?dryrun=false&fields=personalPoints.value"

with open('datasets/glucose-test-data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
  #making it now with a test date = the first date from the file  

### change test date, timestamp

    test_date = '05/22/2020'
    for row in csv_reader:
        if (line_count == 0) or (line_count == 1):
                line_count+=1
        else: 
            current_date = row[2]
            current_date = str(current_date)
            
            if any(current_date):
                record_type = row[3]
                date_only = current_date[0:10]
                #comparing dates and record type
                if (date_only == test_date) and (record_type == '1'):
                        number = row[5]
                        if any(number):
                            number = float(number)
                            #timestamp of the current data is calculated but is not used 
                            timestamp = 1000*(calendar.timegm(time.strptime(current_date, '%m/%d/%Y %H:%M')))
                            print(number)
                            payload = {'activity': (None,"""{"gameDescriptor": 61,
                                                                        "dataProvider": 1, 
                                                                        "date": PUT CURRENT TIMESTAMP,
                                                                        "propertyInstances":[{
                                                                        "property": 88, 
                                                                        "value":""" + str(5.6) + """
                                                                          }],
                                                                        "players": [329]}""")}
                            line_count += 1
                            print("send")
                            headers = {'Authorization':'Bearer HERE THE AUTHORIZATION TOKEN'}
                            response = requests.post(url, headers=headers, files = payload)
                            print(response.text.encode('utf8'))
                            print(timestamp)
                            print(current_date)
                                    
