import pandas as pd

nilaiMTK = {
    'Nama' : ['Ali','Boni','Dodi'],
    'Nilai' : [80,88,89],
    'Grade' : ['A','A','A']
} 

dataNilaiMTK = pd.DataFrame(nilaiMTK)
print(dataNilaiMTK)
