merekMobil={"avanza","xenia","expander","ertiga"}
mobilku={"avanza","xenia"}

if mobilku.issubset(merekMobil):
    print("set mobilku adalah subset merkmobil")

merekMobil.add("inova")
print("setelah ditambahkan inova (add) : ",merekMobil)

merekMobil.remove("inova")
print("print setelah dikurangi inova (remove) :",merekMobil)

merekMobil.update(["avanza","sigra"])
print("Diupdate dengan avanza dan sigra : ",merekMobil)

merekMobil.difference_update(mobilku)
print("difference_update : ",merekMobil)
    