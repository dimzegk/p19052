import datetime
date=raw_input("�������� ��� ����������(��/��/����): ")
date=date.split("/")
month=int(date[1])
year=int(date[2])
for i in range (0,len(date)):
    date[i]=int(date[i])
date=datetime.date(date[2],date[1],date[0])
print date
now=datetime.date.today()
print now
diff=abs(date-now)
print "�� ��� ����������� �������",diff.days," ����� �",(diff.days)*24,"���� �",(diff.days)*24*3600,"������������."
from calendar import monthrange
days=monthrange(year,month)
print "� ����� ��� ����������� ��� ������ ����",days[1],"�����."
