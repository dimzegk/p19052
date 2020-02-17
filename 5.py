f=raw_input("Εισάγετε το όνομα του αρχείου ή την θέση του αρχείου:  ")
with open(f,"r") as f:
    words=f.read().split()
for i in range(0,len(words)):
    if words[i].isalpha():
      if len(words[i])>3:
        words[i]=words[i][1:]+words[i][0]+'ay'
    elif words[i][:-1].isalpha():
       words[i]=words[i][1:-1]+words[i][0]+'ay'+words[i][-1]
print (" ".join(words))
