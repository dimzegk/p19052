import datetime
date=raw_input("Εισάγετε την ημερομηνία (ΗΗ/ΜΜ/ΕΕΕΕ): ")
date=date.split("/")
month=int(date[1])
year=int(date[2])
for i in range (0,len(date)):
    date[i]=int(date[i])
date=datetime.date(date[2],date[1],date[0])
now=datetime.date.today()
diff=abs(date-now)
print "Οι δύο ημερομηνίες απέχουν",diff.days," μέρες ή",(diff.days)*24,"ώρες ή",(diff.days)*24*3600,"δευτερόλεπτα."
from calendar import monthrange
days=monthrange(year,month)
print "Ο μήνας της ημερομηνίας που δώσατε έχει",days[1],"μέρες."
