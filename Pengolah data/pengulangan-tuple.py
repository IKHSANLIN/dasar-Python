mhs1=("budi","majalengka","jawa barat","memancing",17,"april","1996")
for y in mhs1:
    print(y)
    
data=("satu","dua","tiga","empat","lima","enam","tujuh","delapan")
print("data tuple : ",data)

i = 0
hitungA=0

for x in data:
    for y  in data[i]:
        if y=="u":
            hitungA=hitungA+1
    i=i+1

print("Jumlah huruf 'a' ada : ",hitungA)