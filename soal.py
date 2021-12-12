mhs2=("wati","cirebon","jawa barat","membaca",12,"Juni",1999)
mhs1=("budi","majalengka","jawa barat","memancing",17,"April",1996)
daftar=[mhs1,mhs2]

 

i=0
for z in daftar:
    for x in daftar[i]:
        if daftar[i].index(x)==0:
            print(x)
    i=i+1