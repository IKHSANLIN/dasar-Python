data= [1,2,3,4,5,6]

def kuadrat(x):
    return x**2

hasil=map(kuadrat, data)
print(list(hasil))

data= [1,2,3,4,5,6]
hasil=map(lambda x : x**2, data)
print(list(hasil))

hasil=map(lambda x : x != 4,data)
print(list(hasil))

hasil=filter(lambda x : x != 4 , data)
print(list(hasil))
