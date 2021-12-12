from functools import reduce
data=[1,2,3,4,5]
print(reduce(max,data))

#indexing
data=("pisang","Mangga","pepaya","melon","jeruk","durian","semangka")
print("data pertama : ",data[0])
print("data terakhir : ",data[-1])

print(data)
print("")
print("Data [0:2] --> dari awal hingga sebelum indeks 2",data[0:2])
print("Data [:3] --> 3 data pertama",data[:3])
print("Data[-3:] --> 3 data terakhir : ",data[-3:])
print("Data [::2] lompat dua mulai dari elemen pertama :",data[::2])
print("Data [3::2] --> lompat dua, mulai dari indeks ke 3 : ",data[3::2])
print("Data [-2::1]--> lompat satu ke kanan, mulai dari indeks -2 : ",data[-2::1])
print("Data [-2::-1] --> lompat satu ke kiri,mualai dari indeks ke -2 : ",data[-2::-1])

