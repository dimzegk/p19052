def bill():
    products=raw_input("Εισάγετε τις εγγραφές του λεξικού με τις αγορές σε λίστα.Π.χ.[['γάλα',1.50]]: ")
    products=products.replace("(","").replace(")","").replace("[","").replace("]","").replace(":",",").replace("'","").replace('"','').replace("€","")
    products=products.split(",")
    products={products[i]: float(products[i+1]) for i in range(0,len(products),2)}
    tax=raw_input("Εισάγετε το ποσοστό φόρου(Π.χ. 10%): ")
    tax=float(tax.strip('%'))/100
    bill=sum(products.values())+sum(products.values())*tax
    print "Το ποσό πληρωμής είναι",round(bill,2),"€."
    
