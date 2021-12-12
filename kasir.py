def total(a,b):
        return a*b
def hitungNet(c,d):
        return total(c,d)-5000
    
jumlah = int(input("Jumalh : "))
harga_satuan=int(input("Harga : "))

if(total(jumlah,harga_satuan)>=50000):
    print(hitungNet(jumlah,harga_satuan))
    
else:
    print(total(jumlah,harga_satuan))
    
   