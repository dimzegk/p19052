with open("numbers.txt") as f:
    numbers=f.read().split(",")
x=raw_input("�������� ��� 6��� �������: ")
count=0
from collections import Counter
for i in range (0,len(numbers)):
    common=(Counter(x) & Counter(numbers[i]))
    summ=(sum(common.values()))
    if summ==4:
        print "� �������",numbers[i],"����� ��������� ��� ���� 6 ��������."
        count=+1
if count==0:
    print "��� ������� ��������� 4���."


    

