import datetime
import calendar
 
def findDay(date):
    born = datetime.datetime.strptime(date, '%Y-%m-%d').weekday()
    return (findFinalDay(calendar.day_name[born]))
def findFinalDay(day):
if day == "Saturday":
return "Sat"
elif day == "Sunday":
return 'Sun'
elif day == "Monday":
return 'Mon'
elif day == "Tuesday":
return 'Tue'
elif day == "Wednesday":
return 'Wed'
elif day == "Thursday":
return 'Thu'
elif day == "Friday":
return 'Fri'
def getList(dict):
    dist={"Mon":0,"Tue":0,"Wed":0,"Thu":0,"Fri":0,"Sat":0,"Sun":0}
    for key in dict.keys():
    tempkey = findDay(key)
    dist[tempkey] = dict[key] + dist[tempkey]
    return newDist

D = {"2020-01-01":4,"2020-01-02":4,"2020-01-03":6,"2020-01-04":8,"2020-01-05":2,"2020-01-06":6,"2020-01-07":2,"2020-01-08":2}
print(getList(D))