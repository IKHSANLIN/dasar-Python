bawah = int(input("Masukan batas bawah : "))
atas = int(input("Masukan batas atas : "))

for x in range(bawah,atas+1):
    if (x%2)!=0: 
        print(x,end=" ")