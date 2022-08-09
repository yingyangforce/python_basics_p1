#------------------------------------
# | p3 - | print current date / time
#------------------------------------

from datetime import date, datetime

#date/time, YYYY-MM-DD HH:MM:SS.MSMSMS
currentdatetime = datetime.now()
#raw
print("datetime: ", currentdatetime)
#formatted
print(f"formatted datetime: {currentdatetime:%Y/%m/%d %H:%M}")

#date, YYYY-MM-DD
currentdate = date.today()
#raw
print("date: ", currentdate)
#formatted
print(f"formatted date: {currentdate:%Y/%m/%d}")


