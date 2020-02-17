with open("numbers.txt") as f:
    numbers=f.read().split(",")
x=raw_input("Εισάγετε μία 6αδα αριθμών: ")
count=0
from collections import Counter
for i in range (0,len(numbers)):
    common=(Counter(x) & Counter(numbers[i]))
    summ=(sum(common.values()))
    if summ==4:
        print "Ç ôåôñÜäá",numbers[i],"åßíáé äéáèÝóéìç ãéá ôïõò 6 áñéèìïýò."
        count=+1
if count==0:
    print "Δεν υπάρχει διαθέσιμη 4αδα."
